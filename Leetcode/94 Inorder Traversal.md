# LeetCode 94 – Binary Tree Inorder Traversal

**Link:** [https://leetcode.com/problems/binary-tree-inorder-traversal/](https://leetcode.com/problems/binary-tree-inorder-traversal/)

---

## 🧠 Problem Statement

Given the `root` of a binary tree, return its **inorder traversal** as a list.

> Inorder Traversal: **Left → Root → Right**

---

## ✅ Code (Recursive – C++)

```cpp
class Solution {
public:
    vector<int> v;

    void ino(TreeNode* root) {
        if (root == NULL) return;

        ino(root->left);          // Traverse left
        v.push_back(root->val);   // Visit root
        ino(root->right);         // Traverse right
    }

    vector<int> inorderTraversal(TreeNode* root) {
        ino(root);
        return v;
    }
};
````

---

## 🔍 Intuition

In an inorder traversal, we:

1. Recurse on the left child.
    
2. Visit the current node.
    
3. Recurse on the right child.
    

---

## 🧮 Time & Space Complexity

- **Time Complexity:** O(n) – Each node is visited once.
    
- **Space Complexity:** O(n) – For recursion stack in the worst case (e.g. skewed tree).
    

---

## ✅ Sample Test Cases

```text
Input: root = [1,null,2,3]
Output: [1,3,2]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
```

---

## 🗒️ Your Notes

> This is a straightforward recursive solution.  
> In C++, member variable `v` is used to store results.  
> We could also solve this using an **iterative stack-based approach** if recursion is not preferred.

---

