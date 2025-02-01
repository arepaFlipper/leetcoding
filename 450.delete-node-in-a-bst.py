# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
# @leet end
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minValueNode(self, root):
        current = root
        while current and current.left:
            current = current.left
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # This is where your solution will go.
        if not root: 
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right: # Here is a Tree of two nodes only and

                print('root.left:', root.left.val)
                return root.left # we want to remove the higher node (root).
                # Then it goes to the following statement using min_node.val
            else:
                min_node = self.minValueNode(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root

    # Helper functions
    @staticmethod
    def serialize_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
        """Converts a binary tree to a list representation."""
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing Nones for compact representation
        while result and result[-1] is None:
            result.pop()
        return result

    @staticmethod
    def deserialize_tree(data: List[Optional[int]]) -> Optional[TreeNode]:
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


# Test framework for Delete Node in a BST
def test_delete_node():
    test_cases = [
        {
            "root": [5, 3, 6, 2, 4, None, 7],
            "key": 3,
            "expected": [[5, 4, 6, 2, None, None, 7], [5, 2, 6, None, 4, None, 7]],
        },
        {
            "root": [5, 3, 6, 2, 4, None, 7],
            "key": 0,
            "expected": [[5, 3, 6, 2, 4, None, 7]],
        },
        {
            "root": [],
            "key": 0,
            "expected": [[]],
        },
        {
            "root": [1],
            "key": 1,
            "expected": [[]],
        },
        {
            "root": [2, 1, 3],
            "key": 3,
            "expected": [[2, 1]],
        },
        {
            "root": [2, 1, 3],
            "key": 2,
            "expected": [[3, 1]],
        },
        {
            "root": [2, 1],
            "key": 2,
            "expected": [[1]],
        },
        {
            "root": [5, 3, None, 2],
            "key": 3,
            "expected": [[5, 2]],  # Only one valid BST output in this case.
        },
    ]

    for i, test in enumerate(test_cases):
        root = Solution.deserialize_tree(test["root"])
        key = test["key"]
        expected_options = test["expected"]

        # Solution object
        solution = Solution()
        result_root = solution.deleteNode(root, key)
        result_list = Solution.serialize_tree(result_root)

        # Check if the result matches any expected option (multiple valid BSTs)
        if result_list in expected_options:
            print(f"Test case {i+1} passed! ✅")
        else:
            print(f"❌ Test case {i+1} failed: {result_list} not in {expected_options} 😭")


# Run tests
test_delete_node()

