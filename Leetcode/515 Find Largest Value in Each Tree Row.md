# LeetCode 515 – Find Largest Value in Each Tree Row

**Link:** [https://leetcode.com/problems/find-largest-value-in-each-tree-row](https://leetcode.com/problems/find-largest-value-in-each-tree-row)  
**Tags:** Tree, BFS, Level Order

---

## 🧠 Problem Statement

Given the root of a binary tree, return **an array of the largest value in each row** of the tree (0-indexed).

---

## ✅ Code (Java – Level Order Traversal / BFS)

```java
class Solution {
    public List<Integer> largestValues(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;

        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            int max = Integer.MIN_VALUE;

            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                max = Math.max(max, node.val);
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }

            res.add(max);
        }

        return res;
    }
}
````

---

## 🔍 Intuition

- Traverse the tree **level by level** (using BFS).
    
- Track the **maximum value** at each level.
    
- Append the max of each level to the result list.
    

---

## 🧪 Examples

```text
Input:
        1
       / \
      3   2
     / \   \
    5   3   9

Output: [1, 3, 9]
```

---

## 🧮 Complexity

- **Time Complexity:** O(n) — every node is visited once.
    
- **Space Complexity:** O(w) — where `w` is the maximum width of the tree (max nodes in any level).
    

---
