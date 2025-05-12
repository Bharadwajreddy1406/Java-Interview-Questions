# LeetCode 131. Palindrome Partitioning

**Link:** [LeetCode 131](https://leetcode.com/problems/palindrome-partitioning/)

---

## 🧠 Problem Statement

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return all possible palindrome partitioning combinations.

---

## 🧪 Constraints

- 1 <= `s.length` <= 16
- Only lowercase English letters

---

## ✅ Code (Java – Backtracking)

```java
class Solution {

    public void backtrack(String s, int index, int n, List<String> curr, List<List<String>> ans) {
        if (index == n) {
            ans.add(new ArrayList<>(curr));
            return;
        }

        for (int i = index + 1; i <= n; i++) {
            String sub = s.substring(index, i);
            if (isPalindrome(sub)) {
                curr.add(sub);
                backtrack(s, i, n, curr, ans);
                curr.remove(curr.size() - 1);
            }
        }
    }

    public boolean isPalindrome(String s) {
        int n = s.length();
        for (int i = 0; i < n / 2; i++) {
            if (s.charAt(i) != s.charAt(n - i - 1)) return false;
        }
        return true;
    }

    public List<List<String>> partition(String s) {
        List<List<String>> ans = new ArrayList<>();
        backtrack(s, 0, s.length(), new ArrayList<>(), ans);
        return ans;
    }
}
````

---

## 🔍 Intuition

This is a **backtracking problem** where we explore every possible partition of the string and pick those combinations where each part is a palindrome.

- At each step, take a prefix substring from `index` to `i`
    
- If it’s a **palindrome**, explore recursively from `i`
    
- Backtrack by removing the last added segment
    

---

## 🌳 Backtracking Tree Example

Input: `"aab"`

```
Start → "a" (palindrome)
          → "a" (palindrome)
              → "b" (palindrome)
                ✅ ["a", "a", "b"]
          → "ab" (not palindrome)

Start → "aa" (palindrome)
          → "b" (palindrome)
            ✅ ["aa", "b"]

Start → "aab" (not palindrome)
```

Final Output:

```text
[["a","a","b"], ["aa","b"]]
```

---

## 🧮 Time & Space Complexity

- **Time Complexity:** O(2^n × n)
    
    - 2^n for exploring all partitions
        
    - O(n) to check palindrome at each node (could be optimized using memoization)
        
- **Space Complexity:** O(n) for recursion stack + O(n) for each `curr` list
    

---

## ⚡ Optimizations

- You can **memoize palindrome checks** using a 2D DP table: `dp[i][j] = true` if `s[i..j]` is a palindrome
    

---

## 📦 Data Structures Used

- `List<String> curr` – stores the current path (partition so far)
    
- `List<List<String>> ans` – stores all valid partitions
    
- Recursion stack for exploring options
    

---

## ✅ Edge Cases

- `"a"` → `[["a"]]`
    
- `"aaa"` → `[["a","a","a"], ["a","aa"], ["aa","a"], ["aaa"]]`
    

---

