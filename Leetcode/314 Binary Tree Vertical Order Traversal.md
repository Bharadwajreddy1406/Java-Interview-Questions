# LeetCode 314 – Binary Tree Vertical Order Traversal

**Link:** [https://leetcode.com/problems/binary-tree-vertical-order-traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/)  
**Tags:** Tree, BFS, HashMap, Queue, Level Order

---

## 🧠 Problem Statement

Given the `root` of a binary tree, return the **vertical order traversal** of its nodes' values. 
- Traverse nodes **column-wise** (left to right), and **top to bottom** within each column.
- Use **BFS**, not DFS, to maintain proper vertical and top-down order.

---

## ✅ Code (Java)

```java
class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();

        Map<Integer, List<Integer>> map = new TreeMap<>();
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        Queue<Integer> colQueue = new LinkedList<>();

        nodeQueue.offer(root);
        colQueue.offer(0);

        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.poll();
            int col = colQueue.poll();

            map.computeIfAbsent(col, k -> new ArrayList<>()).add(node.val);

            if (node.left != null) {
                nodeQueue.offer(node.left);
                colQueue.offer(col - 1);
            }

            if (node.right != null) {
                nodeQueue.offer(node.right);
                colQueue.offer(col + 1);
            }
        }

        return new ArrayList<>(map.values());
    }
}
````

---

## 🔍 Intuition

- We want to **group nodes by vertical column**, from left to right.
    
- For **top-to-bottom ordering**, we need **level order traversal** → BFS.
    
- Use:
    
    - A `Map<Integer, List<Integer>>` to group nodes by column
        
    - A `Queue<TreeNode>` to process nodes level-by-level
        
    - A `Queue<Integer>` to track the **column index** for each node
        

---

## ⚠️ DFS Won’t Work – Why?

DFS visits deep nodes **before** shallow ones on the same column.

Example:

```
      1
     / \
    2   3
     \
      4
       \
        5
```

DFS might process `5` before `3`, leading to `[5, 3]` in that column — which is incorrect.  
Correct order: `[3, 5]` → only achievable by **BFS**.

---

## 🧪 Example

```text
Input:
      3
     / \
    9   8
   / \ / \
  4  0 1  7

Output: [[4], [9], [3, 0, 1], [8], [7]]
```

---

## 🧮 Time & Space Complexity

- **Time:** `O(n)` — Each node is visited once
    
- **Space:** `O(n)` — For map and queues
    

---

## ✅ Notes

- TreeMap ensures **columns are sorted** (left to right)
    
- BFS ensures **top-to-bottom** order
    
- `computeIfAbsent()` simplifies map initialization
    

---
