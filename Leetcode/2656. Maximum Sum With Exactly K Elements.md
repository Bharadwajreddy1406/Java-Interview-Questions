# LeetCode 2656. Maximum Sum With Exactly K Elements

**Link:** [LeetCode 2656](https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/)

---

## 🧠 Problem Statement

You are given an integer array `nums` and an integer `k`. 

You need to **maximize the sum** by picking exactly `k` elements with the following rule:

- In each operation, choose the current **maximum** element from the array.
- Add it to your score.
- Then, insert `max + 1` back into the array.
- Repeat this process `k` times.

Return the maximum sum after `k` operations.

---

## 🧪 Example Test Case

### Input:
```

nums = [1,2,3,4,5], k = 3

```

### Output:
```

18

````

### Explanation:
Pick 5 → insert 6  
Pick 6 → insert 7  
Pick 7  
Sum = 5 + 6 + 7 = 18

---

## 🔍 Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
- `1 <= k <= 100`

---

## 🧠 Intuition

Instead of simulating the heap-like behavior or sorting the array each time:
- Just find the current **maximum element once**.
- Add the next `k` consecutive integers starting from it.
  - Mathematically: `max + (max+1) + (max+2) + ... + (max + k - 1)`
- This is an arithmetic progression.

---

## 🧰 Data Structures Used

- No additional data structure required
- Simple variables for tracking `max` and `sum`

---

## ✅ Code (Java)

```java
class Solution {
    public int maximizeSum(int[] nums, int k) {
        int max = Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++){
            max = Math.max(max,nums[i]);
        }
        // int sum =0;
        // for(int i=0;i<k;i++){
        //     sum+= (max + i);
        // }
        // or
        int sum = k * max + (k * (k - 1)) / 2;
        return sum;
    }
}
````

---

## 🧠 Your Note:

> Instead of sorting and picking the last element, finding the `max` manually reduced the complexity — better performance in LeetCode.

---

## 🧮 Time & Space Complexity

- **Time Complexity:** O(n + k)
    
    - O(n) to find max
        
    - O(k) to sum k terms
        
- **Space Complexity:** O(1)
    

---

## 📌 Mathematical Formula :

You can replace the `for` loop with a formula for better performance:

```java
// sum = k * max + (k * (k - 1)) / 2;
```
---
