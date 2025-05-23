# LeetCode 545 – Boundary of Binary Tree

**Link:** [https://leetcode.com/problems/boundary-of-binary-tree](https://leetcode.com/problems/boundary-of-binary-tree)  
**Tags:** Tree, DFS, Simulation

---

## 🧠 Problem Statement

Return the **values of the boundary of a binary tree** in **anticlockwise** direction starting from the root. The boundary includes:
- The root (if not a leaf),
- The **left boundary** (excluding leaves),
- All **leaf nodes** (from left to right),
- The **right boundary** (excluding leaves, in bottom-up order).

---

## ✅ Code (Java)

```java
class Solution {
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        if (!isLeaf(root)) res.add(root.val);
        addLeftBoundary(root.left, res);
        addLeaves(root, res);
        addRightBoundary(root.right, res);
        return res;
    }

    private boolean isLeaf(TreeNode node) {
        return node.left == null && node.right == null;
    }

    private void addLeftBoundary(TreeNode node, List<Integer> res) {
        while (node != null) {
            if (!isLeaf(node)) res.add(node.val);
            node = (node.left != null) ? node.left : node.right;
        }
    }

    private void addRightBoundary(TreeNode node, List<Integer> res) {
        List<Integer> temp = new ArrayList<>();
        while (node != null) {
            if (!isLeaf(node)) temp.add(node.val);
            node = (node.right != null) ? node.right : node.left;
        }
        for (int i = temp.size() - 1; i >= 0; --i) {
            res.add(temp.get(i));
        }
    }

    private void addLeaves(TreeNode node, List<Integer> res) {
        if (isLeaf(node)) {
            res.add(node.val);
            return;
        }
        if (node.left != null) addLeaves(node.left, res);
        if (node.right != null) addLeaves(node.right, res);
    }
}
````

---

## 🔍 Intuition

- Treat the boundary as **3 separate parts**:
    
    1. Left boundary: go left until you can't (skip leaves)
        
    2. Leaf nodes: in-order traversal (DFS)
        
    3. Right boundary: go right until you can't (collect and reverse)
        

We carefully avoid **duplicating leaves** and **root** is only added if it's not a leaf.

---

## 🧪 Example

```text
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
       / \
      8   9

=> Boundary: [1, 2, 4, 8, 9, 6, 7, 3]
```

---

## 🧮 Time & Space Complexity

- **Time Complexity:** `O(n)`
    
    - Every node is visited once.
        
- **Space Complexity:** `O(h)` for recursion stack (DFS), `O(n)` for result list.
    

---

## ✅ Notes

- Use `isLeaf()` to handle special cases.
    
- Left and right boundaries skip leaves to avoid duplication.
    
- Right boundary is reversed before adding to result.
    

---
