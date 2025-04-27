# Leetcode 619 - Biggest Single Number

## 🧩 Question

Write an SQL query to find the **largest number** that appears **only once** in the table `MyNumbers`.  
If no such number exists, return `null`.

---

## 🧱 Schema

### Table: `MyNumbers`

| Column Name | Type |
|-------------|------|
| num         | int  |

- Each row contains a single number.
- Some numbers may appear more than once.

---

## 📥 Example Input

**Input:**

```text
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+
````

**Output:**

```text
+-----+
| num |
+-----+
| 6   |
+-----+
```

**Explanation:**  
The numbers that appear only once are: `1`, `4`, `5`, and `6`.  
The largest among them is **6**, so we return it.

---

## ✅ Solution

```sql
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS t;
```

---

## 🔍 Explanation

- `GROUP BY num` groups all identical numbers.
    
- `HAVING COUNT(*) = 1` filters the groups to keep only numbers that appear once.
    
- The outer `SELECT MAX(num)` returns the **largest** of these unique values.
    
- If no such number exists, `MAX()` will return `NULL`, as required.
    

---

## 🧠 Concepts Used

- Aggregate Functions: `COUNT()`, `MAX()`
    
- Grouping Data: `GROUP BY`
    
- Filtering Aggregates: `HAVING`
    
- Subqueries
    

---

## 🧱 Output Schema

|num|
|---|
|int (or null)|

---
I started by thinking:

> “What defines a ‘single number’? It’s one that appears exactly once.”

From that thought, I realized I needed to **group** the numbers and **filter** those groups.  
Once I isolated the unique ones, the final step was just finding the **maximum**.

So it's a two-step pipeline:

1. Get unique numbers with `HAVING COUNT(*) = 1`.
    
2. Get the maximum of that list with `MAX()`.
    

---
