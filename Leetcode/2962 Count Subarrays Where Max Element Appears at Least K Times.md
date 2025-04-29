# LeetCode 2962. Count Subarrays Where Max Element Appears at Least K Times

**Link:** [LeetCode 2962](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/)

---

## Problem Statement
You are given an integer array `nums` and a positive integer `k`.

Return the number of subarrays where the maximum element appears at least `k` times.

A **subarray** is a contiguous sequence of elements within an array.

---

## Example Test Cases

**Example 1:**
```

Input: nums = [1,3,2,3,3], k = 2 Output: 6 Explanation: The subarrays where 3 appears at least 2 times are:

- [1,3,2,3,3]
    
- [3,2,3,3]
    
- [1,3,2,3]
    
- [3,2,3]
    
- [2,3,3]
    
- [3,3]
    

```

**Example 2:**
```

Input: nums = [1,4,2,1], k = 1 Output: 4 Explanation: The subarrays where 4 appears at least 1 time are:

- [1,4]
    
- [1,4,2]
    
- [1,4,2,1]
    
- [4]
    

````

---

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`
- `1 <= k <= 10^5`

---

## Intuition
- First, find the maximum element in the array.
- Then, use a sliding window approach to find all subarrays where the maximum element appears at least `k` times.
- When the frequency of the maximum element inside the window becomes at least `k`, all subarrays extending to the right are valid.
- Carefully shrink the window from the left to avoid overcounting.

---

## Data Structures Used
- Two pointers (`l` and `r`) for the sliding window.
- Simple counters for frequency tracking.

---

## Code

```java
class Solution {
    public long countSubarrays(int[] nums, int k) {
        int max = Integer.MIN_VALUE;
        long count = 0;
        int n = nums.length;

        // Find the maximum element
        for (int i : nums) {
            max = Math.max(max, i);
        }

        int freq = 0;
        for (int l = 0, r = 0; r < n; r++) {
            if (nums[r] == max) {
                freq++;
            }

            // Shrink window from left until freq >= k
            while (l < n && freq >= k) {
                count += (n - r);
                if (nums[l] == max && freq > 0) {
                    freq--;
                }
                l++;
            }
        }
        return count;
    }
}
````

---

## Time Complexity

- **O(n)** —
    
    - One pass to find the maximum element.
        
    - Another pass with two pointers for the sliding window.
        

## Space Complexity

- **O(1)** —
    
    - Only a few variables are used; no extra space depending on `n`.
        

---
