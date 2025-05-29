# 🧾 Leetcode 583: Delete Operation for Two Strings

---

### ✅ Problem Summary:

Given two strings `word1` and `word2`, return the **minimum number of steps required to make the two strings equal**.  
In each step, you can **delete exactly one character** from either string.

---

### 💡 Key Insight:

This is a variation of the **Longest Common Subsequence (LCS)** problem:

- We aim to **minimize deletions**.
    
- If we **find the LCS**, we can keep those characters and **delete the rest**.
    
- Formula:
    
    ```
    minDistance = (len(word1) - LCS) + (len(word2) - LCS)
                = len(word1) + len(word2) - 2 * LCS
    ```
    

However, your approach solves it **directly with recursion and memoization**, without explicitly computing LCS.

---

### 🧠 Approach: Recursive + Memoization

Define a recursive function `solve(i, j)` that returns the **minimum number of deletions** required to make `word1[i:]` and `word2[j:]` equal.

---

### 🔁 Recursive Steps:

- **Base Cases**:
    
    - If `i` reaches end of `word1`, we need to delete all remaining characters from `word2`: `word2.length() - j`
        
    - If `j` reaches end of `word2`, we need to delete all remaining characters from `word1`: `word1.length() - i`
        
- **Memoization**:
    
    - Use `dp[i][j]` to store the result of subproblem `(i, j)`
        
- **Match Case**:
    
    - If `word1[i] == word2[j]`, move both pointers without any deletion
        
- **Mismatch Case**:
    
    - Try deleting either from `word1` or from `word2`
        
    - Return the **minimum** of the two possibilities + 1 deletion
        

---

### ⏱️ Time Complexity:

- `O(m * n)` where `m = word1.length()`, `n = word2.length()`  
    (Each `(i, j)` pair is computed once)
    

### 📦 Space Complexity:

- `O(m * n)` for the memoization table
    

---

### 📄 Java Code:

```java
class Solution {

    public int solve(String w1, String w2, int i, int j, int[][] dp) {
        if (i == w1.length()) return w2.length() - j;  // delete all from w2
        if (j == w2.length()) return w1.length() - i;  // delete all from w1

        if (dp[i][j] != -1) return dp[i][j];

        if (w1.charAt(i) == w2.charAt(j)) {
            return dp[i][j] = solve(w1, w2, i + 1, j + 1, dp);
        }

        int deleteFromW1 = 1 + solve(w1, w2, i + 1, j, dp);
        int deleteFromW2 = 1 + solve(w1, w2, i, j + 1, dp);

        return dp[i][j] = Math.min(deleteFromW1, deleteFromW2);
    }

    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word1.length()][word2.length()];
        for (int[] row : dp) Arrays.fill(row, -1);
        return solve(word1, word2, 0, 0, dp);
    }
}
```

---
