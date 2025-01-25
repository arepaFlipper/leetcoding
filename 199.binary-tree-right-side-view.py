from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postOrder(root, res)
        res.sort()
        return res

    def postOrder(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        if root is not None:
            self.postOrder(root.left, res)
            self.postOrder(root.right, res)
            res.append(root.val)


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

def test_right_side_view():
    test_cases = [
        # Example 1
        {"root": [1, 2, 3, None, 5, None, 4], "expected": [1, 3, 4]},
        # Example 2
        {"root": [1, 2, 3, 4, None, None, None, 5], "expected": [1, 3, 4, 5]},
        # Example 3
        {"root": [1, None, 3], "expected": [1, 3]},
        # Example 4: Empty tree
        {"root": [], "expected": []},
        # Additional Test: Single-node tree
        {"root": [1], "expected": [1]},
        # Additional Test: Full binary tree
        {"root": [1, 2, 3, 4, 5, 6, 7], "expected": [1, 3, 7]},
        # Additional Test: Skewed tree with only left children
        {"root": [1, 2, None, 3, None, 4], "expected": [1, 2, 3, 4]},
        # Additional Test: Skewed tree with only right children
        {"root": [1, None, 2, None, 3, None, 4], "expected": [1, 2, 3, 4]},
        # Additional Test: Tree with mixed left and right children
        {"root": [1, 2, 3, None, 5, 6, 7, None, None, None, 8], "expected": [1, 3, 7, 8]},
    ]

    for i, test in enumerate(test_cases):
        # Deserialize the tree
        solution = Solution()
        root = solution.deserialize_tree(test["root"])
        
        # Call the user's rightSideView function
        try:
            result = solution.rightSideView(root)
            assert result == test["expected"], f"Test case {i + 1} failed: Expected {test['expected']}, got {result}"
            print(f"Test case {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test case {i + 1} failed with error: {e} ❌")

# Run tests
if __name__ == "__main__":
    test_right_side_view()

