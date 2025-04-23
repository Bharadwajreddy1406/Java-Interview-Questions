# 🧠 LeetCode 91 – Decode Ways

**Date**: 2025-04-23  
**Tags**: `Recursion`, `Memoization`, `DP`, `Digit Parsing`, `Leetcode-91`

---

## 🔍 Problem Summary

Given a string `s` containing only digits, return the total number of ways to decode it into letters (like A-Z), where:

- `"1"` → `'A'`,  
- `"2"` → `'B'`,  
- ...  
- `"26"` → `'Z'`.

### ⚠️ Constraints:
- `'0'` is **invalid** unless it's part of `"10"` to `"26"`.
- We can decode:
  - **One digit at a time**, or
  - **Two digits at a time** (if the value ≤ 26)

---

## 💡 Intuition

At every index:
- We try taking **one digit** and decode recursively.
- If possible, we take **two digits** and decode recursively.
- Sum both the results.
#thinklikethis
1) we'll choose index
2) we'll do all stuff on the index ( that is picking 1 digit, or picking 2 digit )
3) at the end we sum the results and return


🗣️ My Thought Process:
> This is a problem where we either pick 1 digit or 2 digits. If we reach the end of the string, it's a successful decoding path and we return 1.  
> If a path reaches an invalid `0` → return 0.  
> Memoization just stores the result of a subproblem at `dp[index]`, making it easy to optimize.

---

## 🔁 Recursive + Memoization Code

```java
class Solution {

    public int func(int index, int n, String s, int[] dp){
        if(index >= s.length()) return 1;  // Base case: fully decoded

        if(s.charAt(index) == '0') return 0;  // Invalid path

        if(dp[index] != -1) return dp[index];

        int twoway = 0;

        // Check if 2-digit decode is valid
        if(index < n-1){
            if(Integer.parseInt("" + s.charAt(index) + s.charAt(index+1)) <= 26){
                twoway += func(index + 2, n, s, dp);
            }
        }

        // Always try 1-digit decode
        int oneway = func(index + 1, n, s, dp);

        return dp[index] = oneway + twoway;
    }

    public int numDecodings(String s) {
        int[] dp = new int[s.length()];
        Arrays.fill(dp, -1);
        return func(0, s.length(), s, dp);
    }
}
````

---

## 🧪 Example

### Input:

```
s = "226"
```

### Output:

```
3
```

### Explanation:

- `"2 2 6"` → "BBF"
    
- `"22 6"` → "VF"
    
- `"2 26"` → "BZ"
    

---

## 🧠 Key Takeaways

- Think of the recursion as a **decision tree**:
    
    - At each index: take 1 digit or 2 digits if valid.
        
    - Add both choices' return values.
        
- **Memoization is easy**: just store the result of each index so we don't recompute.
    

---

## ⏱️ Complexity

|Metric|Value|
|---|---|
|Time|O(n)|
|Space|O(n) (DP + stack)|

---
