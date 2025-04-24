# Leetcode 121 - Best Time to Buy and Sell Stock 📈

## 🗓️ Date
2025-04-24

## 🏷️ Tags
`Greedy` `Array` `Sliding Window`

---

## 💡 Problem
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

You want to maximize your profit by choosing **a single day to buy** one stock and **a different day in the future to sell** that stock.

Return the **maximum profit** you can achieve from this transaction.  
If you can't achieve any profit, return `0`.

---

## 🧪 Test Case Example

### Input:
```txt
prices = [7,1,5,3,6,4]
````

### Output:

```txt
5
```

### Explanation:

Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

---

## 🧰 Data Structures Used

- Just simple **integers** to track:
    
    - The **minimum price** seen so far (best day to buy).
        
    - The **maximum profit** calculated till now.
        

---

## 🧠 My Notes

I did that pattern of updating the minimum so far while scanning and keeping the max profit in one loop.

This is a classic **single pass greedy** problem where you just keep track of two things:

- `minPrice`: the lowest price we've seen so far (good day to buy).
    
- `maxProfit`: the best profit we can make if we sell today.
    

Every time we move forward, we check if today is the new **minimum price**. Otherwise, we calculate profit = `today's price - minPrice`, and update max if it's higher.

The trick is:

- Buy at the **lowest point seen so far**.
    
- Try to sell at every point, check if it's the **best profit**.
    

---

## 🧾 Approach

1. Initialize `minPrice` with the first day’s price.
    
2. Loop through the array:
    
    - If current price is lower than `minPrice`, update `minPrice`.
        
    - Else, calculate `profit = currentPrice - minPrice` and update max profit.
        
3. Return `max`.
    

---

## 🧑‍💻 Code

```java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }

            max = Math.max(max, prices[i] - minPrice);
        }

        return max;
    }
}
```

---

## ⏱️ Complexity

- **Time:** O(n) — Only one pass through the prices array.
    
- **Space:** O(1) — Constant space, no extra data structures used.
    

---

## 🧠 Reflections

I did that simple but powerful trick — keep updating the minimum so far and calculating profit at each step.  
What I learned is: sometimes you don’t need dynamic programming or fancy stuff — just clean logic and greedy tracking works wonders.

Also, it reminds me to always ask:  
**What’s the best I can do with the info so far?**

---
