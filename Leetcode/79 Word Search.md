# Leetcode 79 - Word Search 🧩

## 🗓️ Date
2025-04-24

## 🏷️ Tags
`Backtracking` `DFS` `Matrix` `Recursion`

---

## 💡 Problem
Given a 2D board of characters and a word, return `true` if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically neighboring).  
Same letter cell may not be used more than once.

---

## 🧪 Test Case Example

### Input:
```txt
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
````

### Output:

```txt
true
```

---

## 🧰 Data Structures Used

- 2D Array
    
- DFS Recursion
    
- Backtracking using character replacement and restoration
    

---

## 🧠 My Notes

This problem was all about recursion and careful ordering of base conditions.  
I initially wrote the `pointer == length - 1` condition **above** the character check.  
Because of that, the code was not checking the last character at all and was **returning true too early**.

What I learned is that:

- **The order of base conditions matters.**
    
- You need to first check if the current character matches the word, and **then** check if it’s the last one.
    
- If you reverse that, the recursion short-circuits before validating the last character.
    

I fixed this by putting the character match before the pointer length check.  
That way, it only returns `true` if the last character actually matches and it's the final pointer.

---

## 🧾 Approach

- Start DFS from each cell of the board.
    
- If the current cell matches `word.charAt(0)`, recursively check 4 directions.
    
- Use backtracking: mark the current cell as visited (with `'#'`), and restore it after recursive calls.
    
- Return true if the full word is matched.
    

---

## 🧑‍💻 Code

```java
class Solution {

    int [][] directions = {{-1,0},{0,-1},{1,0},{0,1}}; // up, left, down, right

    public boolean dfs(int i, int j, char[][] board, String word, int pointer){
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length) return false;
        if (board[i][j] == '#') return false;
        if (board[i][j] != word.charAt(pointer)) return false;
        if (pointer == word.length() - 1) return true;

        char temp = board[i][j];
        board[i][j] = '#'; // mark as visited

        for (int[] dir : directions) {
            int r = i + dir[0];
            int c = j + dir[1];
            if (dfs(r, c, board, word, pointer + 1)) {
                return true;
            }
        }

        board[i][j] = temp; // backtrack
        return false;
    }

    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(i, j, board, word, 0)) return true;
            }
        }
        return false;
    }
}
```

---

## ⏱️ Complexity

- **Time:** O(m * n * 4^L), where L = word length
    
- **Space:** O(L) — recursion stack
    

---

## 🧠 Reflections

I did that one mistake that cost me some time — I put the base condition for `pointer == length - 1` before checking the actual character match.  
So the DFS was returning true even when the last character didn’t match.  
Once I fixed the **order of conditions**, everything worked perfectly.

This was a great reminder that writing base conditions properly is just as important as the recursion logic itself.

---
