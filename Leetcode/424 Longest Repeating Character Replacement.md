# 💻424.  Problem: Longest Repeating Character Replacement

- **📅 Date:** 2025-04-12
- **📌 Platform:** LeetCode
- **🏷️ Tags:** #dsa #slidingwindow #string #medium

---

## 🧾 Problem Statement

> You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character.  
> Perform this operation at most `k` times.  
> Return the length of the longest substring containing the same letter you can get after performing the above operations.

---

## 🔓 Trigger / Intuition

> ✨ _When adjusting characters to make substrings uniform, think of how many characters you need to change to make a window valid.  
   If `window_length - most_frequent_char_count <= k`, it's a valid window._

---

## 🛠️ Data Structures / Concepts Used

> 🧠 **Sliding Window + Frequency Array + Max Frequency Tracking**
> - Use two pointers (left `l`, right `r`) to form a window.
> - Count character frequencies using a fixed array `a[26]` for uppercase letters.
> - Maintain the frequency `f` of the most occurring character in the current window.
> - Adjust the window if changing all non-`f` chars exceeds `k`.

---

## 🧪 Test Cases

```

Input: s = "ABAB", k = 2 Output: 4

Input: s = "AABABBA", k = 1 Output: 4

````

---

## ✍️ My Explanation / Approach

> 📌 We maintain a sliding window and count character frequencies in that window.
>
> 🪛 At each right index `r`, we update:
> - Frequency of `s[r]` in the frequency array.
> - The max frequency `f` seen so far.
>
> 🧮 If the current window size minus `f` exceeds `k`, then we shrink the window from the left.
> - This ensures we don't make more than `k` replacements.
>
> ✅ We update the result `len` whenever we have a valid window.

---

## 🧑‍💻 Final Code

```java
class Solution {
    public int characterReplacement(String s, int k) {
        int len = 0;
        char[] arr = s.toCharArray();
        int n = s.length();
        int r = 0, l = 0;
        int f = 0;
        int[] a = new int[26];

        while (r < n) {
            a[arr[r] - 'A']++;
            f = Math.max(f, a[arr[r] - 'A']);

            if ((r - l + 1) - f <= k) {
                len = Math.max(len, r - l + 1);
            }

            if ((r - l + 1) - f > k) {
                a[arr[l++] - 'A']--;
            }

            r++;
        }

        return len;
    }
}
````

---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n)`
    
    - Each character is processed at most twice (once by `r`, once by `l`)
        
- **Space Complexity:** `O(1)`
    
    - Fixed array of size 26 for uppercase English letters
        

---
## 🗒️ Notes / Mistakes / To Revisit?

> 🔄 **Pointers and Frequencies**
> - Adjusting pointers and updating frequencies ensures efficiency and correctness in processing data segments.
> - Trimming invalid segments and maintaining max frequency helps in identifying valid segments accurately.

> 💡 **Max Frequency Insight**
> - Maintaining the max frequency is key; reducing it hurts results.
> - As long as the required changes are ≤ k, the substring is valid.
> - Increasing frequency is more helpful than reducing it.
> - ✅ Stable max frequency enhances the chance of longer substrings.
> - ✅ Sliding window ensures optimal segment evaluation without rescanning.

> 🔁 **Don't shrink unnecessarily**
> - ❗️We often think of using a `while` loop to shrink the window until it's valid again, but that's unnecessary here.
> - The answer is the *maximum* valid length, so shrinking aggressively would reduce that length.
> - 🧠 Instead, if adding a new character makes the window invalid, we just remove the first character and update the frequency map accordingly.
> - This maintains a valid window without overshrinking and preserves the longest possible valid substring.

> 🔁 Mark for revision? 
> - [   ] Yes 
> - [ x ] No

---
