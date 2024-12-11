# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def tree_to_list(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.tree_to_list(root.left) + self.tree_to_list(root.right)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # The first value on Preorder traversal is the root
        root = TreeNode(preorder[0])

        # Find the root value in the inorder list
        middle_idx = inorder.index(preorder[0])
        # Values after the middle_idx index are nodes from the left subtree

        # Recursive
        root.left = self.buildTree(preorder[1:middle_idx + 1], inorder[:middle_idx])
        root.right = self.buildTree(preorder[middle_idx + 1:], inorder[middle_idx + 1:])
        return root

solution = Solution()

# Test Case 1
input_preorder_1 = [3, 9, 20, 15, 7]
input_inorder_1 = [9, 3, 15, 20, 7]
expected_output_1 = [3, 9, 20, None, None, 15, 7]

result_1 = solution.buildTree(input_preorder_1, input_inorder_1)

print("Test Case 1:")
print("Input:")
print("Preorder:", input_preorder_1)
print("Inorder:", input_inorder_1)

print("Output:")
print(solution.tree_to_list(result_1))

if solution.tree_to_list(result_1) == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_preorder_2 = [-1]
input_inorder_2 = [-1]
expected_output_2 = [-1]

result_2 = solution.buildTree(input_preorder_2, input_inorder_2)

print("\nTest Case 2:")
print("Input:")
print("Preorder:", input_preorder_2)
print("Inorder:", input_inorder_2)

print("Output:")
print(solution.tree_to_list(result_2))

if solution.tree_to_list(result_2) == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

