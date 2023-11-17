I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

  124. Binary Tree Maximum Path Sum  
  A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.  
  The path sum of a path is the sum of the node's values in the path.  
  Given the root of a binary tree, return the maximum path sum of any non-empty path.  
     
  Example 1:  
  https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg  
  Input: root = [1,2,3]  
  Output: 6  
  Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.  
  Example 2:  
  https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg  
  Input: root = [-10,9,20,null,null,15,7]  
  Output: 42  
  Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.  
     
  Constraints:  
  	The number of nodes in the tree is in the range [1, 3 * 104].  
  	-1000 <= Node.val <= 1000  


The following is my solution to test:
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def depth_first_search(current_node: Optional[TreeNode]):
            if not current_node:
                return 0
            max_left = depth_first_search(current_node.left)
            max_right = depth_first_search(current_node.right)

            # prevents from sum negative values
            max_left = max(max_left,0)
            max_right= max(max_right,0)

            res[0] = max(res[0], max_left + current_node.val + max_right)
            max_from_cur = current_node.val + max(max_left,max_right)
            return max_from_cur

        depth_first_search(root)
        return res[0]
```
