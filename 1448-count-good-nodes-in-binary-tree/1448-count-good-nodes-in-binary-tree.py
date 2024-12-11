# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def depth_first_search(node, max_val):
            if not node:
                return 0
            
            res = 1 if node.val >= max_val else 0
            max_val = max(node.val,max_val)
            res += depth_first_search(node.right, max_val)
            res += depth_first_search(node.left, max_val)
            return res
        
        return depth_first_search(root, root.val)


solution = Solution()

# Test Case 1
input_tree_1_root = TreeNode(3)
input_tree_1_root.left = TreeNode(3)
input_tree_1_root.right = TreeNode(0) # append 0 instead of None
input_tree_1_root.right.left = TreeNode(4)
input_tree_1_root.right.right = TreeNode(2)
expected_output_1 = 3

result_1 = solution.goodNodes(input_tree_1_root)

print("\nTest Case 1:")
print("Input:")
# Displaying the corrected tree structure
print("   3")
print("  / \\")
print(" 3  None")
print("    / \\")
print("   4   2")

print("Output:")
print(result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_tree_2_root = TreeNode(3)
input_tree_2_root.left = TreeNode(3)
input_tree_1_root.right = TreeNode(0) # append 0 instead of None
input_tree_2_root.right.left = TreeNode(4)
input_tree_2_root.right.right = TreeNode(2)
expected_output_2 = 3

result_2 = solution.goodNodes(input_tree_2_root)

print("\nTest Case 2:")
print("Input:")
# Displaying the tree structure
print("3")
print("|_ 3")
print("|_ None")
print("   |_ 4")
print("   |_ 2")

print("Output:")
print(result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_tree_3_root = TreeNode(1)
expected_output_3 = 1

result_3 = solution.goodNodes(input_tree_3_root)

print("\nTest Case 3:")
print("Input:")
# Displaying the tree structure
print("1")

print("Output:")
print(result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

