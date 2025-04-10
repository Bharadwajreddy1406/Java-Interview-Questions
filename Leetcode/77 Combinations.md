# LeetCode 77 - Combinations

## Problem Description

Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

**Example:**

Input: `n = 4`, `k = 2`  
Output:  
```

[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

```

---

## Test Cases

### Test Case 1:
```

Input: n = 4, k = 2  
Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

```

### Test Case 2:
```

Input: n = 3, k = 2  
Output: [[1, 2], [1, 3], [2, 3]]

```

### Test Case 3:
```

Input: n = 1, k = 1  
Output: [[1]]

````

---

## Constraints

- `1 <= k <= n <= 50`

---

## Approach / Intuition

We will solve this problem using **backtracking**. 

1. **Backtracking** is a technique that involves exploring all possible solutions by trying out each option and **backtracking** when a solution doesn't work.
2. Here, we start with an empty combination and explore the next possible number. If the combination reaches the desired length `k`, we add it to the result.
3. At each step, we ensure we don’t revisit previous numbers by maintaining a starting index for the next recursive call. This way, the solution naturally generates combinations in lexicographical order.

### Key Steps:

- We recursively build combinations starting from `1` to `n`.
- Each combination is of size `k`, and we keep adding numbers to the current combination while ensuring no duplicates.
- Once the combination reaches size `k`, we store it and backtrack to explore other possibilities.

---

## Code Implementation

```java
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        back(ans, 1, n + 1, k, curr);
        return ans;
    }

    public void back(List<List<Integer>> ans, int start, int n, int k, List<Integer> current) {
        if (current.size() == k) {
            ans.add(new ArrayList<>(current)); // Add current valid combination
            return;
        }

        for (int i = start; i < n; i++) {
            current.add(i); // Add the current number
            back(ans, i + 1, n, k, current); // Recurse with next number
            current.remove(current.size() - 1); // Backtrack by removing the last number
        }
    }
}
````

---

## Time Complexity

- **Time Complexity:** `O(C(n, k))`, where `C(n, k)` is the number of combinations, i.e., the total number of ways to choose `k` elements from `n`.
    
- **Space Complexity:** `O(k)`, since we store each combination in a temporary list of size `k`.
    

---

## Additional Notes

- **Important Detail:** The `back` function starts with an index `start` to ensure that combinations are generated without repetition and in lexicographical order.
    
- **Edge Case Considerations:**
    
    - If `n = k`, there is only one combination, which is `[1, 2, ..., n]`.
        
    - If `k = 1`, all combinations are simply the individual numbers from `1` to `n`.
        

---

