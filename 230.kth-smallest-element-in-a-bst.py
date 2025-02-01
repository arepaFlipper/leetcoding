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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            n += 1

            if n == k:
                return current.val
            else:
                current = current.right

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

def test_kth_smallest():
    test_cases = [
        # Example 1
        {"root": [3, 1, 4, None, 2], "k": 1, "expected": 1},
        # # Example 2
        {"root": [5, 3, 6, 2, 4, None, None, 1], "k": 3, "expected": 3},
        # # Example 3: Additional Test: Single-node tree
        {"root": [1], "k": 1, "expected": 1},
        # NOTE: Example 4:-Additional Test: Complete binary tree
        {"root": [3, 1, 4], "k": 2, "expected": 3},
        # NOTE: Example 5: Additional Test: Skewed tree with only left children
        {"root": [4, 3, None, 2, None, 1], "k": 3, "expected": 3},
        # NOTE: Example 6: Additional Test: Skewed tree with only right children
        {"root": [1, None, 2, None, 3, None, 4], "k": 4, "expected": 4},
        # NOTE: Example 7: Additional Test: Large tree to test efficiency
        {"root": list(range(1, 101)), "k": 50, "expected": 44},  # Tree with nodes from 1 to 100
    ]

    for i, test in enumerate(test_cases):
        # Deserialize tree
        solution = Solution()
        root = solution.deserialize_tree(test["root"])
        
        # Call the user's kth smallest function
        result = Solution().kthSmallest(root, test["k"])
        
        # Compare results
        if result == test["expected"]:
            print(f"Test case {i + 1} passed! ✅")
            print(" ")
            print(" ")
        else:
            print(f"Test case {i + 1} failed: Expected {test['expected']}, got {result} ❌")

# Run tests
test_kth_smallest()

# @leet end
