# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            is_balanced = (left[0] and right[0] and (abs(left[1] - right[1]) <= 1))
            
            return (is_balanced, 1 + max(left[1], right[1]))
        return dfs(root)[0]

solution = Solution()

# Test Case 1
input_tree_1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
expected_output_1 = True

result_1 = solution.isBalanced(input_tree_1)

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
input_tree_2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)))
expected_output_2 = False

result_2 = solution.isBalanced(input_tree_2)

print("\nTest Case 2:")
print("Input:")
print([result.val for result in [input_tree_2]])

print("Output:")
print(result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_tree_3 = None
expected_output_3 = True

result_3 = solution.isBalanced(input_tree_3)

print("\nTest Case 3:")
print("Input: Empty tree")
print("Output:")
print(result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

