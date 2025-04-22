## 🧗‍♂️ Problem: 746. Min Cost Climbing Stairs

### 🔗 Link
[Leetcode 746](https://leetcode.com/problems/min-cost-climbing-stairs/)

---

### 🧠 Intuition
You can start at index `0` or `1`. At each step, you can move 1 or 2 steps forward. The goal is to reach the **top** (i.e., beyond the last index), with the **minimum total cost** paid at the steps you land on.

---

### 🔄 Approach 1: Top-down (Recursion + Memoization)

We define a function `solve(index)` that returns the **minimum cost to reach `index`**. From each index, you can come from `index - 1` or `index - 2`.

#### ✅ Code
```java
class Solution {
    public int solve(int arr[], int index, int [] dp){
        if(index < 0){
            return 0;
        }
        if(dp[index] != -1){
            return dp[index];
        }
        if(index == 0 || index == 1){
            return arr[index];
        }
        int pick = arr[index] + solve(arr, index - 1, dp);
        int pick2 = arr[index] + solve(arr, index - 2, dp);

        return dp[index] = Math.min(pick, pick2);
    }

    public int minCostClimbingStairs(int[] cost) {
        int dp[] = new int[cost.length];
        Arrays.fill(dp, -1);
        return Math.min(
            solve(cost, cost.length - 1, dp),
            solve(cost, cost.length - 2, dp)
        );
    }
}
````

#### ⏱️ Time & Space Complexity

|Metric|Complexity|
|---|---|
|Time Complexity|O(n)|
|Space Complexity|O(n) (recursion + dp)|

---

### 🔄 Approach 2: Bottom-up DP

Instead of solving from the top, we compute the **min cost** to reach each index in order.

#### ✅ Code

```java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] dp = new int[n];

        dp[0] = cost[0];
        dp[1] = cost[1];

        for(int i = 2; i < n; i++){
            dp[i] = cost[i] + Math.min(dp[i-1], dp[i-2]);
        }

        return Math.min(dp[n-1], dp[n-2]);
    }
}
```

#### 🧠 Explanation:

- `dp[i]` = `cost[i]` + min cost to reach either `i-1` or `i-2`
    
- Return the min of last two since you can step off from either to the top.
    

#### ⏱️ Time & Space Complexity

|Metric|Complexity|
|---|---|
|Time Complexity|O(n)|
|Space Complexity|O(n)|

---

### 🔄 Approach 3: Bottom-up + Space Optimized (O(1) space)

Since at each step we only need the last two results, we can just track them using variables.

#### ✅ Code

```java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int prev2 = cost[0];
        int prev1 = cost[1];

        for(int i = 2; i < n; i++){
            int curr = cost[i] + Math.min(prev1, prev2);
            prev2 = prev1;
            prev1 = curr;
        }

        return Math.min(prev1, prev2);
    }
}
```

#### 🧠 Explanation:

- Reduces space usage by keeping only `prev1` and `prev2`.
    
- Same logic as above, just no array.
    

#### ⏱️ Time & Space Complexity

|Metric|Complexity|
|---|---|
|Time Complexity|O(n)|
|Space Complexity|O(1)|

---

### 🧪 Sample Test Case

**Input:**

```
cost = [10, 15, 20]
```

**Output:**

```
15
```

**Explanation:**

- Start at index 1 → 15
    
- Step off from there → total = 15
    

---

### 📌 Reflections

- Converting recursive solutions to iterative DP is a common and valuable optimization.
    
- Space optimization using two variables is efficient and ideal for interview settings.
    
- Always analyze if full `dp[]` is necessary—often we only need last few values.
    

---

### 📆 Date Solved

20-04-2025

