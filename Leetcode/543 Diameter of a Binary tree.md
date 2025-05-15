# LeetCode 543 – Diameter of Binary Tree

**Link:** [LeetCode 543](https://leetcode.com/problems/diameter-of-binary-tree/)

---

## 🧠 Problem Statement

The **diameter** of a binary tree is the length of the **longest path** between any two nodes in the tree.  
This path **may or may not pass through the root**.

> The length of a path is the number of **edges** between the nodes.

---

## ✅ Code (Java – Post-order DFS)

```java
class Solution {

    public int findmax(TreeNode root, int[] max){
        if (root == null) return 0;

        int lh = findmax(root.left, max);
        int rh = findmax(root.right, max);

        max[0] = Math.max(max[0], lh + rh); // Update max path through current node

        return 1 + Math.max(lh, rh); // Return height of the subtree
    }

    public int diameterOfBinaryTree(TreeNode root) {
        int[] max = new int[]{0};
        findmax(root, max);
        return max[0];
    }
}
````

---

## 🔍 Intuition

- At **every node**, the potential diameter is:
    
    ```
    height(left subtree) + height(right subtree)
    ```
    
- We calculate the **height** of the subtree recursively.
    
- While doing so, we keep track of the **maximum diameter** seen so far using `max[0]`.
    

---

## 💡 Notes

- We are calculating diameter in a **single DFS traversal**.
    
- This avoids recomputation and makes it **efficient**.
    
- We use an array `max[0]` to store the result across recursive calls.
    

---

## 🧮 Time & Space Complexity

- **Time:** O(n) – Every node is visited once.
    
- **Space:** O(h) – Recursion stack space, where `h` is the height of the tree.
    

---

## ✅ Test Cases

```text
Input: [1,2,3,4,5]
Tree:
       1
      / \
     2   3
    / \
   4   5
Output: 3
Explanation: Path = 4 → 2 → 1 → 3

Input: [1,2]
Output: 1

Input: [1]
Output: 0
```

---

## 🌳 Traversal Strategy

- Use **post-order DFS**:
    
    - Process left → right → node.
        
    - At each node, calculate left and right subtree heights.
        
    - Update max diameter with `left + right`.
        
    - Return `1 + max(left, right)` to caller.
        

---

