# 🧾 Leetcode 5: Longest Palindromic Substring – DP Approach

### ✅ Problem Summary:

Given a string `s`, return the longest substring which is a palindrome.

---

### 💡 Intuition:

- A palindrome reads the same forwards and backwards.
    
- Use **Dynamic Programming** to build a 2D table `dp[i][j]`:
    
    - `dp[i][j] == true` means the substring `s[i...j]` is a palindrome.
        
- We build this table bottom-up by increasing substring lengths.
    

---

### 🧠 Key Idea:

- For any substring `s[i...j]` to be a palindrome:
    
    - `s[i] == s[j]` **and**
        
    - `dp[i+1][j-1] == true` (i.e., the inner substring is also a palindrome)
        

---

### 🧱 DP Table:

- `dp[i][j]` → `true` if `s[i...j]` is a palindrome
    

---

### 🪜 Steps:

1. **Base case 1: Single letters**  
    Every character is a palindrome by itself.  
    `dp[i][i] = true`
    
2. **Base case 2: Two-character substrings**  
    If `s[i] == s[i+1]`, then `dp[i][i+1] = true`
    
3. **For substrings of length ≥ 3**  
    Loop over increasing lengths `k` from 3 to `n`  
    For each substring `s[i...j]` (where `j = i + k - 1`), check:
    
    ```java
    if (dp[i+1][j-1] && s.charAt(i) == s.charAt(j))
        dp[i][j] = true;
    ```
    
4. Whenever a new longer palindrome is found, update:
    
    ```java
    start = i;
    maxLen = k;
    ```
    

---

### ⏱️ Time Complexity:

- `O(n^2)` – Filling the 2D DP table of size `n x n`
    

### 📦 Space Complexity:

- `O(n^2)` – For the 2D `dp` array
    

---

### 🔁 Example:

For input `"babad"`

- Possible palindromes: `"bab"` and `"aba"`
    
- The code returns either (both are correct).
    

---

### 🧹 Clean Java Code:

```java
class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];

        int start = 0, maxLen = 1;

        // All substrings of length 1 are palindromes
        for (int i = 0; i < n; i++) dp[i][i] = true;

        // Substrings of length 2
        for (int i = 0; i < n - 1; ++i) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                dp[i][i + 1] = true;
                start = i;
                maxLen = 2;
            }
        }

        // Substrings of length 3 or more
        for (int len = 3; len <= n; ++len) {
            for (int i = 0; i <= n - len; ++i) {
                int j = i + len - 1;
                if (dp[i + 1][j - 1] && s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = true;
                    start = i;
                    maxLen = len;
                }
            }
        }

        return s.substring(start, start + maxLen);
    }
}
```

---
