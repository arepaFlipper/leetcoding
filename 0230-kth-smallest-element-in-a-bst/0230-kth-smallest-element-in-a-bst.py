# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            current = current.right

solution = Solution()

# Test Case 1
input_tree_1_root = TreeNode(3)
input_tree_1_root.left = TreeNode(1)
input_tree_1_root.right = TreeNode(4)
input_tree_1_root.left.right = TreeNode(2)
expected_output_1 = 1

result_1 = solution.kthSmallest(input_tree_1_root, 1)

print("Test Case 1:")
print("Input:")
# Displaying the corrected tree structure
print("   3")
print("  / \\")
print(" 1   4")
print("  \\")
print("   2")

print("Output:")
print(result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_tree_2_root = TreeNode(5)
input_tree_2_root.left = TreeNode(3)
input_tree_2_root.right = TreeNode(6)
input_tree_2_root.left.left = TreeNode(2)
input_tree_2_root.left.right = TreeNode(4)
input_tree_2_root.left.left.left = TreeNode(1)
expected_output_2 = 3

result_2 = solution.kthSmallest(input_tree_2_root, 3)

print("\nTest Case 2:")
print("Input:")
# Displaying the corrected tree structure
print("   5")
print("  / \\")
print(" 3   6")
print(" / \\")
print("2   4")
print("/")
print("1")

print("Output:")
print(result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

