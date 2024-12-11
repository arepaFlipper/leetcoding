# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        (root.left, root.right) = (root.right, root.left)

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def is_same_tree(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    return (node1.val == node2.val and
            is_same_tree(node1.left, node2.left) and
            is_same_tree(node1.right, node2.right))

solution = Solution()

# Test Case 1
input_tree_1 = TreeNode(4)
input_tree_1.left = TreeNode(2, TreeNode(1), TreeNode(3))
input_tree_1.right = TreeNode(7, TreeNode(6), TreeNode(9))

expected_output_1 = TreeNode(4)
expected_output_1.left = TreeNode(7, TreeNode(9), TreeNode(6))
expected_output_1.right = TreeNode(2, TreeNode(3), TreeNode(1))

result_1 = solution.invertTree(input_tree_1)

print("Test Case 1:")
print("Input:")
# Displaying tree values in breadth-first order
print([result.val for result in [input_tree_1]])

print("Output:")
print([result.val for result in [result_1]])

if is_same_tree(result_1, expected_output_1):
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_tree_2 = TreeNode(2, TreeNode(1), TreeNode(3))
expected_output_2 = TreeNode(2, TreeNode(3), TreeNode(1))

result_2 = solution.invertTree(input_tree_2)

print("\nTest Case 2:")
print("Input:")
print([result.val for result in [input_tree_2]])

print("Output:")
print([result.val for result in [result_2]])

if is_same_tree(result_2, expected_output_2):
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_tree_3 = None
expected_output_3 = None

result_3 = solution.invertTree(input_tree_3)

print("\nTest Case 3:")
print("Input: None")
print("Output: None")

if is_same_tree(result_3, expected_output_3):
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

