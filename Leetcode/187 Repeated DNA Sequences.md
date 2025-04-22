# 🧬 LeetCode 187 – Repeated DNA Sequences

**Link**: [https://leetcode.com/problems/repeated-dna-sequences](https://leetcode.com/problems/repeated-dna-sequences)  
**Date**: `22-04-2025`
**Tags**: `HashSet`, `String`, `Sliding Window`  
**Platform**: LeetCode  
**Difficulty**: Medium

---

## 🧠 Problem Summary
You're given a DNA string `s`, and you need to find **all the 10-letter-long sequences (substrings)** that occur **more than once**.

---

## 🧩 Intuition
- Use a **sliding window** of size 10.
- Keep track of substrings seen so far in a set.
- If a substring appears more than once, add it to the result.

---

## ⚠️ Issue with Initial Implementation
```java
StringBuilder sb = new StringBuilder("");
...
sb.append(s.charAt(right));
if (sb.length() > 10) sb.delete(0, 1);
````

- This version maintains the window using `StringBuilder` and deletes the first char when size exceeds 10.
    
- ❗ `sb.delete(0, 1)` is **O(n)** every time — which becomes inefficient when repeated many times.
    

---

## ✅ Optimized Approach

Instead of modifying a `StringBuilder`, just use `s.substring(i, i + 10)` in a loop — faster and cleaner.

---

## ✨ Final Code (Java)

```java
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int n = s.length();
        Set<String> set = new HashSet<>();
        Set<String> list = new HashSet<>();
        
        for (int i = 0; i <= n - 10; i++) {
            String a = s.substring(i, i + 10);
            if (set.contains(a)) list.add(a);
            set.add(a);
        }
        
        return new ArrayList<>(list);
    }
}
```

---

## 🐢 Brute Version (Sliding Window with StringBuilder)

```java
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int left = 0;
        int right = 0;
        int n = s.length();
        Set<String> set = new HashSet<>();
        Set<String> list = new HashSet<>();
        StringBuilder sb = new StringBuilder();

        while (right < n) {
            sb.append(s.charAt(right));
            if (sb.length() > 10) {
                sb.delete(0, 1);  // O(n) operation
            }

            if (sb.length() == 10) {
                String dna = sb.toString();
                if (set.contains(dna)) list.add(dna);
                set.add(dna);
            }

            right++;
        }

        return new ArrayList<>(list);
    }
}
```

---

## 🧪 Example

### Input:

```text
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
```

### Output:

```text
["AAAAACCCCC", "CCCCCAAAAA"]
```

---

## ⏱️ Time & Space Complexity

### Optimized Version

- **Time**: O(n)
    
- **Space**: O(n) for the sets
    

---

## 🔁 Reflections

- Avoid string mutations (`StringBuilder.delete`) inside tight loops when possible.
    
- Always consider **substring-based windowing** for fixed-length sliding windows in strings.
    
---
