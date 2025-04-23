# ✅ LeetCode 72 - Edit Distance

**Link**: [https://leetcode.com/problems/edit-distance](https://leetcode.com/problems/edit-distance)  
**Date**: 2025-04-23  
**Tags**: `Dynamic Programming`, `Recursion`, `Memoization`, `String`  
**Difficulty**: Hard

---

## 📘 Problem Summary

Given two strings `word1` and `word2`, return the **minimum number of operations** required to convert `word1` to `word2`.

Allowed operations:
- Insert a character
- Delete a character
- Replace a character

---

## ✅ Recursive + Memoization Approach

### 🔸 Idea

Use recursion with memoization to explore all paths of converting `word1` to `word2` by applying **insert, delete, or replace** operations as needed.

### 🔢 Code

```java
class Solution {

    public int func(int i, int j, String w1, String w2, int[][] dp) {
        if (i < 0) return j + 1;       // Need to insert remaining j+1 characters
        if (j < 0) return i + 1;       // Need to delete remaining i+1 characters

        if (dp[i][j] != -1) return dp[i][j];

        if (w1.charAt(i) == w2.charAt(j)) {
            return dp[i][j] = func(i - 1, j - 1, w1, w2, dp);
        }

        int insert = func(i, j - 1, w1, w2, dp);     // Insert w2[j] in w1
        int delete = func(i - 1, j, w1, w2, dp);     // Delete w1[i]
        int replace = func(i - 1, j - 1, w1, w2, dp); // Replace w1[i] with w2[j]

        return dp[i][j] = 1 + Math.min(insert, Math.min(replace, delete));
    }

    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word1.length()][word2.length()];
        for (int i = 0; i < word1.length(); i++) {
            Arrays.fill(dp[i], -1);
        }
        return func(word1.length() - 1, word2.length() - 1, word1, word2, dp);
    }
}
````

---

## 🧠 Intuition

We're comparing both strings from the end:

- If characters match, no operation needed—move both pointers left.
    
- If not, we try all three operations and pick the one with **minimum cost**:
    
    - **Insert**: Try to match by inserting a character to `word1` (i stays, j--).
        
    - **Delete**: Remove current char from `word1` (i--, j stays).
        
    - **Replace**: Replace current char in `word1` to match `word2[j]` (i--, j--).
        

---

## ⚙️ Explanation of Operations

|Operation|Meaning|Pointer Movement|
|---|---|---|
|**Insert**|Insert `w2[j]` into `w1`, then check next in `w2`|`func(i, j-1)`|
|**Delete**|Delete `w1[i]` and try to match with same `w2[j]`|`func(i-1, j)`|
|**Replace**|Replace `w1[i]` with `w2[j]`, then move both|`func(i-1, j-1)`|

All these operations cost `+1`.

---

## ⏱️ Time & Space Complexity

|Metric|Complexity|
|---|---|
|Time|O(m × n)|
|Space|O(m × n)|

Where `m = word1.length()` and `n = word2.length()`

---

## 🧪 Example

```java
Input: word1 = "horse", word2 = "ros"

Operations:
"horse" → "rose"   (replace 'h' → 'r')
"rose" → "ros"     (delete 'e')

Output: 2
```

---

## 💡 Reflections

- Classic DP problem for understanding recursion + memoization + tabulation.
    
- Important base case: if any index goes negative, the cost is remaining length of the other string.

---
