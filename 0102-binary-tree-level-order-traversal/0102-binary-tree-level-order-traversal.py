# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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

solution = Solution()

# Test Case 1
input_tree_1_root = TreeNode(3)
input_tree_1_root.left = TreeNode(9)
input_tree_1_root.right = TreeNode(20)
input_tree_1_root.right.left = TreeNode(15)
input_tree_1_root.right.right = TreeNode(7)
expected_output_1 = [[3], [9, 20], [15, 7]]

result_1 = solution.levelOrder(input_tree_1_root)

print("Test Case 1:")
print("Input:")
print([result.val for result in [input_tree_1_root]])

print("Output:")
print(result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_tree_2_root = TreeNode(1)
expected_output_2 = [[1]]

result_2 = solution.levelOrder(input_tree_2_root)

print("\nTest Case 2:")
print("Input:")
print([result.val for result in [input_tree_2_root]])

print("Output:")
print(result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_tree_3_root = None
expected_output_3 = []

result_3 = solution.levelOrder(input_tree_3_root)

print("\nTest Case 3:")
print("Input:")
print(input_tree_3_root)

print("Output:")
print(result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

