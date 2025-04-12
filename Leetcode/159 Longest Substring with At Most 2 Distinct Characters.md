# 💻 Problem: Longest Substring with At Most Two Distinct Characters

- **📅 Date:** 2025-04-12
- **📌 Platform:** LeetCode
- **🏷️ Tags:** #dsa #sliding-window #string #medium

---

## 🧾 Problem Statement

> Given a string `s`, return the length of the longest substring that contains at most two distinct characters.

---

## 🔓 Trigger / Intuition

> ✨ _This is a classic sliding window problem. The idea struck when recalling problems like 904 "Fruit Into Baskets" where we manage a window and make adjustments when a condition is violated (i.e., when there are more than two distinct characters)._  
> 340 leetcode is a similar problem too
> _We can track the frequency of characters in the current window using a counter, and if the window exceeds two distinct characters, shrink it from the left._

---

## 🛠️ Data Structures / Concepts Used

> 📘 _Sliding Window Technique_  
> - **Frequency Map**: Used to track the count of characters in the current window.
> - **Sliding Window**: Expand the window by moving the right pointer and contract it by adjusting the left pointer when the number of distinct characters exceeds 2.

---

## 🧪 Test Cases

```

Input: "eceba", k = 2 Output: 3 Explanation: The substring is "ece" which its length is 3.

Input: "ccaabbb", k = 2 Output: 5 Explanation: The substring is "aabbb" which its length is 5.

````

---

## ✍️ My Explanation / Approach

> 🧠 _The sliding window approach works by expanding the window to include new characters and contracting it when the number of distinct characters exceeds two._  
> - Step 1: Loop through the string and add characters to the frequency map.
> - Step 2: If the number of distinct characters exceeds 2, shrink the window from the left by moving the left pointer and updating the frequency map.
> - Step 3: Track the length of the longest valid window and return it after processing the entire string.

---

## 🧑‍💻 Final Code

```java
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> cnt = new HashMap<>();
        int n = s.length();
        int ans = 0;
        for (int i = 0, j = 0; i < n; ++i) {
            char c = s.charAt(i);
            cnt.put(c, cnt.getOrDefault(c, 0) + 1);
            while (cnt.size() > 2) {
                char t = s.charAt(j++);
                cnt.put(t, cnt.get(t) - 1);
                if (cnt.get(t) == 0) {
                    cnt.remove(t);
                }
            }
            ans = Math.max(ans, i - j + 1);
        }
        return ans;
    }
}
````

---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n)`
    
    - We iterate through the string once, and the left pointer (`j`) only moves forward, making the time complexity linear.
        
- **Space Complexity:** `O(k)`
    
    - We store at most `2` distinct characters in the frequency map.
        

---

## 🗒️ Notes / Mistakes / To Revisit?

> - ✅ Sliding window approach works well to handle the constraint of two distinct characters.
>     
> - ❌ No major mistakes.
>     

---
