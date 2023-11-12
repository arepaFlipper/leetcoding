I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:


  199. Binary Tree Right Side View  
  Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.  
     
  Example 1:  
  https://assets.leetcode.com/uploads/2021/02/14/tree.jpg  
  Input: root = [1,2,3,null,5,null,4]  
  Output: [1,3,4]  
  Example 2:  
  Input: root = [1,null,3]  
  Output: [1,3]  
  Example 3:  
  Input: root = []  
  Output: []  
     
  Constraints:  
  	The number of nodes in the tree is in the range [0, 100].  
  	-100 <= Node.val <= 100  

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])
        
        while queue:
            right_side = None
            queue_length = len(queue)

            for idx in range(queue_length):
                node = queue.popleft()
                if node:
                    right_side = node
                    queue.append(node.left)
                    queue.append(node.right)

            if right_side:
                res.append(right_side.val)

        return res
```
