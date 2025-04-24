# Leetcode 509 - Fibonacci Number 🧩

## 🗓️ Date
2025-04-24

## 🏷️ Tags
`Dynamic Programming` `Recursion` `Memoization`

---

## 💡 Problem
The problem asks to return the nth Fibonacci number. The Fibonacci sequence is defined as:

```

F(0) = 0 F(1) = 1 F(n) = F(n-1) + F(n-2) for n > 1

````

You need to implement a function that efficiently computes the nth Fibonacci number using dynamic programming.

---

## 🧪 Test Case Example

### Input:
```txt
n = 5
````

### Output:

```txt
5
```

### Explanation:

The Fibonacci sequence is: `0, 1, 1, 2, 3, 5`, so the 5th Fibonacci number is `5`.

---

## 🧰 Data Structures Used

- **Array (DP Table)**: Used to store previously calculated Fibonacci values to avoid recomputation.
    

---

## 🧠 My Notes

In this problem, I used **memoization** to avoid redundant calculations while solving the Fibonacci sequence.  
I did that by using a `dp` array where `dp[i]` stores the Fibonacci number for index `i`.  
If the value has already been computed, I simply return it from the `dp` array instead of recalculating it.

Here’s what I learned:

- The key idea is to solve the subproblems once and store the results for future reference.
    
- I used a top-down approach with recursion and **memoization** to ensure we don't solve the same problem multiple times.
    
- The base cases (`n <= 0` and `n == 1`) are handled explicitly, while the recurrence is simple: `fibo(n) = fibo(n-1) + fibo(n-2)`.
    

---

## 🧾 Approach

1. **Base Cases**: If `n <= 0`, return `0`. If `n == 1`, return `1`.
    
2. Use a **dp array** to store the Fibonacci numbers.
    
3. **Recursion with Memoization**: If the Fibonacci number at index `n` has already been calculated (`dp[n] != -1`), return it. Otherwise, calculate it using the recurrence relation and store the result in `dp[n]`.
    

---

## 🧑‍💻 Code

```java
class Solution {

    public int fibo(int n, int[] dp) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        if (dp[n] != -1) return dp[n];
        return dp[n] = fibo(n-1, dp) + fibo(n-2, dp);
    }

    public int fib(int n) {
        int dp[] = new int[n + 1];
        Arrays.fill(dp, -1);
        return fibo(n, dp);
    }
}
```

---

## ⏱️ Complexity

- **Time:** O(n) — The function is called for each value from 0 to n, and each subproblem is solved only once due to memoization.
    
- **Space:** O(n) — The space complexity comes from the `dp` array, which stores the Fibonacci numbers.
    

---

## 🧠 Reflections

I did that classic mistake in the beginning — I didn't use memoization and kept recalculating Fibonacci values, leading to excessive recomputation.  
Once I added the `dp` array and used memoization, the solution became significantly more efficient.

The main takeaway here was **memoization** in recursion. It saves a lot of time when you need to solve the same problem multiple times.

---
