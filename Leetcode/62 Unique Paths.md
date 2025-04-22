## 🧠 Problem: Unique Paths

**Leetcode**: 62  
**Date**: 2025-04-12  
**Tags**: DP, Grid, Memoization

---

### ❓ Intuition

We are asked to count how many unique paths exist from the **top-left** corner to the **bottom-right** corner of an `m x n` grid.  
The movement is **only allowed** in two directions: **right** and **down**.

This is a classic **dynamic programming** problem where each cell depends on the number of ways to reach it from the cell **above** and the cell **to the left**.

---

### 💡 Approach: Top-Down DP with Memoization

We define a recursive function `solve(m, n)` to return the number of paths from `(0,0)` to `(m,n)`.

- Base case:
  - If out of bounds → return 0.
  - If at `(0, 0)` → return 1 (only one path starts here).
- Memoize results to avoid recomputation.

---

### ✅ Code (Java)

```java
class Solution {

    public int solve(int m, int n, int dp[][]){
        if (m < 0 || n < 0) return 0;
        if (m == 0 && n == 0) return 1;

        if (dp[m][n] != -1) return dp[m][n];

        int top = solve(m - 1, n, dp);
        int left = solve(m, n - 1, dp);

        return dp[m][n] = left + top;
    }

    public int uniquePaths(int m, int n) {
        int [][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(dp[i], -1);
        }

        return solve(m - 1, n - 1, dp);
    }
}
````

---

### 🧩 Test Case

**Input:**

```
m = 3, n = 7
```

**Output:**  
`28` unique paths from `(0,0)` to `(2,6)`

---

### ⏱️ Complexity

- **Time**: `O(m * n)` — each subproblem solved once.
    
- **Space**: `O(m * n)` — for dp table.
    

---

### 🧠 Reflections

- Very similar to Fibonacci grid problems.
    
- You can solve it bottom-up with a 2D or even 1D DP array.
    
- Good warm-up for obstacle-based pathfinding problems like Leetcode 63.
    

---
