# 🧾 Leetcode 1035: Uncrossed Lines – Memoized DP

---

### ✅ Problem Summary:

You are given two integer arrays `nums1` and `nums2`. You want to draw the **maximum number of connecting lines** between the elements of the two arrays such that:

- Each line connects one element from `nums1` to one from `nums2`.
    
- The elements connected by lines must be **equal**.
    
- The lines must not **cross** (i.e., if `nums1[i]` connects to `nums2[j]`, no other line should cross it).
    

🟰 This is **equivalent to finding the Longest Common Subsequence (LCS)** between `nums1` and `nums2`.

---

### 💡 Intuition:

Use **recursion + memoization** to explore all ways of connecting elements without crossing.

---

### 🧠 Key Idea:

- If `nums1[i] == nums2[j]`, we can connect them and move both pointers.
    
- Else, try skipping one element in either array and take the maximum result.
    

---

### 🪜 Recursive Steps (`solve(i, j)`):

- **Base case**: if `i >= nums1.length || j >= nums2.length`, return 0.
    
- **Memoization**: Use `dp[i][j]` to store the result of subproblem `(i, j)`.
    
- **Match case**: If `nums1[i] == nums2[j]`, connect them → `1 + solve(i+1, j+1)`
    
- **No match**: Try skipping one from either `nums1` or `nums2`:
    
    ```java
    solve(i+1, j) OR solve(i, j+1)
    ```
    

---

### 🧠 DP Table:

- `dp[i][j]` = Max uncrossed lines for `nums1[i:]` and `nums2[j:]`
    

---

### ⏱️ Time Complexity:

- `O(m * n)` → Each state `(i, j)` is computed once  
    (where `m = nums1.length`, `n = nums2.length`)
    

### 📦 Space Complexity:

- `O(m * n)` for `dp` array
    
- `O(m + n)` recursion stack (can be avoided with bottom-up)
    

---

### 🔁 Example:

```text
nums1 = [1, 4, 2]
nums2 = [1, 2, 4]
```

- Match `1` at index 0 → match
    
- Try both ways for the rest:
    
    - `4` with `2` (no match)
        
    - `2` with `2` (match)
        
- Result: 2 connections → `1-1` and `2-2` or `1-1` and `4-4`
    

---

### 🧹 Clean Java Code:

```java
class Solution {
    public int solve(int[] nums1, int[] nums2, int i, int j, int[][] dp) {
        if (i >= nums1.length || j >= nums2.length) return 0;
        if (dp[i][j] != -1) return dp[i][j];

        if (nums1[i] == nums2[j]) {
            return dp[i][j] = 1 + solve(nums1, nums2, i + 1, j + 1, dp);
        }

        int op1 = solve(nums1, nums2, i + 1, j, dp);
        int op2 = solve(nums1, nums2, i, j + 1, dp);
        return dp[i][j] = Math.max(op1, op2);
    }

    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        int[][] dp = new int[m][n];
        for (int[] row : dp) Arrays.fill(row, -1);

        return solve(nums1, nums2, 0, 0, dp);
    }
}
```

---
