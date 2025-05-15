# LeetCode 110 – Balanced Binary Tree

**Link:** [LeetCode 110](https://leetcode.com/problems/balanced-binary-tree/)

---

## 🧠 Problem Statement

A binary tree is **balanced** if:

- The left and right subtrees of **every node** differ in height by **no more than 1**.

Given the `root` of a binary tree, return `true` if it is balanced, or `false` otherwise.

---

## ✅ Code (Java – Post-order DFS with Early Exit)

```java
class Solution {

    public int helper(TreeNode root){
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;

        int lh = helper(root.left);
        int rh = helper(root.right);

        if(lh == -1 || rh == -1) return -1;

        if(Math.abs(lh - rh) > 1) return -1;

        return Math.max(lh, rh) + 1;
    }

    public boolean isBalanced(TreeNode root) {
        return helper(root) != -1;
    }
}
````

---

## 💡 Notes

- This problem is **post-order DFS traversal**.
    
- The key idea is:
    
    - Calculate height of left and right subtrees.
        
    - If any subtree is already unbalanced (`-1`), stop early and return `-1`.
        
    - Otherwise, check balance condition `|left - right| <= 1`.
        
- Return actual height if balanced, otherwise `-1` to bubble up failure.
    

---

## 🔍 Intuition

- Normally, to check balance you might:
    
    1. Compute left subtree height.
        
    2. Compute right subtree height.
        
    3. Check balance.
        
    
    - But that leads to **O(n²)** in worst case.
        
- In this optimized approach:
    
    - You return `-1` **early** if any subtree is unbalanced.
        
    - This ensures **O(n)** time.
        

---

## 🧮 Time & Space Complexity

- **Time:** O(n), where n is the number of nodes (each visited once).
    
- **Space:** O(h), where h is the height of the tree (recursion stack).
    

---

## ✅ Test Cases

```text
Input: [3,9,20,null,null,15,7]
Output: true

Input: [1,2,2,3,3,null,null,4,4]
Output: false

Input: []
Output: true
```

---

## 🌳 Tree Traversal Flow (Post-order)

For node `root`:

1. Compute `leftHeight`
    
2. Compute `rightHeight`
    
3. If either is `-1` → bubble up unbalanced.
    
4. If `|leftHeight - rightHeight| > 1` → return `-1`.
    
5. Else return `max(leftHeight, rightHeight) + 1`.
    

---

## 📌 Your Observations

> This is a smart variation of the height-finding function.  
> Instead of separately checking if each subtree is balanced,  
> We cleverly use the height return value to encode imbalance using `-1`.  
> This avoids redundant traversal and leads to **O(n)** solution.

---
