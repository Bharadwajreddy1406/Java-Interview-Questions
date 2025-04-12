# 💻Leetcode 1358:  Problem: Number of Substrings Containing All Three Characters

- **📅 Date:** 2025-04-12
- **📌 Platform:** LeetCode
- **🏷️ Tags:** #dsa #slidingwindow #string #medium

---

## 🧾 Problem Statement

> Given a string `s`, return the number of substrings that contain at least one occurrence of all three characters `'a'`, `'b'`, and `'c'`.

---

## 🔓 Trigger / Intuition

> ✨ _Brute force came first, then an optimization when realizing once a valid substring is found, the rest automatically become valid. Finally, the best approach keeps track of last seen indices and just adds `min(last[0], last[1], last[2]) + 1` if all are seen._

---

## 🛠️ Data Structures / Concepts Used

> 📘 _Sliding window idea, prefix optimization, and index tracking_  
> - Array to store last seen positions of `'a'`, `'b'`, `'c'`.

---

## 🧪 Test Cases

```

Input: s = "abcabc" Output: 10

Input: s = "aaacb" Output: 3

````

---

## ✍️ My Explanation / Approach

> 🧠 _Step-by-step logic in your words_
> - First brute force: For every i, check substrings `s[i:j]` and maintain a freq array of a/b/c.
> - Optimization: As soon as we find a valid substring, all future j values are valid. So just add `s.length() - j`.
> - Final approach:
>   - Keep an array `last[3]` for last seen positions of `a`, `b`, `c`.
>   - For each char at index `i`, update its last seen.
>   - If all 3 are seen, take the smallest last seen index and add it + 1 to the answer.

---
![[1358-image1.png]]

![[1358-image2.png]]
## 🧑‍💻 Final Code

```java
class Solution {
    public int numberOfSubstrings(String s) {
        int ans = 0;
        int last[] = new int[]{-1, -1, -1};

        for (int i = 0; i < s.length(); i++) {
            last[s.charAt(i) - 'a'] = i;
            ans += (1 + Math.min(last[0], Math.min(last[1], last[2])));
        }

        return ans;
    }
}
````

---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n)`
    
- **Space Complexity:** `O(1)`
    

---

## 🗒️ Notes / Mistakes / To Revisit?

> - ✅ Optimization from brute force to constant space was neat.
>     
> - ❌ Initially checked all substrings — slow.
>     
> - 🔁 Mark for revision? [ ] Yes [x] No
>     

---
