# LeetCode 2302. Count Subarrays With Score Less Than K

**Link:** [LeetCode 2302](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/)

---

## Problem Statement

The **score** of a subarray `(i, j)` is defined as:  
```

score = sum(nums[i..j]) * (j - i + 1)

```

Given an integer array `nums` and an integer `k`, return the number of subarrays where the score is **strictly less than** `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

---

## Example Test Cases

**Example 1:**
```

Input: nums = [2,1,4,3,5], k = 10 Output: 6 Explanation: The valid subarrays are:

- [2]
    
- [1]
    
- [4]
    
- [3]
    
- [5]
    
- [2,1]
    

```

**Example 2:**
```

Input: nums = [1,1,1], k = 5 Output: 6 Explanation: All subarrays have score less than 5.

````

---

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= 10^15`

---

## Intuition

- The score is based on the sum of elements and the size of the subarray.
- We use a sliding window from `j` to `i`, expanding `i` forward.
- If the score becomes invalid (i.e., `sum * windowSize >= k`), we shrink the window from the left by increasing `j`.

---

## Sliding Window Update Logic Explained

At every step:
- Expand the right end of the window: `sum += nums[i]`
- **Check if current window is valid**:  
  While `sum * (i - j + 1) >= k`, shrink from the left:
  - Subtract `nums[j]` from the sum
  - Move `j` forward (shrink the window)

Once valid, the number of subarrays ending at `i` is `(i - j + 1)`.  
We add this count to the total.

This logic ensures:
- Each subarray counted has a score less than `k`
- The window is always minimal and valid

---

## Data Structures Used

- Two pointers: `i` and `j` for the sliding window
- Running sum (`long`) for performance on large inputs

---

## Code

```java
class Solution {
    public long countSubarrays(int[] nums, long k) {
        long sum = 0;
        long count = 0;
        int i = 0;
        int j = 0;

        while (i < nums.length) {
            sum += nums[i];

            while (sum * (i - j + 1) >= k) {
                sum -= nums[j];
                j++;
            }

            count += i - j + 1;
            i++;
        }

        return count;
    }
}
````

---

## Time Complexity

- **O(n)**  
    Each element is added and removed from the window at most once.
    

## Space Complexity

- **O(1)**  
    Only constant extra space is used (pointers and a few variables).
    

---

```

---

Let me know if you want the explanations to be even more concise or tailored for faster review (e.g., interview revision). Ready for the next one?
```