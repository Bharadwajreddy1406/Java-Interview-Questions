# 🧠 LeetCode 176 – Second Highest Salary

**Date**: 2025-04-23  
**Tags**: `SQL`, `Subquery`, `Aggregation`, `Leetcode-176`

---

## 📄 Problem

Write a SQL query to get the second highest salary from the `Employee` table.  
If no second highest salary exists, the query should return `null`.

---

## ✅ SQL Query

```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee)
LIMIT 1;
````

---

## 🧠 Explanation

- We use a **subquery** to get the **maximum salary** in the table.
    
- Then we **filter** the `Employee` records to get only those salaries **less than** the max.
    
- From this filtered set, we get the **maximum salary again**, which will be the **second highest**.
    
- The `LIMIT 1` ensures we only return one row.
    

✅ If there is **no second highest salary** (i.e., all employees have the same salary), the subquery returns an empty set, and the result will be `null`.

---

## 🛠️ Alternate Approaches

You can also use `DISTINCT` and `ORDER BY` with `LIMIT` and `OFFSET`, like:

```sql
SELECT DISTINCT salary AS SecondHighestSalary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

---

## ⚙️ Notes

Both solutions are valid. The subquery + MAX method is often cleaner for interview-style questions.

---
