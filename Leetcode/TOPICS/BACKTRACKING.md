[[17.Letter Combinations of a Phone Number]]
[[22. Generate Parentheses]]	
[[37.Sudoku Solver]]
[[39.Combination Sum]]
[[40.Combination Sum II]]
[[46. Permutations]]
[[51. N-Queens]]
[[52 N-Queens II]]
[[77 Combinations]]
[[78. Subsets]]
[[79 Word Search]]
[[90. SUBSETS II]]
[[93. Restore IP Addresses]]
[[113 Path Sum II]]
[[131 Palindrome Partitioning]]
[[47. Permutations II]]
[[216 Combination Sum III]]
[[401 Binary watch]]



### 🔁 Pattern: Sort + Skip Duplicates = Use `for` loop with `continue`

When dealing with problems like:

- **Subset II**
    
- **Combination Sum II**
    
- **Permutations II**
    

The **standard approach** is:

1. **Sort the array** to bring duplicates together.
    
2. Use a **`for` loop** to explore choices at the current level.
    
3. **Skip duplicates** using this pattern:
    
    ```java
    if (i > start && nums[i] == nums[i - 1]) continue;
    ```
    

This means:

- Only the **first occurrence** of a duplicate is allowed at a specific recursive level.
    
- All others are skipped to avoid repeated solutions.
    

---

### 🧠 Mnemonic to remember:

> **“Sort first, skip with `i > start`.”**  
> (Start means the current level in DFS.)

---
