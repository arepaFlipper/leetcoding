# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        current = root
        while current:
            if (p.val > current.val) and (q.val > current.val):
                current = current.right
            elif (p.val < current.val) and (q.val < current.val):
                current = current.left
            else:
                return current

solution = Solution()

# Test Case 1
input_tree_1_root = TreeNode(6)
input_tree_1_root.left = TreeNode(2)
input_tree_1_root.right = TreeNode(8)
input_tree_1_root.left.left = TreeNode(0)
input_tree_1_root.left.right = TreeNode(4)
input_tree_1_root.right.left = TreeNode(7)
input_tree_1_root.right.right = TreeNode(9)
input_tree_1_root.left.right.left = TreeNode(3)
input_tree_1_root.left.right.right = TreeNode(5)
input_tree_1_p = input_tree_1_root.left
input_tree_1_q = input_tree_1_root.right
expected_output_1 = input_tree_1_root

result_1 = solution.lowestCommonAncestor(input_tree_1_root, input_tree_1_p, input_tree_1_q)

print("Test Case 1:")
print("Input:")
print([result.val for result in [input_tree_1_root]])
print(f"p: {input_tree_1_p.val}, q: {input_tree_1_q.val}")

print("Output:")
print(result_1.val)

if result_1.val == expected_output_1.val:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_tree_2_root = TreeNode(6)
input_tree_2_root.left = TreeNode(2)
input_tree_2_root.right = TreeNode(8)
input_tree_2_root.left.left = TreeNode(0)
input_tree_2_root.left.right = TreeNode(4)
input_tree_2_root.right.left = TreeNode(7)
input_tree_2_root.right.right = TreeNode(9)
input_tree_2_root.left.right.left = TreeNode(3)
input_tree_2_root.left.right.right = TreeNode(5)
input_tree_2_p = input_tree_2_root.left
input_tree_2_q = input_tree_2_root.left.right
expected_output_2 = input_tree_2_p

result_2 = solution.lowestCommonAncestor(input_tree_2_root, input_tree_2_p, input_tree_2_q)

print("\nTest Case 2:")
print("Input:")
print([result.val for result in [input_tree_2_root]])
print(f"p: {input_tree_2_p.val}, q: {input_tree_2_q.val}")

print("Output:")
print(result_2.val)

if result_2.val == expected_output_2.val:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_tree_3_root = TreeNode(2)
input_tree_3_root.left = TreeNode(1)
input_tree_3_p = input_tree_3_root
input_tree_3_q = input_tree_3_root.left
expected_output_3 = input_tree_3_root

result_3 = solution.lowestCommonAncestor(input_tree_3_root, input_tree_3_p, input_tree_3_q)

print("\nTest Case 3:")
print("Input:")
print([result.val for result in [input_tree_3_root]])
print(f"p: {input_tree_3_p.val}, q: {input_tree_3_q.val}")

print("Output:")
print(result_3.val)

if result_3.val == expected_output_3.val:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

