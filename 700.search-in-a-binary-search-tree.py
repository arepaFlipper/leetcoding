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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)

        if val == root.val:
            return root


# Test framework for Search in a BST
def test_search_in_bst():
    test_cases = [
        {"root": [4, 2, 7, 1, 3], "val": 2, "expected": [2, 1, 3]},
        {"root": [4, 2, 7, 1, 3], "val": 5, "expected": []},
        {"root": [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13], "val": 6, "expected": [6, 4, 7]},
        {"root": [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13], "val": 13, "expected": [13]},
        {"root": [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13], "val": 15, "expected": []},
        {"root": [4], "val": 4, "expected": [4]},  # Single node tree
        {"root": [4], "val": 2, "expected": []},  # Single node, non-matching value
    ]

    for i, test in enumerate(test_cases):
        root = deserialize_tree(test["root"])
        val = test["val"]
        expected = test["expected"]

        # Solution object
        solution = Solution()
        result = solution.searchBST(root, val)
        result_list = serialize_tree(result)

        # Validate results
        assert result_list == expected, f"❌ Test case {i+1} failed: {result_list} != {expected} 😭"
        print(f"Test case {i+1} passed! ✅")

# Run tests
test_search_in_bst()

