

## **N-Queens II**

###### 📌 Link:

[LeetCode - N-Queens II](https://leetcode.com/problems/n-queens-ii/)

---
### 📄 Problem Description:

The problem asks you to find all distinct solutions to the N-Queens puzzle where you place `N` queens on an `N x N` chessboard so that no two queens threaten each other. Specifically, this problem requires you to return the number of distinct solutions, rather than listing them.

---

### 🧪 Test Cases:

```
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-Queens puzzle.

Input: n = 1
Output: 1
Explanation: There is one solution to the 1-Queens puzzle.
```

---

### 📋 Constraints:

- `1 <= n <= 9`
    

---

### 💡 Intuition / Approach:

The problem uses **Backtracking** to place queens one by one on the board, row by row, and checks for valid placements by ensuring that no two queens threaten each other.

The idea is to iterate over each row, and for each row, try placing a queen in every column. After placing a queen, we recursively try to place queens in subsequent rows. If a solution is found (i.e., we successfully place queens in all rows), we increment the count.

Key points:

1. **Can place a queen?** The conditions for a valid position are:
    
    - No queen in the same column.
        
    - No queen in the same diagonal (both left and right).
        
2. **Backtrack** when placing queens: If placing a queen in a particular column doesn’t lead to a valid solution, we backtrack by removing the queen and trying the next column.
    

---

### 💻 Code (Your Solution):

```java
class Solution {
    public void backtrack(char[][] board , int row, int n, int[] ans){
        if(row == n){
            ans[0]++;
            return;
        }

        for(int col = 0; col < n; col++){
            if(canPlace(board, row, col, n)){
                board[row][col] = 'Q';
                backtrack(board, row + 1, n, ans);
                board[row][col] = '.'; // Backtrack
            }
        }
    }

    public boolean canPlace(char[][] board, int row, int col, int n){
        // Check column
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') return false;
        }

        // Check left diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') return false;
        }

        // Check right diagonal
        for (int i = row, j = col; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') return false;
        }

        return true;
    }

    public int totalNQueens(int n) {
        char[][] board = new char[n][n];
        for(char[] row : board) {
            Arrays.fill(row, '.'); // Initialize the board with '.' 
        }

        int[] ans = new int[]{0}; // To store the count of solutions
        backtrack(board, 0, n, ans);
        return ans[0];
    }
}
```

---

### 🧰 New Data Structures / Concepts Used:

**Backtracking:**

- **Backtracking** is a technique for solving problems incrementally, trying partial solutions and discarding those that fail to meet the constraints. In this problem, it is used to place queens one row at a time and backtrack when an invalid position is reached.
    

**Can-Place Logic:**

- The `canPlace` function checks whether placing a queen at a particular position is valid. It ensures that the column, the left diagonal, and the right diagonal are free of other queens.
    
---
