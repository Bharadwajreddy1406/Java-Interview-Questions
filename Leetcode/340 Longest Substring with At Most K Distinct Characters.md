# 💻 Problem: Longest Substring with At Most K Distinct Characters

- **📅 Date:** 12-04-2025
- **📌 Platform:** LeetCode
- **🏷️ Tags:** #dsa #sliding-window #string #medium

---

## 🧾 Problem Statement

> Given a string `s` and an integer `k`, return the length of the longest substring of `s` that contains at most `k` distinct characters.

---

## 🔓 Trigger / Intuition

> ✨ _It’s a sliding window problem, which clicked after recalling the leetcode 904 "Fruit Into Baskets" problem._  
> _The key idea is to keep track of distinct characters in the window and adjust the left pointer when the count exceeds `k`._

---

## 🛠️ Data Structures / Concepts Used

> 📘 _Sliding Window Technique_  
> - **Frequency Map**: Used to track the count of characters in the current window.
> - **Sliding Window**: Expand the window by moving the right pointer and contract it by adjusting the left pointer when the number of distinct characters exceeds `k`.

---

## 🧪 Test Cases

```

Input: "eceba", k = 2 Output: 3

Input: "aa", k = 1 Output: 2

````

---

## ✍️ My Explanation / Approach

> 🧠 _The approach uses a sliding window to maintain a range of at most `k` distinct characters._  
> - Step 1: We loop over the string and expand the window by adding characters from the right pointer to the frequency map.
> - Step 2: If the number of distinct characters exceeds `k`, we shrink the window by moving the left pointer and updating the frequency map.
> - Step 3: For each valid window, we update the maximum length found so far.

---

## 🧑‍💻 Final Code

```java
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        Map<Character, Integer> cnt = new HashMap<>();
        int n = s.length();
        int ans = 0, j = 0;
        for (int i = 0; i < n; ++i) {
            char c = s.charAt(i);
            cnt.put(c, cnt.getOrDefault(c, 0) + 1);
            while (cnt.size() > k) {
                char t = s.charAt(j);
                cnt.put(t, cnt.getOrDefault(t, 0) - 1);
                if (cnt.get(t) == 0) {
                    cnt.remove(t);
                }
                ++j;
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
    
    - We store at most `k` distinct characters in the frequency map.
        

---

## 🗒️ Notes / Mistakes / To Revisit?

> - ✅ The sliding window approach worked well here, and I was able to maintain the frequency map efficiently.
>     
> - ❌ No major mistakes. Need to watch out for edge cases where `k` is greater than the length of the string.
>     

---
