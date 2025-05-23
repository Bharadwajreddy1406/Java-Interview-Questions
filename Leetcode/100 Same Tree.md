# LeetCode 100 – Same Tree

**Link:** [https://leetcode.com/problems/same-tree](https://leetcode.com/problems/same-tree)  
**Tags:** Tree, DFS, Recursion

---

## 🧠 Problem Statement

Given two binary trees `p` and `q`, return `true` **if they are structurally identical and the nodes have the same value**, otherwise return `false`.

---

## ✅ Code (Java – Recursive DFS)

```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;

        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
````

---

## 🔍 Intuition

To check if two trees are the same, we:

1. Compare current nodes: `p.val == q.val`
    
2. Recursively compare left children
    
3. Recursively compare right children
    

We return false **immediately** if:

- One node is `null` and the other isn't.
    
- The values at the current nodes differ.
    

---

## 🧮 Time & Space Complexity

- **Time Complexity:** `O(n)`
    
    - `n` = number of nodes in the smaller of the two trees
        
- **Space Complexity:** `O(h)`
    
    - `h` = height of the tree (recursion stack)
        

---

## ✅ Example

```text
Tree 1:       Tree 2:
   1             1
  / \           / \
 2   3         2   3

=> Output: true

Tree 1:       Tree 2:
   1             1
  /               \
 2                 2

=> Output: false (structure mismatch)
```

---

## 📝 Notes

- Base case: both nodes null → true
    
- One null → false
    
- Values not equal → false
    
- Recurse on both left and right subtrees
    

---
