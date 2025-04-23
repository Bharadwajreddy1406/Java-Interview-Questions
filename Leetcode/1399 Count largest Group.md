# ✅ LeetCode 1399 - Count Largest Group

**Link**: [https://leetcode.com/problems/count-largest-group](https://leetcode.com/problems/count-largest-group)  
**Date**: 2025-04-23  
**Tags**: `HashMap`, `Math`, `Counting`, `Optimization`  
**Difficulty**: Easy

---

## 📘 Problem Summary

Given an integer `n`, group the numbers from `1` to `n` based on the **sum of their digits**.

Return the **number of groups** that have the **largest size**.

---

## ✅ Brute Force Approach using HashMap

### 🔸 Idea

- Use a `HashMap<Integer, Integer>` to count the frequency of each digit sum.
- Track the maximum group size as we iterate.
- At the end, count how many groups had this maximum size.

### 🔢 Code

```java
class Solution {

    public int getSum(int n) {
        int val = 0;
        while (n > 0) {
            val += n % 10;
            n /= 10;
        }
        return val;
    }

    public int countLargestGroup(int n) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int maxSize = 0;

        for (int i = 1; i <= n; i++) {
            int sum = getSum(i);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
            maxSize = Math.max(maxSize, map.get(sum));
        }

        int count = 0;
        for (int size : map.values()) {
            if (size == maxSize) count++;
        }

        return count;
    }
}
````

---

## ✅ Optimized Version using Array

### 🔸 Optimization

- We know the **maximum digit sum** possible is `9 × 4 = 36` (since n ≤ 10,000).
    
- So, instead of using a `HashMap`, use a fixed-size array of length 37.
    
- This reduces memory overhead and improves performance.
    

### 🔢 Code

```java
class Solution {

    public int getSum(int n) {
        int val = 0;
        while (n > 0) {
            val += n % 10;
            n /= 10;
        }
        return val;
    }

    public int countLargestGroup(int n) {
        int[] arr = new int[37]; // digit sums can range from 1 to 36
        // coz 9999 is the biggest according to constraint given on n
        int maxSize = 0;

        for (int i = 1; i <= n; i++) {
            int sum = getSum(i);
            arr[sum]++;
            maxSize = Math.max(maxSize, arr[sum]);
        }

        int count = 0;
        for (int size : arr) {
            if (size == maxSize) count++;
        }

        return count;
    }
}
```

---

## 🧠 Intuition

- We bucket numbers based on their digit sum.
    
- The largest groups are those with the highest frequency of such sums.
    
- We simply count how many such groups exist.
    

---

## ⏱️ Time & Space Complexity

|Approach|Time Complexity|Space Complexity|
|---|---|---|
|HashMap|O(N × D)|O(N)|
|Array|O(N × D)|O(1) (fixed 37)|

Where `D` is the number of digits in `i` (at most `log₁₀(N)`).

---

## 🧪 Example

```java
Input: n = 13

Digit Sums:
1 → 1
2 → 2
...
10 → 1
11 → 2
12 → 3
13 → 4

Groups:
1 → {1,10}  
2 → {2,11}  
3 → {3,12}  
4 → {4,13}  
...

Max group size: 2  
Output: 4
```

---

## 💡 Reflections

- Simple problem but good use-case for **bucket counting**.
    
- Optimization from `HashMap` to array helps in competitive coding scenarios.
    
---
