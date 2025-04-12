## LeetCode 1004: Max Consecutive Ones III

#### 🔧 Problem Statement:

Given a binary array `nums` and an integer `k`, return the **maximum number of consecutive 1's** in the array if you can flip at most `k` 0's.

---

#### 💡 Core Idea:

**Think of this question as finding the longest subarray with at most `k` zeros.**

Once you look at it that way, the problem becomes a classic **sliding window** task:

- Keep a window with **at most `k` zeros**.
    
- Expand the window to the right, and **shrink from the left** when you exceed `k` zeros.
    

---

#### ✅ Constraints:

- You can flip **at most `k`** zeros to 1s.
    
- The subarray must be **contiguous**.
    

---

#### 🧠 Intuition:

- Use two pointers (`left` and `right`) to create a sliding window.
    
- Count the number of zeros within the current window.
    
- If the count of zeros exceeds `k`, move the `left` pointer until the window becomes valid again (i.e., contains at most `k` zeros).
    
- At each step, track the **maximum length** of such a valid window.
    

---

#### 🧪 Test Case Insight:

```
nums = [0, 0, 0, 1], k = 4
```

Here:

- The total number of zeros is 3, which is **less than `k`**.
    
- So we can flip **all of them** and include the 1 → longest subarray is of length `4`.
    

✅ If you used this condition:

```java
if(count == k) {
    max = Math.max(max, right - left + 1);
}
```

Then you'd miss cases where the number of zeros is **less than `k`**.  
So that check is **unnecessary**.

the code still works because of the max comparison at the end of while loop

The **`while(count > k)`** logic already ensures the window always has **at most `k`** zeros.

---

#### ✅ Final Code:

```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int right = 0;
        int count = 0;  // count of zeros in current window
        int max = 0;

        while (right < nums.length) {
            if (nums[right] == 0) count++;

            // Shrink window from the left if we exceed k flips
            while (left < nums.length && count > k) {
                if (nums[left] == 0) count--;
                left++;
            }

            // Update max with current window size
            max = Math.max(max, right - left + 1);
            right++;
        }

        return max;
    }
}
```

---

#### 🔍 Complexity:

- **Time Complexity**: `O(n)`
    
- **Space Complexity**: `O(1)`
    

---

#### 🧘 Key Takeaway:

- 🔁 **View it as: “Longest subarray with at most `k` zeros.”**
    
- 🧹 The `while(count > k)` ensures window validity.
    
- 🧼 **No need to check for `count == k`** – we want **up to `k`** zeros, not exactly `k`.
    

---

