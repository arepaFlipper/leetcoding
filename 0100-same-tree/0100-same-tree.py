# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

solution = Solution()

# Test Case 1
input_tree_1_p = TreeNode(1, TreeNode(2), TreeNode(3))
input_tree_1_q = TreeNode(1, TreeNode(2), TreeNode(3))
expected_output_1 = True

result_1 = solution.isSameTree(input_tree_1_p, input_tree_1_q)

print("Test Case 1:")
print("Input:")
# Displaying tree values in breadth-first order
print([result.val for result in [input_tree_1_p]])
print([result.val for result in [input_tree_1_q]])

print("Output:")
print(result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_tree_2_p = TreeNode(1, TreeNode(2), None)
input_tree_2_q = TreeNode(1, None, TreeNode(2))
expected_output_2 = False

result_2 = solution.isSameTree(input_tree_2_p, input_tree_2_q)

print("\nTest Case 2:")
print("Input:")
print([result.val for result in [input_tree_2_p]])
print([result.val for result in [input_tree_2_q]])

print("Output:")
print(result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_tree_3_p = TreeNode(1, TreeNode(2), TreeNode(1))
input_tree_3_q = TreeNode(1, TreeNode(1), TreeNode(2))
expected_output_3 = False

result_3 = solution.isSameTree(input_tree_3_p, input_tree_3_q)

print("\nTest Case 3:")
print("Input:")
print([result.val for result in [input_tree_3_p]])
print([result.val for result in [input_tree_3_q]])

print("Output:")
print(result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

