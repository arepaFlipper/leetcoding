# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]

solution = Solution()

# Test Case 1
input_tree_1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
expected_output_1 = 3

result_1 = solution.diameterOfBinaryTree(input_tree_1)

print("Test Case 1:")
print("Input:")
# Displaying tree values in breadth-first order
print([result.val for result in [input_tree_1]])

print("Output:")
print(result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_tree_2 = TreeNode(1, TreeNode(2))
expected_output_2 = 1

result_2 = solution.diameterOfBinaryTree(input_tree_2)

print("\nTest Case 2:")
print("Input:")
print([result.val for result in [input_tree_2]])

print("Output:")
print(result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

