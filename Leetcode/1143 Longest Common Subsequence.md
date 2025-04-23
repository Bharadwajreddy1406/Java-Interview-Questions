# ✅ LeetCode 1143 - Longest Common Subsequence

**Link**: [https://leetcode.com/problems/longest-common-subsequence](https://leetcode.com/problems/longest-common-subsequence)  
**Date**: 2025-04-23  
**Tags**: `Dynamic Programming`, `Recursion`, `Memoization`, `String`, `LCS`  
**Difficulty**: Medium

---

## 📘 Problem Summary

Given two strings `text1` and `text2`, return the **length of their longest common subsequence**.

A **subsequence** is a sequence that appears in the same relative order but not necessarily contiguous.

---

## ✅ Recursive + Memoization Approach

### 🔸 Idea

Use recursion to compare characters from the end of both strings.  
- If characters match, add 1 and move both pointers.
- If they don't, try both possibilities: exclude from either string, and return the max.

### 🔢 Code

```java
class Solution {

    public int func(int i, int j, String word1, String word2, int[][] dp){
        if (i < 0 || j < 0) return 0;

        if (dp[i][j] != -1) return dp[i][j];

        if (word1.charAt(i) == word2.charAt(j)) {
            return dp[i][j] = 1 + func(i - 1, j - 1, word1, word2, dp);
        }

        int first = func(i - 1, j, word1, word2, dp);
        int second = func(i, j - 1, word1, word2, dp);

        return dp[i][j] = Math.max(first, second);
    }

    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp = new int[text1.length()][text2.length()];
        for (int i = 0; i < text1.length(); i++) {
            Arrays.fill(dp[i], -1);
        }
        return func(text1.length() - 1, text2.length() - 1, text1, text2, dp);
    }
}
````

---

## 🧠 Intuition

We traverse both strings from the end and:

- If characters match, we can include them in our LCS → `1 + func(i-1, j-1)`
    
- If not, explore both options: skip a char from either string → take the `max()`.
    

The memoization table avoids recomputation.

---

## 🧪 Example

```java
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: LCS = "ace"
```

---

## ⏱️ Time & Space Complexity

|Metric|Complexity|
|---|---|
|Time|O(m × n)|
|Space|O(m × n) (DP table)|

Where `m = text1.length()` and `n = text2.length()`

---

## 💡 Reflections

- Classic DP problem to understand string comparison via recursion and memoization.
    
- Can also be solved using **tabulation (bottom-up)** with a 2D matrix.
    
- Base case is `0` when either index goes below 0.
    
---
