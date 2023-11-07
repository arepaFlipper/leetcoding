I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

  572. Subtree of Another Tree  
  Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.  
  A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.  
     
  Example 1:  
  https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg  
  Input: root = [3,4,5,1,2], subRoot = [4,1,2]  
  Output: true  
  Example 2:  
  https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg  
  Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]  
  Output: false  
     
  Constraints:  
  	The number of nodes in the root tree is in the range [1, 2000].  
  	The number of nodes in the subRoot tree is in the range [1, 1000].  
  	-104 <= root.val <= 104  
  	-104 <= subRoot.val <= 104  

The following is my solution to test:

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.is_same_tree(root,subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right))
        
        return False

```

