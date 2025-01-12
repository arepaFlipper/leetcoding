from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper functions
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

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
# @leet end
#
#
# Test framework for Insert into a BST
def test_insert_into_bst():
    test_cases = [
        {"root": [4, 2, 7, 1, 3], "val": 5, "expected": [[4, 2, 7, 1, 3, 5], [4, 2, 7, 1, 3, None, 5]]},
        {"root": [40, 20, 60, 10, 30, 50, 70], "val": 25, "expected": [[40, 20, 60, 10, 30, 50, 70, None, None, 25]]},
        {"root": [4, 2, 7, 1, 3, None, None, None, None, None, None], "val": 5, "expected": [[4, 2, 7, 1, 3, 5]]},
        {"root": [], "val": 10, "expected": [[10]]},  # Edge case: inserting into an empty tree
        {"root": [2], "val": 3, "expected": [[2, None, 3]]},  # Edge case: single-node tree
    ]

    for i, test in enumerate(test_cases):
        root = deserialize_tree(test["root"])
        val = test["val"]
        expected_options = test["expected"]

        # Solution object
        solution = Solution()
        result_root = solution.insertIntoBST(root, val)
        result_list = serialize_tree(result_root)

        # Check if the result matches any expected option (multiple valid BSTs)
        if result_list in expected_options:
            print(f"Test case {i+1} passed! ✅")
        else:
            print(f"❌ Test case {i+1} failed: {result_list} not in {expected_options} 😭")

# Run tests
test_insert_into_bst()

