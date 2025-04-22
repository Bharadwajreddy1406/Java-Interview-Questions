## 🏠 Problem: 198. House Robber

### 🔗 Link
[Leetcode 198](https://leetcode.com/problems/house-robber/)

---

### 🧠 Intuition
You're given an array of integers where each value represents money at a house. You **cannot rob two adjacent houses**. Maximize the amount of money you can rob without triggering the alarm.

---

### 🔄 Approach 1: Recursion (Top-down)

Define `solve(index)` which returns the max money you can rob **up to** that house.

#### ✅ Code
```java
class Solution {
    public int solve(int arr[], int index){
        if(index < 0) return 0;
        if(index == 0) return arr[0];

        int first = arr[index] + solve(arr, index - 2); // pick this
        int second = solve(arr, index - 1);             // skip this

        return Math.max(first, second);
    }

    public int rob(int[] nums) {
        return Math.max(
            solve(nums, nums.length - 1),
            solve(nums, nums.length - 2)
        );
    }
}
````

#### ⚠️ Limitation:

- Exponential time due to repeated subproblems.
    

---

### 🔄 Approach 2: Memoization (Top-down + DP)

Use `dp[index]` to cache results.

#### ✅ Code

```java
class Solution {
    public int solve(int arr[], int index, int[] dp){
        if(index < 0) return 0;
        if(index == 0) return arr[0];
        if(dp[index] != -1) return dp[index];

        int first = arr[index] + solve(arr, index - 2, dp);
        int second = solve(arr, index - 1, dp);

        return dp[index] = Math.max(first, second);
    }

    public int rob(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, -1);
        return Math.max(
            solve(nums, nums.length - 1, dp),
            solve(nums, nums.length - 2, dp)
        );
    }
}
```

#### ⏱️ Time & Space Complexity

|Metric|Complexity|
|---|---|
|Time Complexity|O(n)|
|Space Complexity|O(n)|

---

### 🔄 Approach 3: Bottom-up DP

Build the `dp` array iteratively.

#### ✅ Code

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if(n == 0) return 0;
        if(n == 1) return nums[0];

        int[] dp = new int[n];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for(int i = 2; i < n; i++){
            dp[i] = Math.max(nums[i] + dp[i-2], dp[i-1]);
        }

        return dp[n-1];
    }
}
```

---

### 🔄 Approach 4: Space Optimized (O(1) Space)

Only last two results are needed at any time.

#### ✅ Code

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if(n == 0) return 0;
        if(n == 1) return nums[0];

        int prev2 = nums[0];
        int prev1 = Math.max(nums[0], nums[1]);

        for(int i = 2; i < n; i++){
            int curr = Math.max(nums[i] + prev2, prev1);
            prev2 = prev1;
            prev1 = curr;
        }

        return prev1;
    }
}
```

#### ⏱️ Time & Space Complexity

|Metric|Complexity|
|---|---|
|Time Complexity|O(n)|
|Space Complexity|O(1)|

---

### 🧪 Sample Test Case

**Input:**

```
nums = [2,7,9,3,1]
```

**Output:**

```
12
```

**Explanation:**

- Rob 2 + 9 + 1 = 12
    
- Can't rob adjacent (7 & 9 or 9 & 3)
    

---

### 📌 Reflections

- Don’t double count overlapping subproblems; memoization avoids that.
    
- Space-optimized version is ideal for interviews.
    
- Common pattern in dynamic programming: pick vs skip.
    

---

### 📆 Date Solved

20-04-2025
