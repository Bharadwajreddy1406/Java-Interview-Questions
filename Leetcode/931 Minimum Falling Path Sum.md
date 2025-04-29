# LeetCode 931. Minimum Falling Path Sum

**Link:** [LeetCode 931](https://leetcode.com/problems/minimum-falling-path-sum/)

---

## Problem Statement

Given an `n x n` integer matrix, return the **minimum sum** of any falling path through the matrix.

A **falling path** starts at any element in the first row and chooses one element from each row. The next row's element must be either directly below or diagonally left/right.

---

## Example Test Cases

**Example 1:**
```

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]] Output: 13 Explanation: Falling path = 1 → 4 → 8

```

**Example 2:**
```

Input: matrix = [[-19,57],[-40,-5]] Output: -59 Explanation: Falling path = -19 → -40

````

---

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 100`
- `-100 <= matrix[i][j] <= 100`

---

## Intuition

We want the **minimum path sum** from any column of the top row to any column of the bottom row, only moving vertically or diagonally.

- Start from row 0 and try all columns.
- At each cell `(i, j)`, you can go to `(i+1, j-1)`, `(i+1, j)`, or `(i+1, j+1)` if within bounds.
- Use:
  - **Recursion** for brute force.
  - **Memoization** to cache and avoid recomputation.
  - **Tabulation (Bottom-Up DP)** for optimal performance.

---

## Data Structures Used

- 2D array for memoization and tabulation.
- Simple recursion for brute-force approach.

---

## Approach 1: Recursion

```java
class Solution {
    public int func(int i, int j, int[][] matrix, int n) {
        if (j < 0 || j >= n) return Integer.MAX_VALUE;
        if (i == n - 1) return matrix[i][j];

        int minSum = Integer.MAX_VALUE;
        for (int col = j - 1; col <= j + 1; col++) {
            minSum = Math.min(minSum, func(i + 1, col, matrix, n));
        }

        return matrix[i][j] + minSum;
    }

    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int min = Integer.MAX_VALUE;

        for (int j = 0; j < n; j++) {
            min = Math.min(min, func(0, j, matrix, n)); 
        }

        return min;
    }
}
````

### TC: O(3^n) – Exponential

### SC: O(n) – Recursive stack depth

---

## Approach 2: Memoization (Top-Down DP)

```java
class Solution {
    public int func(int i, int j, int[][] matrix, int n, int[][] dp) {
        if (j < 0 || j >= n) return Integer.MAX_VALUE;
        if (i == n - 1) return matrix[i][j];
        if (dp[i][j] != -1) return dp[i][j];

        int minSum = Integer.MAX_VALUE;
        for (int col = j - 1; col <= j + 1; col++) {
            if (col >= 0 && col < n) {
                minSum = Math.min(minSum, func(i + 1, col, matrix, n, dp));
            }
        }

        return dp[i][j] = matrix[i][j] + minSum;
    }

    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int min = Integer.MAX_VALUE;
        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], -1);
        }

        for (int j = 0; j < n; j++) {
            min = Math.min(min, func(0, j, matrix, n, dp)); 
        }

        return min;
    }
}
```

### TC: O(n^2) – Every cell computed once

### SC: O(n^2) – For memoization table + recursion stack

---

## Approach 3: Tabulation (Bottom-Up DP)

```java
class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int[][] dp = new int[n][n];

        for (int j = 0; j < n; j++) {
            dp[n - 1][j] = matrix[n - 1][j]; // Base case
        }

        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < n; j++) {
                int down = dp[i + 1][j];
                int leftDiag = (j > 0) ? dp[i + 1][j - 1] : Integer.MAX_VALUE;
                int rightDiag = (j < n - 1) ? dp[i + 1][j + 1] : Integer.MAX_VALUE;

                dp[i][j] = matrix[i][j] + Math.min(down, Math.min(leftDiag, rightDiag));
            }
        }

        int min = Integer.MAX_VALUE;
        for (int j = 0; j < n; j++) {
            min = Math.min(min, dp[0][j]);
        }

        return min;
    }
}
```

### TC: O(n^2)

### SC: O(n^2) – For DP table

---
