## Problem: House Robber II

**Leetcode 213**

---
### Date

`2025-04-12`
### Tags

`Dynamic Programming`, `Memoization`, `Recursion`, `Array`, `Robbery Pattern`, `DP with boundaries`

---
### Intuition

- It's a circular version of House Robber I.
    
- We can't rob the first and last house together since they are adjacent in a circle.
    
- So we consider two ranges:
    
    - Rob from house 0 to n-2 (exclude last)
        
    - Rob from house 1 to n-1 (exclude first)
        
- The answer will be the maximum of both.
    

---
### Data Structures Used

- Array for storing house values.
    
- DP array for memoization.
    
---
### Test Cases

```
Input: [2,3,2] => Output: 3
Input: [1,2,3,1] => Output: 4
Input: [1,2,3] => Output: 3
Input: [1] => Output: 1
```

---
### Recursion Only Code

```java
class Solution {
    public int solve(int arr[], int index, int start) {
        if(index < start) return 0;
        if(index == start) return arr[start];

        int pick = arr[index] + solve(arr, index - 2, start);
        int notPick = solve(arr, index - 1, start);

        return Math.max(pick, notPick);
    }

    public int rob(int[] nums) {
        int n = nums.length;
        if(n == 1) return nums[0];

        int rob1 = solve(nums, n - 2, 0);
        int rob2 = solve(nums, n - 1, 1);

        return Math.max(rob1, rob2);
    }
}
```

---

### Memoized Code

```java
class Solution {
    public int solve(int arr[], int index, int[] dp, int start) {
        if(index < start) return 0;
        if(index == start) return arr[start];
        if(dp[index] != -1) return dp[index];

        int pick = arr[index] + solve(arr, index - 2, dp, start);
        int notPick = solve(arr, index - 1, dp, start);

        return dp[index] = Math.max(pick, notPick);
    }

    public int rob(int[] nums) {
        int n = nums.length;
        if(n == 1) return nums[0];

        int[] dp1 = new int[n];
        Arrays.fill(dp1, -1);
        int rob1 = solve(nums, n - 2, dp1, 0);

        int[] dp2 = new int[n];
        Arrays.fill(dp2, -1);
        int rob2 = solve(nums, n - 1, dp2, 1);

        return Math.max(rob1, rob2);
    }
}
```

---

### Time & Space Complexity

**Time Complexity**: O(n) per call with memoization.  
**Space Complexity**: O(n) for memoization array.

---

### Reflection

- The recursion range needs to be carefully managed due to circular adjacency.
    
- Memoization improves efficiency drastically.
    
- Very similar to House Robber I, but with two split paths to simulate circle.
    
- Recursion with boundaries is a powerful technique here.