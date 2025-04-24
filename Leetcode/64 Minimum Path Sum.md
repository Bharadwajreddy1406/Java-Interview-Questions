# **Leetcode 64** 
### ✅ Problem Summary

You are given an `m x n` grid filled with **non-negative numbers**, and you need to find a path from the **top-left** to the **bottom-right**, such that the sum of all numbers along the path is **minimized**.  
You can **only move down or right** at any point in time.

---

### 🔍 Intuition Behind the Approach

This is a **classic DP on grid** problem. At each cell `(m, n)`, you have two choices:

- Come from the top: `(m-1, n)`
    
- Come from the left: `(m, n-1)`
    

So the minimum cost to reach `(m, n)` is the cost at `(m, n)` **plus** the **minimum** of the costs to reach the top or left cells.

---

### 👨‍💻 Code Explanation

```java
class Solution {
    public int func(int m, int n , int [][] grid, int[][] dp){
        if (m < 0 || n < 0) return Integer.MAX_VALUE; // out of bounds
        if (m == 0 && n == 0) return grid[0][0]; // base case

        if (dp[m][n] != -1) return dp[m][n]; // memoization

        // Take minimum of coming from top or left
        int top = func(m-1, n, grid, dp);
        int left = func(m, n-1, grid, dp);

        // Store the result
        return dp[m][n] = grid[m][n] + Math.min(top, left);
    }

    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int [][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(dp[i], -1); // initialize dp
        }
        return func(m - 1, n - 1, grid, dp); // start from bottom-right
    }
}
```

---

### 🧠 Notes

- The **base case** is `(0, 0)` because that’s where the path starts.
    
- The function recursively computes the minimum path to any cell `(m, n)` by only considering paths from the **top** and **left**, because only right and down moves are allowed.
    
- If we ever go **outside** the grid (`m < 0` or `n < 0`), we return `Integer.MAX_VALUE` so it doesn't affect the minimum logic.
    

---

### 🧪 Example

**Input**:

```java
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```

**Valid paths**:

- `1 → 3 → 1 → 1 → 1 = 7`
    
- `1 → 1 → 4 → 2 → 1 = 9`
    

**Output**: `7`

---

### ⏱️ Time & Space Complexity

- **Time Complexity**: `O(m * n)` due to memoization avoiding recomputation.
    
- **Space Complexity**: `O(m * n)` for the DP table + recursion stack space.
    

---

Let me know if you want the **tabulation version** (bottom-up DP) too!