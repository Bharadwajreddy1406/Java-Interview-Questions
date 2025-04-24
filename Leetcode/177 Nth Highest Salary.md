# 🧠 LeetCode 177 – Nth Highest Salary

**Date**: 2025-04-23  
**Tags**: `SQL`, `Function`, `Subquery`, `Leetcode-177`

---

## 📄 Problem

Write a SQL query to get the **Nth** highest salary from the `Employee` table.  
If there is no **Nth** highest salary, the query should return `null`.

---

## ✅ SQL Function

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE offset_value INT;
  SET offset_value = N - 1;

  RETURN (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET offset_value
  );
END
````

---

## 🧠 Explanation

- **Input**: The function accepts an integer `N`, which represents the **Nth highest salary** to be fetched.
    
- **Logic**:
    
    - **`offset_value`** is calculated as `N - 1` since the **`OFFSET`** starts from 0 (i.e., if you want to skip `N-1` records, you need to start from `N-1`).
        
    - We select **distinct salaries** from the `Employee` table and **order** them in descending order (highest to lowest).
        
    - The **`LIMIT 1 OFFSET`** is used to skip the first `N-1` salaries and fetch the **Nth** salary.
        
- **Edge case**: If `N` exceeds the number of unique salaries, the query will return `null` as there is no **Nth** salary.
    

---

## 🧑‍💻 Rules of Usage for `OFFSET`

- **`OFFSET`** is used to **skip a specified number of rows** in the result set before beginning to return rows.
    
- It is generally used in conjunction with `LIMIT` to implement pagination or to fetch results starting from a particular row.
	
> it's used with `order by`  and not separately

### **Syntax**:

```sql
SELECT column_name
FROM table_name
ORDER BY column_name
LIMIT N OFFSET M;
```

- **`LIMIT N`**: Limits the result to `N` rows.
    
- **`OFFSET M`**: Skips the first `M` rows.
    

### **Examples**:

1. **Fetching the 2nd highest salary**:
    
    ```sql
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1;
    ```
    
    - **Explanation**: This will skip the highest salary (1 row) and return the **second highest salary**.
        
2. **Fetching the 3rd highest salary**:
    
    ```sql
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 2;
    ```
    
    - **Explanation**: This skips the top 2 salaries and fetches the **third highest salary**.
        
3. **Fetching all salaries starting from the 5th highest**:
    
    ```sql
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 10 OFFSET 4;
    ```
    
    - **Explanation**: This will return the next 10 salaries starting from the **5th highest** salary.
        
4. **When `OFFSET` exceeds the total number of records**:
    
    ```sql
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 100;
    ```
    
    - **Explanation**: If there are fewer than 100 distinct salaries, the query will return `null` because the `OFFSET` exceeds the available rows.
        

### **Important Considerations**:

- **Performance**: Using `OFFSET` with large result sets can be inefficient because the database has to process and skip the first `M` rows before starting to return results.
    
- **Edge cases**: If `N` exceeds the number of rows or unique values in the result, the query will return `null` because there's no corresponding record.
    

---

## 🛠️ Notes

- This approach efficiently handles the problem using the **`DISTINCT`** keyword to avoid duplicates in salary and ensures the correct Nth value is returned by using **`OFFSET`**.
    
- The solution works in **MySQL** for getting the Nth highest salary using a custom function.
    

---
