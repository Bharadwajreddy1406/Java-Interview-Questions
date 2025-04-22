# ✅ LeetCode 720 - Longest Word in Dictionary

**Link**: [https://leetcode.com/problems/longest-word-in-dictionary](https://leetcode.com/problems/longest-word-in-dictionary)  
**Date**: {{DATE}}  
**Tags**: `Trie`, `Sorting`, `Prefix`, `String`  
**Difficulty**: Medium

###### **`this problem is similar to leetcode 1858`**

---

## 📘 Problem Summary

Given a list of words, return the **longest word** in the dictionary such that **every prefix** of the word is also in the dictionary.

If there are multiple answers with the same length, return the **lexicographically smallest** one.

---

## ✅ Solution using Trie

```java
class Node {
    Node[] arr;
    boolean isEnd;

    Node() {
        arr = new Node[26];
        isEnd = false;
    }
}

class Trie {
    Node root;

    Trie() {
        root = new Node();
    }

    public void insert(String word) {
        Node node = root;
        for (char ch : word.toCharArray()) {
            if (node.arr[ch - 'a'] == null) {
                node.arr[ch - 'a'] = new Node();
            }
            node = node.arr[ch - 'a'];
        }
        node.isEnd = true;
    }

    public boolean search(String prefix) {
        Node node = root;
        for (char ch : prefix.toCharArray()) {
            if (node.arr[ch - 'a'] == null) return false;
            node = node.arr[ch - 'a'];
        }
        return node.isEnd;
    }
}
````

### 🔍 Main Function

```java
class Solution {
    public String longestWord(String[] words) {
        Trie t = new Trie();
        for (String word : words) {
            t.insert(word);
        }

        Arrays.sort(words);
        String w = "";

        for (String word : words) {
            boolean check = true;
            for (int i = 1; i < word.length(); i++) {
                check &= t.search(word.substring(0, i));
            }

            if (check && (
                word.length() > w.length() ||
                (word.length() == w.length() && word.compareTo(w) < 0)
            )) {
                w = word;
            }
        }

        return w;
    }
}
```

---

## 🛠️ Issue Faced

Initially used this condition:

```java
if (check && word.length() >= w.length()) {
    w = word;
}
```

This fails in cases where two words have the same length. The word that appears **later** in the sorted array replaces the earlier one, even if it's **not lexicographically smaller**.

---

## 🧪 Failing Test Case

```java
Input: ["a", "banana", "app", "appl", "ap", "apply", "apple"]
```

- ❌ Before fix: `"apply"`
    
- ✅ Expected: `"apple"`
    

---

## ✅ Fix

Updated the condition to:

```java
if (check && (
    word.length() > w.length() ||
    (word.length() == w.length() && word.compareTo(w) < 0)
)) {
    w = word;
}
```

This ensures the lexicographically **smallest** word is chosen when there is a tie in length.

---

## ⏱️ Time & Space Complexity

- **Time**:
    
    - Trie insertions: O(N * L)
        
    - Prefix checking per word: O(L²)
        
    - Sorting: O(N log N)
        
- **Space**: O(N * L) for Trie
    

Where:

- `N` = number of words
    
- `L` = max length of any word
    

---
