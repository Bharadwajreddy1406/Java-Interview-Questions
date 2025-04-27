# Leetcode 3392 - Count Subarrays of Length Three With a Condition

## 🧩 Question

Given an array of integers `nums`, your task is to count how many subarrays of length `3` satisfy the following condition:

- The sum of the first and last element of the subarray must be twice the middle element.

Return the count of such subarrays.

---

## 📥 Example Input

**Input:**

```text
nums = [-1, -4, -1, 4]
````

**Output:**

```text
1
```

**Explanation:**

- The subarray `[ -1, -4, -1 ]` satisfies the condition because `(-1 + -1) = -4 * 2`.
    
- But `[ -4, -1, 4 ]` does not satisfy this condition because `(-4 + 4) != -1 * 2`.
    

---

## ✅ Solution

```java
class Solution {
    public int countSubarrays(int[] nums) {
        
        int count = 0;
        int sum = 0;
        
        for(int left = 0, right = 0; right < nums.length; right++) {
            sum += nums[right];

            if(right - left + 1 > 3) {
                sum -= nums[left];
                left++;
            }

            if(right - left + 1 == 3) {
                if(2 * (nums[left] + nums[right]) == nums[left + 1]) {
                    count++;
                }
            }
        }

        return count;
    }
}
```

---

## 🧠 Explanation

### Key Logic:

- The subarrays being considered must have **exactly 3 elements**.
    
- For every valid subarray (i.e., one with 3 elements), we check the condition:
    
    ```
    2 * (nums[left] + nums[right]) == nums[left + 1]
    ```
    
- **Two pointers** (`left` and `right`) are used to slide over the array and check each subarray of length 3.
    
- The `sum` is used to track the sum of elements between the `left` and `right` pointers, ensuring that when the window exceeds size 3, we adjust the pointers accordingly.
    

---

## 🧠 Why "Multiply Instead of Divide"?

### Messy Case:

For input `nums = [-1, -4, -1, 4]`, using the **division logic** (i.e., checking if `-4 + 4 == -1 / 2`), the result was incorrect.

- The first subarray `[-1, -4, -1]` satisfies the condition because `(-1 + -1) == -4 * 2`.
    
- The second subarray `[-4, -1, 4]` does **not** satisfy the condition because:
    
    - `(-4 + 4) == 0` which is not equal to `-1 / 2` (and shouldn't be).
        

Using the **multiplication** logic:

- Instead of dividing by 2, we multiply `nums[left] + nums[right]` by 2, which ensures that the condition checks are valid and prevents any cases like the one above.
    

Thus, replacing division with multiplication fixed the issue, because the division logic was incorrectly counting subarrays where the sum of the first and last elements didn't meet the condition.

---
## 🧠 Concepts Used

- **Sliding Window:** Efficient approach for checking conditions across subarrays of fixed size.
    
- **Array Traversal:** Two-pointer technique to iterate through subarrays.
    
- **Multiplication/Division Logic:** Tweaked logic to avoid errors in fractional comparisons.
    

---

