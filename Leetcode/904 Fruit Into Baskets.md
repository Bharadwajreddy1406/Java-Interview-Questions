## 🧠 Leetcode 904 – Fruit Into Baskets

**Category**: Sliding Window  
**Difficulty**: Medium  
**Link**: [Leetcode 904](https://leetcode.com/problems/fruit-into-baskets/)  
**Tag**: `sliding-window` `hashmap` `two-pointers`

---

### 📜 Problem Statement

You are given an array of integers `fruits` where `fruits[i]` represents a type of fruit.

You want to collect **at most 2 types** of fruits into baskets. You can only pick **one fruit per tree**, starting from any tree, and moving to the right. Find the **maximum number of fruits you can collect in total**.

---

### 🔍 Example

```text
Input: fruits = [1,2,1]
Output: 3

Input: fruits = [0,1,2,2]
Output: 3

Input: fruits = [1,2,3,2,2]
Output: 4
```

---

### 🧩 Approach: Sliding Window

- Use a **hash map** to track the count of each fruit type in the window.
    
- Expand the window by moving `right`.
    
- If we ever have **more than 2 types**, shrink the window by moving `left` until only 2 types remain.
    
- Keep updating the maximum window size.
    

---

### ✅ Code (Java)

```java
class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> map = new HashMap<>();
        int left = 0;
        int max = 0;

        for (int right = 0; right < fruits.length; right++) {
            map.put(fruits[right], map.getOrDefault(fruits[right], 0) + 1);

            while (map.size() > 2) {
                map.put(fruits[left], map.get(fruits[left]) - 1);
                if (map.get(fruits[left]) == 0) {
                    map.remove(fruits[left]);
                }
                left++;
            }

            max = Math.max(max, right - left + 1);
        }

        return max;
    }
}
```

---

### 🧠 Key Observations

- The max number of fruits collected is equal to the **longest subarray with at most 2 distinct integers**.
    
- HashMap is used to **count frequency** of each fruit type.
    
- The window is adjusted dynamically based on the number of types.
    

---

### 📌 Time & Space Complexity

- **Time**: O(n) — each element is processed at most twice.
    
- **Space**: O(1) — at most 3 keys in the map (since we remove when >2 types).
    
---
