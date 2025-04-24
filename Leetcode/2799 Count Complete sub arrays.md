# Leetcode 2799 - Count Complete Subarrays 🔢

## 🗓️ Date
2025-04-24

## 🏷️ Tags
`Array` `Sliding Window` `HashMap`

---

## 💡 Problem

Given an integer array `nums`, we need to find the total number of **complete subarrays** in the array.

A subarray is called **complete** if it contains all the distinct elements of `nums`.

---

## 🧪 Example

### Input:
```txt
nums = [1, 3, 1, 2, 2, 1, 3]
````

### Output:

```txt
11
```

### Explanation:

The complete subarrays are:

- [1, 3, 1, 2, 2, 1]
    
- [1, 3, 1, 2, 2, 1, 3]
    
- [3, 1, 2, 2, 1]
    
- [3, 1, 2, 2, 1, 3]
    
- [1, 3, 1, 2, 2]
    
- [1, 3, 1, 2, 2, 1]
    
- [1, 3, 1]
    
- [3, 1, 2, 2]
    
- [1, 3, 1, 2]
    
- [3, 1, 2]
    
- [2, 2, 1]
    

---

## ⚙️ Logic

I did that approach where:

- We track **distinct elements** in the array with a `HashSet` and calculate its size (`n`).
    
- We use the sliding window technique (using `left` and `right` pointers) along with a `HashMap` to track the count of elements in the current window.
    
- If the size of the map equals `n` (i.e., all distinct elements are in the window), we know that we've found a **complete subarray**.
    
- Instead of counting the complete subarray directly, we add **`nums.length - right`** to `count`, because we know that any subarray starting from `left` and ending anywhere after `right` is a valid complete subarray. So it's all the way to the end of the array.
    
- Then, we slide the `left` pointer to reduce the size of the window until the map size is less than `n` again.
    

The key part that I learned here is when we find a complete subarray, we can consider **all** subarrays starting from `left` and ending at any index after `right` (i.e., to the end of the array). Hence, instead of just adding `count++`, we add `nums.length - right`.

---

## 🧾 Approach

1. **Use a HashSet** to find out the distinct elements in the array.
    
2. Use **two pointers (`left`, `right`)** to maintain a sliding window.
    
3. When the window contains all distinct elements, add the number of valid subarrays that can end at `right` (which is `nums.length - right`).
    
4. Slide the left pointer and continue until you’ve processed the entire array.
    

---

## 🧑‍💻 Code

```java
class Solution {
    public int countCompleteSubarrays(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int i : nums) set.add(i);
        int n = set.size();
        int count = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        int left = 0;
        int right = 0;
        while (right < nums.length) {
            map.put(nums[right], map.getOrDefault(nums[right], 0) + 1);
            while (map.size() == n) {
                count += (nums.length - right);
                map.put(nums[left], map.get(nums[left]) - 1);
                if (map.get(nums[left]) == 0) {
                    map.remove(nums[left]);
                }
                left++;
            }
            right++;
        }
        return count;
    }
}
```

---

## ⏱️ Complexity

- **Time:** O(n)
    
- **Space:** O(n)
    

---

## 🧠 Reflections

I did that tricky part where we don’t just count one complete subarray, but instead add all the subarrays from `left` to the end of the array. It’s really about the **sliding window** and when the map size equals `n`, you can quickly calculate how many valid subarrays exist from `left` to `right`.

I feel like this is one of those problems where a simple observation — that the right pointer marks the end of many valid subarrays — allows us to **efficiently calculate** the result without double-counting or missing anything.```

---

