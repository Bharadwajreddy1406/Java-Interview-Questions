## 🧠 Problem: Unique Paths II

**Leetcode**: 63  
**Date**: 2025-04-12  
**Tags**: DP, Grid, Obstacles, Memoization

---

### ❓ Intuition

We're given an `m x n` grid, but **some cells contain obstacles** marked as `1`. We can only move **right** or **down**, and we must count the number of **unique paths from top-left to bottom-right**, avoiding obstacles.

This is an extension of Leetcode 62, with an extra check:  
**"Can we even go through this cell?"**

---

### 💡 Approach: Top-Down DP with Memoization

We use a recursive `solve(m, n)` function with memoization.

- If the current cell has an obstacle, we cannot move through it — return 0.
- Base cases:
  - Out of bounds → return 0.
  - At `(0,0)` → return 1 (start point).
- Recursively go **left** and **top**, if current cell is not blocked.

---

### ✅ Code (Java)

```java
class Solution {

    public int solve(int [][] grid, int m, int n, int [][] dp){
        if (m < 0 || n < 0) return 0;
        if (grid[m][n] == 1) return 0; // obstacle
        if (m == 0 && n == 0) return 1;

        if (dp[m][n] != -1) return dp[m][n];

        int left = solve(grid, m, n - 1, dp);
        int top = solve(grid, m - 1, n, dp);

        return dp[m][n] = left + top;
    }

    public int uniquePathsWithObstacles(int[][] grid) {
        if (grid[0][0] == 1) return 0;

        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(dp[i], -1);
        }

        return solve(grid, m - 1, n - 1, dp);
    }
}
````

---

### 🧩 Test Case

**Input:**

```
grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
```

**Output:**  
`2` unique paths

---

### ⏱️ Complexity

- **Time**: `O(m * n)` — each cell visited once.
    
- **Space**: `O(m * n)` — for memoization table.
    

---

### 🧠 Reflections

- Classic extension of Leetcode 62.
    
- Only additional condition: handle `grid[i][j] == 1` carefully.
    
- Can also be solved bottom-up for constant space.
    

---
