# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        res = 1
        stack = [[root, res]]

        while stack:
            (node, depth) = stack.pop()

            if node:
                res = max(res,depth)
                stack.append([node.right, depth+1])
                stack.append([node.left, depth+1])

        return res

solution = Solution()

# Function to check if both trees are identical
def is_same_tree(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    return (node1.val == node2.val and
            is_same_tree(node1.left, node2.left) and
            is_same_tree(node1.right, node2.right))

# Test Case 1
input_tree_1 = TreeNode(3)
input_tree_1.left = TreeNode(9)
input_tree_1.right = TreeNode(20, TreeNode(15), TreeNode(7))

expected_output_1 = 3

result_1 = solution.maxDepth(input_tree_1)

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
input_tree_2 = TreeNode(1)
input_tree_2.right = TreeNode(2)

expected_output_2 = 2

result_2 = solution.maxDepth(input_tree_2)

print("\nTest Case 2:")
print("Input:")
print([result.val for result in [input_tree_2]])

print("Output:")
print(result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

