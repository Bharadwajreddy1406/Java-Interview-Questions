# LeetCode 144 – Binary Tree Preorder Traversal

**Link:** [https://leetcode.com/problems/binary-tree-preorder-traversal/](https://leetcode.com/problems/binary-tree-preorder-traversal/)

---

## 🧠 Problem Statement

Given the `root` of a binary tree, return the **preorder traversal** of its nodes' values.

> Preorder: **Root → Left → Right**

---

## ✅ Code (Recursive)

```java
class Solution {

    public void func(TreeNode root, List<Integer> res) {
        if (root == null) return;

        res.add(root.val);        // Visit root
        func(root.left, res);     // Left subtree
        func(root.right, res);    // Right subtree
    }

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        func(root, res);
        return res;
    }
}
````

---

## 🔍 Intuition

In preorder traversal, we:

1. Visit the current node.
    
2. Recursively visit the left subtree.
    
3. Recursively visit the right subtree.
    

---

## 🧮 Time & Space Complexity

- **Time:** O(n) – Each node is visited once.
    
- **Space:** O(n) – For recursion stack in the worst case (skewed tree).
    

---

## ✅ Test Cases

```text
Input: root = [1,null,2,3]
Output: [1,2,3]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
```

---

## 📌 Your Notes

> This is a classic recursion approach.  
> If asked to do this **iteratively**, we would use a **stack**:
> 
> - Push root
>     
> - While stack not empty:
>     
>     - Pop node, add to result
>         
>     - Push right first, then left (so left is processed first)
>         

---

