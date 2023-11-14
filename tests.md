I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:


  98. Validate Binary Search Tree  
  Given the root of a binary tree, determine if it is a valid binary search tree (BST).  
  A valid BST is defined as follows:  
  	The left subtree of a node contains only nodes with keys less than the node's key.  
  	The right subtree of a node contains only nodes with keys greater than the node's key.  
  	Both the left and right subtrees must also be binary search trees.  
     
  Example 1:  
  https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg  
  Input: root = [2,1,3]  
  Output: true  
  Example 2:  
  https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg  
  Input: root = [5,1,4,null,null,3,6]  
  Output: false  
  Explanation: The root node's value is 5 but its right child's value is 4.  
     
  Constraints:  
  	The number of nodes in the tree is in the range [1, 104].  
  	-231 <= Node.val <= 231 - 1  

The following is my solution to test:
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], link: int, recht: int) -> bool:
            if not node:
                return True
            
            if not(link < node.val < recht):
                return False
            
            return validate(node.left,link,node.val) and validate(node.right, node.val, recht)
        
        return validate(root, float('-INF'),float('INF'))
```
