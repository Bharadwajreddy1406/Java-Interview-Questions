# LeetCode 3355 – Make a Zero Array

**Link:** [https://leetcode.com/problems/make-a-zero-array](https://leetcode.com/problems/make-a-zero-array)  
references: [https://www.youtube.com/watch?v=AEo-Iu0J5DQ](https://www.youtube.com/watch?v=AEo-Iu0J5DQ) 
and 
[https://www.youtube.com/watch?v=R-PBfqsRGP0](https://www.youtube.com/watch?v=R-PBfqsRGP0)
**Tag:** Difference Array, Prefix Sum, Greedy

---

## 🧠 Problem Statement

You're given an array `nums` and a list of `queries`, where each query represents an operation that decreases all elements in the subarray `nums[l...r]` by `1`.

Determine if it's possible to apply all operations such that **all elements of `nums` become 0 or less**.

---

## ✅ Code (Java – Using Difference Array)

```java
class Solution {
  public boolean isZeroArray(int[] nums, int[][] queries) {
    int[] tr = new int[nums.length + 1]; // Difference array

    for (int[] q : queries) {
      tr[q[0]]++;         // increment at start
      tr[q[1] + 1]--;     // decrement after end
    }

    int val = 0;  // running sum
    for (int i = 0; i < nums.length; i++) {
      val += tr[i];         // accumulate the effect of difference array
      if (nums[i] > val) {  // not enough decrements to bring nums[i] to 0
        return false;
      }
    }

    return true;
  }
}
````

---

## 🧮 Time & Space Complexity

- **Time Complexity:** `O(n + q)`
    
    - `n` = length of `nums`
        
    - `q` = number of queries
        
- **Space Complexity:** `O(n)`
    

---

## 🔍 Intuition

To perform **multiple range updates efficiently**, we use a **difference array**:

- For each query `[l, r]`, we do:
    
    - `diff[l] += 1`
        
    - `diff[r + 1] -= 1`
        
- The prefix sum of this difference array gives us the **net effect at each index**.
    
- If `nums[i] > effect[i]` at any point, then we **can't reduce it to 0**, so return false.
    

---

## 📝 Prerequisite

### ✅ Difference Array Concept

For efficient range increment operations:

- To add `+1` from `l` to `r`:
    
    - `diff[l] += 1`, `diff[r+1] -= 1`
        
- Final array after all operations = prefix sum of `diff[]`
    

---

## ✅ Example

```text
Input:
nums = [2,1,1]
queries = [[0,1],[1,2]]

Build difference array:
tr = [0,0,0,0]
query [0,1] → tr[0]++, tr[2]--
query [1,2] → tr[1]++, tr[3]--

tr = [1,1,-1,-1]

Now prefix sum:
val = 0 → [1,2,1]
Check: [2,1,1] ≤ [1,2,1] → false

Output: false
```

---

## 🗒️ Notes

> This is a **classic use case of the difference array** for range update problems.  
> Efficiently checks if all values can be brought down to 0 using the given operations.

---

## 🔁 Related Problems

- 370. Range Addition (classic difference array)
        
- 1094. Car Pooling
        
- 2531. Make Number of Distinct Characters Equal
        

```

Let me know if you'd like this grouped with other **range update** problems like LeetCode 370 or car pooling problems for your notes!
```