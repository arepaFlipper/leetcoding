I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:



  102. Binary Tree Level Order Traversal  
  Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).  
     
  Example 1:  
  https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg  
  Input: root = [3,9,20,null,null,15,7]  
  Output: [[3],[9,20],[15,7]]  
  Example 2:  
  Input: root = [1]  
  Output: [[1]]  
  Example 3:  
  Input: root = []  
  Output: []  
     
  Constraints:  
  	The number of nodes in the tree is in the range [0, 2000].  
  	-1000 <= Node.val <= 1000  


The following is my solution to test:

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            queue_length = len(queue)
            level = []
            for i in range(queue_length):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res
```
