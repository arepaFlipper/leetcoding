# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root, res):
        if root is not None:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)

    def deserialize_tree(self, data: List[Optional[int]]) -> Optional[TreeNode]:
        """Converts a list representation to a binary tree."""
        if not data:
            return None
        root = TreeNode(data[0])
        queue = [root]
        i = 1
        while queue and i < len(data):
            node = queue.pop(0)
            if node:
                if i < len(data) and data[i] is not None:
                    node.left = TreeNode(data[i])
                    queue.append(node.left)
                i += 1
                if i < len(data) and data[i] is not None:
                    node.right = TreeNode(data[i])
                    queue.append(node.right)
                i += 1
        return root


# @leet end
#
def test_inorder_traversal():
    test_cases = [
        # Example 1
        {"root": [1, None, 2, 3], "expected": [1, 3, 2]},
        # Example 2
        {"root": [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], "expected": [4, 2, 6, 5, 7, 1, 3, 9, 8]},
        # Example 3: Empty tree
        {"root": [], "expected": []},
        # Example 4: Single-node tree
        {"root": [1], "expected": [1]},
        # Additional Test: Perfect binary tree
        {"root": [1, 2, 3, 4, 5, 6, 7], "expected": [4, 2, 5, 1, 6, 3, 7]},
        # Additional Test: Left-skewed tree
        {"root": [4, 3, None, 2, None, 1], "expected": [1, 2, 3, 4]},
        # Additional Test: Right-skewed tree
        {"root": [1, None, 2, None, 3, None, 4], "expected": [1, 2, 3, 4]},
    ]

    for i, test in enumerate(test_cases):
        # Deserialize tree
        solution = Solution()
        root = solution.deserialize_tree(test["root"])
        
        # Call the user's inorder traversal method
        result = Solution().inorderTraversal(root)
        
        # Compare results
        if result == test["expected"]:
            print(f"Test case {i + 1} passed! ✅")
        else:
            print(f"Test case {i + 1} failed: Expected {test['expected']}, got {result} ❌")

# Run tests
test_inorder_traversal()

