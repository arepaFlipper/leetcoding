I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

  105. Construct Binary Tree from Preorder and Inorder Traversal  
  Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.  
     
  Example 1:  
  https://assets.leetcode.com/uploads/2021/02/19/tree.jpg  
  Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]  
  Output: [3,9,20,null,null,15,7]  
  Example 2:  
  Input: preorder = [-1], inorder = [-1]  
  Output: [-1]  
     
  Constraints:  
  	1 <= preorder.length <= 3000  
  	inorder.length == preorder.length  
  	-3000 <= preorder[i], inorder[i] <= 3000  
  	preorder and inorder consist of unique values.  
  	Each value of inorder also appears in preorder.  
  	preorder is guaranteed to be the preorder traversal of the tree.  
  	inorder is guaranteed to be the inorder traversal of the tree.  


The following is my solution to test:
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # The first value on Preorder traversal is the root
        root = TreeNode(preorder[0])

        # Find the root value inorder list
        middle_idx = inorder.index(preorder[0])
        # values after the middle_idx index are nodes from the left subtree

        # Recursive
        root.left = self.buildTree(preorder[1:middle_idx+1], inorder[:middle_idx])
        root.right = self.buildTree(preorder[middle_idx+1:], inorder[middle_idx+1:])
        return root
        
# Preorder traversal: it takes the node's value from left "←" position (red)
# Inorder traversal: it takes the node's value from down "↓" direction (green)
```
