from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other:
            return False
        return (
            self.val == other.val and
            self.left == other.left and
            self.right == other.right
        )

# @leet start
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

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
        
# @leet end

def serialize_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converts a binary tree to a list representation (level-order traversal)."""
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
    # Trim trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

def test_build_tree():
    test_cases = [
        # Example 1
        {
            "preorder": [3, 9, 20, 15, 7],
            "inorder": [9, 3, 15, 20, 7],
            "expected": [3, 9, 20, None, None, 15, 7]
        },
        # Example 2
        {
            "preorder": [-1],
            "inorder": [-1],
            "expected": [-1]
        },
        # Additional Test: Full binary tree
        {
            "preorder": [1, 2, 4, 5, 3, 6, 7],
            "inorder": [4, 2, 5, 1, 6, 3, 7],
            "expected": [1, 2, 3, 4, 5, 6, 7]
        },
        # Additional Test: Skewed tree (all left children)
        {
            "preorder": [1, 2, 3, 4],
            "inorder": [4, 3, 2, 1],
            "expected": [1, 2, None, 3, None, 4]
        },
        # Additional Test: Skewed tree (all right children)
        {
            "preorder": [1, 2, 3, 4],
            "inorder": [1, 2, 3, 4],
            "expected": [1, None, 2, None, 3, None, 4]
        },
        # Additional Test: Single-node tree
        {
            "preorder": [42],
            "inorder": [42],
            "expected": [42]
        }
    ]

    for i, test in enumerate(test_cases):
        solution = Solution()
        try:
            root = solution.buildTree(test["preorder"], test["inorder"])
            result = serialize_tree(root)
            assert result == test["expected"], f"Test case {i + 1} failed: Expected {test['expected']}, got {result}"
            print(f"Test case {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test case {i + 1} failed with error: {e} ❌")

# Run tests
if __name__ == "__main__":
    test_build_tree()

