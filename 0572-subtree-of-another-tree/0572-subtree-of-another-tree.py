# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.is_same_tree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

solution = Solution()

# Test Case 1
input_tree_1_root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
input_tree_1_subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
expected_output_1 = True

result_1 = solution.isSubtree(input_tree_1_root, input_tree_1_subRoot)

print("Test Case 1:")
print("Input:")
# Displaying tree values in breadth-first order
print([result.val for result in [input_tree_1_root]])
print([result.val for result in [input_tree_1_subRoot]])

print("Output:")
print(result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_tree_2_root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5, None, TreeNode(0)))
input_tree_2_subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
expected_output_2 = True

result_2 = solution.isSubtree(input_tree_2_root, input_tree_2_subRoot)

print("\nTest Case 2:")
print("Input:")
print([result.val for result in [input_tree_2_root]])
print([result.val for result in [input_tree_2_subRoot]])

print("Output:")
print(result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

