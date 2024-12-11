# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], left: int, right: int) -> bool:
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return validate(node.left, left, node.val) and validate(node.right, node.val, right)
        
        return validate(root, float('-INF'), float('INF'))

solution = Solution()

# Test Case 1
input_tree_1_root = TreeNode(2)
input_tree_1_root.left = TreeNode(1)
input_tree_1_root.right = TreeNode(3)
expected_output_1 = True

result_1 = solution.isValidBST(input_tree_1_root)

print("Test Case 1:")
print("Input:")
# Displaying the corrected tree structure
print("   2")
print("  / \\")
print(" 1   3")

print("Output:")
print(result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_tree_2_root = TreeNode(5)
input_tree_2_root.left = TreeNode(1)
input_tree_2_root.right = TreeNode(4)
input_tree_2_root.right.left = TreeNode(3)
input_tree_2_root.right.right = TreeNode(6)
expected_output_2 = False

result_2 = solution.isValidBST(input_tree_2_root)

print("\nTest Case 2:")
print("Input:")
# Displaying the corrected tree structure
print("   5")
print("  / \\")
print(" 1   4")
print("    / \\")
print("   3   6")

print("Output:")
print(result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

