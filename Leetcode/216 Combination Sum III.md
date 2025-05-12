# LeetCode 216 – Combination Sum III

**Link:** [LeetCode 216](https://leetcode.com/problems/combination-sum-iii/)

---

## 🧠 Problem Statement

Find all valid combinations of `k` numbers that add up to a number `n`, using only numbers from 1 to 9.  
Each number can be used **at most once**, and each combination should be **unique**.

---

## ✅ Code (Java – Backtracking)

```java
class Solution {

    public void backtrack(int index, int k, int n, List<List<Integer>> ans, List<Integer> curr) {
        if (curr.size() == k && n == 0) {
            ans.add(new ArrayList<>(curr));
            return;
        }

        for (int i = index; i <= 9; i++) {
            if (i > n) break; // Prune the branch early
            curr.add(i);
            backtrack(i + 1, k, n - i, ans, curr); // Move to next number
            curr.remove(curr.size() - 1);
        }
    }

    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(1, k, n, ans, new ArrayList<>());
        return ans;
    }
}
````

---

## 💡 Notes

- This is a **combinations** problem, not permutations.
    
- No need for `visited[]` because:
    
    - The loop always picks next number starting from `index + 1`.
        
    - Ensures numbers are **not reused**.
        
    - Keeps combinations in **ascending order**, avoiding duplicates like `[3,2,1]`.
        

---

## 🔍 Intuition

We are picking numbers from 1 to 9, **at most once**, and finding all combinations of length `k` such that their sum is `n`.

Use **backtracking** to try:

- Add a number `i`
    
- Reduce `n` by `i`
    
- Recurse with `i + 1` as next start (ensuring no reuse)
    
- If size becomes `k` and sum is `n == 0`, it's a valid result.
    

---

## 🌳 Backtracking Tree Example

Example Input: `k = 3`, `n = 7`

```
Start from 1:
  1 → 2 → 4 ✅ [1,2,4]
  1 → 2 → 5 ❌ (sum too large)
  1 → 3 → 4 ❌ (sum = 8 > 7)

Try from 2:
  2 → 3 → 4 ❌ (sum = 9)

Only one valid combo: [1,2,4]
```

---

## 🧮 Time & Space Complexity

- **Time:** $$O(C(9, k))$$ → maximum combinations choosing `k` from 9
    
- **Space:** $$O(k)$$ recursion stack + $$O(1) extra$$
    

---

## ⚙️ Constraints

- 1 ≤ `k` ≤ 9
    
- 1 ≤ `n` ≤ 60
    

---

## ✅ Test Cases

```text
Input: k = 3, n = 7
Output: [[1,2,4]]

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]

Input: k = 4, n = 1
Output: []
```

---

## 🛠️ Optimization

The line `if (i > n) break;` is a small pruning trick:

- No point checking numbers that would make `n` negative.
    

---
