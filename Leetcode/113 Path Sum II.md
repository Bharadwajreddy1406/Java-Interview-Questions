
# LeetCode 113: Path Sum II

#### Problem Statement:

Given a binary tree and a target sum, find all root-to-leaf paths where each path's sum equals the given target sum.

#### Example:

**Example 1:**

```
Input: 
	    5
	   / \
	  4   8
	 /   / \
	11  13  4
    /  \     \
   7    2    1

Target = 22
Output: 
[
  [5,4,11,2],
  [5,8,4,5]
]
```

**Example 2:**

```
Input: 
   1
  / \
 2   3

Target = 3
Output: 
[[1,2]]
```

#### Constraints:

- The tree will have at most 1000 nodes.
    
- The values of nodes can range between `-1000` to `1000`.
    
- The target sum is between `1` and `1000`.
    

#### Approach & Intuition:

1. **Backtracking Approach**:
    
    - This problem can be solved using **backtracking** to explore all paths from the root to each leaf node.
        
    - The main idea is to maintain the current sum of the path and check if it equals the target when a leaf node is reached.
        
2. **Recursive Steps**:
    
    - **Base Case**: If the current node is `null`, we return as there are no more nodes to explore.
        
    - **Path Construction**: As we traverse, we accumulate the node values in a list (`curr`).
        
    - **Leaf Check**: Once we reach a leaf node (both left and right children are `null`), we check if the accumulated sum matches the target (`sum == target`).
        
    - **Backtrack**: After exploring both left and right subtrees, we remove the current node from the path list to explore other possible paths.
        
3. **Edge Case**: If there is no path that matches the target, the result should be an empty list.
    

#### Code:

```java
class Solution {
    public void back(List<List<Integer>> ans, List<Integer> curr, int sum, TreeNode root, int k) {
        if (root == null) return;

        sum += root.val;  // Update the sum as we traverse

        curr.add(root.val);  // Add the current node value to the path

        // Check if we have reached a leaf node and the sum equals the target
        if (root.left == null && root.right == null && sum == k) {
            ans.add(new ArrayList<>(curr));  // Add the current path to the result
        } else {
            // Recurse on left and right children
            back(ans, curr, sum, root.left, k);
            back(ans, curr, sum, root.right, k);
        }

        // Backtrack by removing the current node from the path
        curr.remove(curr.size() - 1);
    }

    public List<List<Integer>> pathSum(TreeNode root, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();

        back(ans, curr, 0, root, target);  // Start the backtracking from the root
        return ans;
    }
}
```

#### Explanation:

- **Function**: `back(List<List<Integer>> ans, List<Integer> curr, int sum, TreeNode root, int k)`
    
    - `ans`: Stores the final list of paths that sum up to `k`.
        
    - `curr`: Keeps track of the current path being explored.
        
    - `sum`: Accumulated sum of the current path.
        
    - `root`: Current node in the tree.
        
    - `k`: Target sum to be matched.
        
- **Base Case**: If the `root` is `null`, return.
    
- **Leaf Node Check**: If a leaf node is reached and the `sum` equals the target (`k`), the current path (`curr`) is added to the answer list.
    
- **Recursive Call**: Explore the left and right children of the current node recursively.
    
- **Backtracking**: After exploring both subtrees, we remove the last node in the current path (`curr`) to backtrack and try other paths.
    

#### Complexity Analysis:

- **Time Complexity**: `O(N)`, where `N` is the number of nodes in the tree. We visit each node once.
    
- **Space Complexity**: `O(H)`, where `H` is the height of the tree, as the recursion stack can go as deep as the height of the tree and the path list stores nodes along the current path.
    

#### Key Takeaways:

- **Backtracking** is useful for problems involving paths in a tree or graph, where we need to explore all possible paths from start to end.
    
- **Path Accumulation**: We accumulate the current path and check if it meets the target sum.
    
- **Leaf Node Condition**: It's important to check if a node is a leaf before validating the sum condition.
    
---
