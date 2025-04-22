# 🧵 LeetCode 1858 – Longest Word With All Prefixes

**Link**: [https://leetcode.com/problems/longest-word-with-all-prefixes](https://leetcode.com/problems/longest-word-with-all-prefixes)  
**Date**: {{DATE}}  
**Tags**: `Trie`, `Prefix Check`, `Sorting`  
**Platform**: LeetCode  
**Difficulty**: Medium

---

## 🧠 Problem Summary
You are given a list of words. Find the **longest word** such that **all prefixes** of the word are also in the list.

> Example:  
    If `"apple"` is in the list, then to be valid, `"a"`, `"ap"`, `"app"`, `"appl"` must all also be present.

---

## 🔍 Intuition
- Use a **Trie** to insert all words.
- For each word, check whether all its prefixes are valid words using the Trie.
- Among valid candidates, return the **longest** one (lexicographically smallest if tied).

---

## 🛠️ Custom Trie Implementation

### `Node` class:
```java
class Node {
    Node[] arr;
    boolean isEnd;

    Node() {
        arr = new Node[26];
        isEnd = false;
    }
}
````

### `Trie` class:

```java
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
```

---

## ✅ Main Logic

```java
class Solution {
    public String longestWord(String[] words) {
        Trie t = new Trie();

        // Insert all words into the trie
        for (String word : words) {
            t.insert(word);
        }

        // Sort to handle lexicographical condition
        Arrays.sort(words);

        String w = "";
        for (String word : words) {
            boolean check = true;

            // Check if all prefixes are present
            for (int i = 1; i < word.length(); i++) {
                check &= t.search(word.substring(0, i));
            }

            if (check && word.length() >= w.length()) {
                w = word;
            }
        }

        return w;
    }
}
```

---
start loop from 1, coz if u do from 0, then one sub string would be empty one, which's not in Trie, so it'll give u false only..........
## 🧪 Example

### Input:

```java
["a", "app", "ap", "appl", "apple", "apply"]
```

### Output:

```java
"apple"
```

✅ Because all prefixes `"a"`, `"ap"`, `"app"`, `"appl"` are present.

---

## ⏱️ Complexity

### Time:

- Insert: O(N * L)
    
- Search for prefixes: O(N * L²) worst case (due to substring)
    
- Sorting: O(N log N)
    

### Space:

- O(N * L) for Trie
    

Where:

- N = number of words
    
- L = average length of words
    

---

## 💡 Reflections

- Trie shines for prefix-based problems.
    
- Substring calls are slightly costly; can optimize using pointer traversal inside Trie.
    
- Sorting helps break ties based on lexicographical order.
    
---
