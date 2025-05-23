# LeetCode 513 – Find Bottom Left Tree Value

**Link:** [https://leetcode.com/problems/find-bottom-left-tree-value](https://leetcode.com/problems/find-bottom-left-tree-value)  
**Tags:** Tree, BFS, Level Order

---

## 🧠 Problem Statement

Given the `root` of a binary tree, return the **leftmost value in the last row** of the tree.

---

## ✅ Code (Java – BFS Approach)

```java
class Solution {
    public int findBottomLeftValue(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int leftMost = root.val;

        while (!q.isEmpty()) {
            int size = q.size();
            leftMost = q.peek().val;  // First node at current level

            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
        }

        return leftMost;
    }
}
````

---

## 🔍 Intuition

- Use **level order traversal (BFS)** to visit nodes level by level.
    
- The **first node** at each level (`q.peek().val`) is the **leftmost** for that level.
    
- The **last level’s first node** will be the answer.
    

---

## 🧪 Example

```text
Input:
      2
     / \
    1   3

Output: 1
```

```text
Input:
        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output: 7
```

---

## 🧮 Complexity

- **Time:** O(n) — every node is visited once
    
- **Space:** O(w) — width of the tree (maximum queue size at a level)
    

---

## ✅ Notes

- `q.peek().val` before the inner loop ensures we get the **first node at each level**.
    
- Order of pushing left child before right child ensures leftmost is visited first.
    

---
