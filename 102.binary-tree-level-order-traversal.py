from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()

        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            print("level: ", level, " 👈")
            current_level = []
            for idx in range(len(queue)):
                current = queue.popleft()
                print("value: ",current.val, " 🖋️")
                current_level.append(current.val)
                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            if current_level:
                res.append(current_level)
            level +=1
        return res



        
# @leet end

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order list representation."""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

def test_level_order():
    test_cases = [
        # Example 1
        {
            "input": [3, 9, 20, None, None, 15, 7],
            "expected": [[3], [9, 20], [15, 7]]
        },
        # Example 2
        {
            "input": [1],
            "expected": [[1]]
        },
        # Example 3
        {
            "input": [],
            "expected": []
        },
        # Additional Test: Full binary tree
        {
            "input": [1, 2, 3, 4, 5, 6, 7],
            "expected": [[1], [2, 3], [4, 5, 6, 7]]
        },
        # Additional Test: Skewed left tree
        {
            "input": [1, 2, None, 3, None, 4],
            "expected": [[1], [2], [3], [4]]
        },
        # Additional Test: Skewed right tree
        {
            "input": [1, None, 2, None, 3, None, 4],
            "expected": [[1], [2], [3], [4]]
        },
        # Additional Test: Mixed nulls
        {
            "input": [1, 2, 3, None, 4, None, 5],
            "expected": [[1], [2, 3], [4, 5]]
        }
    ]

    for i, test in enumerate(test_cases):
        solution = Solution()
        try:
            root = build_tree(test["input"])
            result = solution.levelOrder(root)
            assert result == test["expected"], f"Test case {i + 1} failed: Expected {test['expected']}, got {result}"
            print(f"Test case {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test case {i + 1} failed with error: {e} ❌")

# Run tests
if __name__ == "__main__":
    test_level_order()


