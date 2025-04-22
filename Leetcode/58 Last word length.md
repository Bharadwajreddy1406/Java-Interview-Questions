# 🧠 LeetCode 58 – Length of Last Word

**Link**: [https://leetcode.com/problems/length-of-last-word](https://leetcode.com/problems/length-of-last-word)  
**Date**: 22-04-2025  
**Tags**: `string`, `two-pointer`, `traversal`  
**Platform**: LeetCode  
**Difficulty**: Easy

---

## 🚀 Problem
Given a string `s` consisting of words and spaces, return the length of the **last word** in the string.  
A word is a maximal substring consisting of non-space characters only.

---

## 🧠 Intuition
We need to:
1. Ignore trailing spaces.
2. Traverse backwards from the end and count characters until the next space.

---

## 🧩 Data Structures Used
- No additional data structures; just index-based traversal.

---

## 🧪 Test Cases

| Input             | Output |
|------------------|--------|
| `"Hello World"`   | `5`    |
| `"   fly me   to   the moon  "` | `4` |
| `"a"`             | `1`    |
| `"day  "`         | `3`    |

---

## ✅ Python Solution
```python
class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()[::-1]  # Trim spaces and reverse the string
        c = 0
        for i in s:
            if i != " ":
                c += 1
            else:
                break
        return c
````

---

## ⚡ Java Solution (Optimal)

```java
class Solution {
    public int lengthOfLastWord(String s) {
        int length = 0;
        int i = s.length() - 1;

        // Skip trailing spaces
        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }

        // Count length of the last word
        while (i >= 0 && s.charAt(i) != ' ') {
            length++;
            i--;
        }

        return length;
    }
}
```

---

## ⏱️ Time & Space Complexity

- **Time**: O(n)
    
- **Space**: O(1)
    

---

## 🧠 Reflection

- Great example of a simple two-pointer/traversal problem.
    
- Clean reverse-traversal avoids the need for `.split()` or extra space.
    
---
