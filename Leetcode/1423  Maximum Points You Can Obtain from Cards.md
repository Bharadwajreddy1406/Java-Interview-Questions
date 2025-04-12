
## LeetCode 1423: Maximum Points You Can Obtain from Cards

#### Problem Statement:

You are given an integer array `nums` representing the points on cards, and an integer `k`. You can take exactly `k` cards from either the **start** or the **end** of the array. Your goal is to maximize the sum of points obtained.

> we no need to get the sum from between the array, only from ends,
> This problem tells us how to solve when corners are involved in question

- [ ] Make sure you read the question properly
#### Example:

**Input:**

```
nums = [1,2,3,4,5,6,1], k = 3
```

**Output:**

```
12
```

**Explanation:** You can pick the first two cards (1,2) and the last one (9), or pick the last three cards (6,1,5), etc. The optimal score is `6 + 1 + 5 = 12`.

---

#### Intuition:

- Initially take the **first `k` cards from the left**. This gives you a baseline score.
    
- Now, simulate a **window shift** by removing cards from the **left side** and adding cards from the **right side**, one by one.
    
- At each step, update the **maximum score**.
    

---

#### Code:

```java
class Solution {
    public int maxScore(int[] nums, int k) {
        int ls = 0; // left sum
        int rs = 0; // right sum

        // Step 1: Start by taking the first k cards from the left
        for (int i = 0; i < k; i++) ls += nums[i];

        int max = ls; // Initialize max score
        int right = nums.length - 1;

        // Step 2: Try taking fewer from the left and more from the right
        for (int i = k - 1; i >= 0; i--) {
            ls -= nums[i];       // Remove one from the left
            rs += nums[right];   // Add one from the right
            right--;             // Move the right pointer
            max = Math.max(max, ls + rs);  // Update max score
        }

        return max;
    }
}
```

---

#### Explanation:

- You consider all combinations where you take `i` cards from the left and `k-i` cards from the right, for all `i` from `k` to `0`.
    
- This guarantees you check **all possible `k`-card splits** between the front and the back of the array.
    

---

#### Complexity Analysis:

- **Time Complexity**: `O(k)`
    
    - Only `k` iterations are done to compute the possible combinations.
        
- **Space Complexity**: `O(1)`
    
    - Only a few integer variables are used.
        

---
