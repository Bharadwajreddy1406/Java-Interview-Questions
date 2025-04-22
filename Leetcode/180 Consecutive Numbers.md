# 📊 LeetCode 180 – Consecutive Numbers

**Link**: [https://leetcode.com/problems/consecutive-numbers](https://leetcode.com/problems/consecutive-numbers)  
**Date**: `22-04-2025`  
**Tags**: `SQL`, `self-join`, `window-function`  
**Platform**: LeetCode  
**Difficulty**: Medium

---

## 🚀 Problem
Find all numbers that appear **at least three times consecutively** in a `Logs` table.

---

## 🧠 Intuition
We want to detect sequences where the **same number appears in 3 consecutive rows** based on increasing `id`.  
We'll use **self-joins** on the same table and check:
- `l1.id = l2.id - 1`
- `l2.id = l3.id - 1`
- `l1.num = l2.num = l3.num`

---

## 💡 Tricky Case
### Input:
| id | num |
|----|-----|
| 1  | 3   |
| 2  | 3   |
| 3  | 3   |
| 4  | 3   |

### ❌ My Output (Duplicates):
| ConsecutiveNums |
|-----------------|
| 3               |
| 3               |

### ✅ Expected:
| ConsecutiveNums |
|-----------------|
| 3               |

### 🛠️ Fix:
Added `DISTINCT` to remove duplicates from the result.

---

## ✅ Final Query
```sql
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM logs l1, logs l2, logs l3
WHERE l1.id = l2.id - 1 
  AND l2.id = l3.id - 1
  AND l1.num = l2.num 
  AND l2.num = l3.num;
````

---

## 🔍 Explanation

1. **Self Join**:
    
    - We join the `logs` table three times (`l1`, `l2`, `l3`) to compare 3 consecutive rows.
        
2. **ID Conditions**:
    
    - Ensure they are consecutive by checking:  
        `l1.id = l2.id - 1`  
        `l2.id = l3.id - 1`
        
3. **Value Equality**:
    
    - All three must have the same `num`:  
        `l1.num = l2.num AND l2.num = l3.num`
        
4. **DISTINCT**:
    
    - Avoid duplicate results when more than 3 consecutive entries have the same number.
        

---

## ⏱️ Time & Space Complexity

- **Time**: O(n²) – due to the self-join, but manageable for small datasets
    
- **Space**: O(1)
    

---

## 🧠 Reflection

- Using multiple self-joins is intuitive here.
    
- Easily falls into the duplicate-result trap when there are **more than 3** in a row — remember to `DISTINCT`!
    
---
explore the concept of window functions in SQL
#windowfunctions