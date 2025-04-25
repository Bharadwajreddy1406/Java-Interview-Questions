# Leetcode 560 - Subarray Sum Equals K

## Question
Given an integer array `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

---

## Schema

### Input
- **nums**: An integer array where 1 ≤ nums.length ≤ 2 * 10^4, and -10^9 ≤ `nums[i]` ≤ 10^9.
- **k**: An integer, -10^9 ≤ k ≤ 10^9.

### Output
- An integer representing the number of subarrays whose sum equals `k`.

---

## Solution

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int sum = 0;
        int count = 0;
        map.put(0, 1); // To account for subarrays that start from the beginning
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];

            if (map.containsKey(sum - k)) {
                count += map.get(sum - k);
            }

            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }

        return count;
    }
}
````

### Explanation:

- **Prefix Sum:** We keep a running sum of the array elements as we iterate. For each element, we check if the difference between the running sum and `k` (i.e., `sum - k`) is already present in our map. This means we have found a subarray that sums to `k`.
    
- **HashMap:** The map stores how many times each prefix sum has occurred. If a specific sum minus `k` has appeared before, it means there exists a subarray (from that previous index to the current index) whose sum equals `k`.
    
- **Initial Map Setup:** We initialize the map with `{0: 1}` to handle the edge case where a subarray starting from the beginning sums to `k`.
    

---

## Example

### Input

```plaintext
nums = [1, 1, 1], k = 2
```

### Output

```plaintext
2
```

- Subarrays that sum to `2` are: `[1, 1]` (at indices `[0, 1])` and `[1, 1]` (at indices `[1, 2]`).
    

---

## Time & Space Complexity

- **Time Complexity:** O(n), where n is the length of the array `nums`. We only traverse the array once, and the operations on the `HashMap` are constant time on average.
    
- **Space Complexity:** O(n), for storing the prefix sums in the `HashMap`.
    

---

## Key Concepts

- **Prefix Sum:** Using prefix sums allows us to find the sum of any subarray in constant time.
    
- **HashMap for Subarray Sums:** By storing previously seen prefix sums, we efficiently calculate the number of subarrays with sum `k` without needing to check every possible subarray explicitly.
    

---

I thought about the problem in terms of building up a running sum as I iterate over the array. The key insight is recognizing that if I know the sum of a subarray up to index `i`, and I also know the sum of a subarray up to some earlier index `j`, I can compute the sum of the subarray between `j` and `i` efficiently. This leads to the use of the prefix sum technique combined with a `HashMap` to store the count of prefix sums, enabling a time-efficient solution.

---

## Helpful Resources

- [Prefix Sum and Explanation (YouTube)](https://www.youtube.com/watch?v=xvNwoz-ufXA) – This link was super helpful in understanding the prefix sum technique and how it applies to problems like this one.
    
---
