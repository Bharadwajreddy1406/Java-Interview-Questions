
# 🧠 Number of Enclosed Empty Spaces

`#bfs` `#2dgrid` `#floodfill` `#java` `#matrix-traversal`

#### 📌 Problem Statement

Pranav has a puzzle board filled with square boxes in the form of a grid.  
Some cells in the grid may be empty. `'0'` indicates an empty cell, `'1'` indicates a box.

Pranav wants to find out the number of empty spaces which are **completely surrounded** by the square boxes (from all four directions: left, right, top, bottom).

You are given the board in the form of a grid `M x N`, filled with 0's and 1's.  
Your task is to help Pranav to find the number of **empty groups surrounded by boxes** in the puzzle board.

**Input Format:**

```
Line-1: Two integers M and N, the number of rows and columns in the board.  
Next M lines: N space-separated integers (either 0 or 1).
```

#### 🧪 Test Cases

```
Input:
5 5  
1 1 1 1 1  
1 0 0 0 1  
1 0 1 0 1  
1 0 0 0 1  
1 1 1 1 1

Output:
1
```

```
Input:
5 6  
1 1 1 1 1 1  
1 0 1 0 0 1  
1 0 1 0 1 1  
1 0 0 0 0 1  
1 1 1 1 1 1

Output:
2
```

#### ✅ Code

```java
import java.util.*;

class Solution {
    static boolean isSafe(int[][] grid, int r, int c) {
        return (r >= 0 && c >= 0 && r < grid.length && c < grid[0].length);
    }

    static void bfs(int[][] grid, int i, int j) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{i, j});
        grid[i][j] = -1;
        int[][] directions = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        while (!q.isEmpty()) {
            int[] p = q.poll();
            for (int[] d : directions) {
                int row = d[0] + p[0];
                int col = d[1] + p[1];
                if (isSafe(grid, row, col) && grid[row][col] == 0) {
                    q.offer(new int[]{row, col});
                    grid[row][col] = -1;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) grid[i][j] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 0) {
                    if (i == 0 || j == 0 || i == n - 1 || j == m - 1) {
                        bfs(grid, i, j);
                    }
                }
            }
        }

        int c = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 0) {
                    bfs(grid, i, j);
                    c++;
                }
            }
        }

        System.out.println(c);
    }
}
```

#### 📊 Complexity

- Time Complexity: `O(M * N)`
    
- Space Complexity: `O(M * N)` (due to BFS queue and visited marking)
    

---
