# Leetcode 181 - Employees Earning More Than Their Managers

## Question
Given an `Employee` table, write a query to find all employees who earn more than their managers. Return the names of these employees.

---

## Schema

### Employee Table

| Column     | Type    | Description                                 |
|------------|---------|---------------------------------------------|
| id         | INT     | The unique ID of the employee.              |
| name       | VARCHAR | The name of the employee.                   |
| salary     | INT     | The salary of the employee.                 |
| managerId  | INT     | The ID of the employee's manager (NULL if the employee has no manager). |

---

## Solution

```sql
SELECT e1.name AS Employee
FROM Employee e1
JOIN Employee e2
ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
````

### Explanation:

1. **Self-Join:** The query performs a self-join on the `Employee` table. `e1` represents the employee, and `e2` represents their manager. The `JOIN` condition `e1.managerId = e2.id` ensures we pair each employee with their manager.
    
2. **Filter Condition:** The `WHERE` clause ensures we only select employees whose salary is greater than the salary of their manager (`e1.salary > e2.salary`).
    
3. **Selection:** We select only the `name` column from `e1`, which represents the employees who meet the criteria.
    

---

## Example

### Input

| id  | name    | salary | managerId |
| --- | ------- | ------ | --------- |
| 1   | John    | 10000  | 2         |
| 2   | Alice   | 2000   | NULL      |
| 3   | Bob     | 1500   | 2         |
| 4   | Charlie | 3000   | 1         |

### Output

|Employee|
|---|
|John|

- John earns more than Alice, so John is returned.
    

---

## Time & Space Complexity

- **Time Complexity:** O(n) - The query performs a self-join between employees and managers. Each row is compared once.
    
- **Space Complexity:** O(n) - The space complexity comes from storing the result set, which contains employees' names.
    

---

## Key Concepts

- **Self-Join:** The query joins the `Employee` table with itself to relate employees to their managers.
    
- **Join Condition:** The `managerId` field links employees to their managers.
    
- **Filter Condition:** The filter ensures we only select employees whose salary is greater than their manager's salary.
    

---
