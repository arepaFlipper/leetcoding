# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def depth_first_search(current_node: Optional[TreeNode]):
            if not current_node:
                return 0
            max_left = depth_first_search(current_node.left)
            max_right = depth_first_search(current_node.right)

            # prevents from summing negative values
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)

            res[0] = max(res[0], max_left + current_node.val + max_right)
            max_from_cur = current_node.val + max(max_left, max_right)
            return max_from_cur

        depth_first_search(root)
        return res[0]

def build_tree_from_array(arr):
    if not arr:
        return None
    
    nodes = [None if val is None else TreeNode(val) for val in arr]
    
    root = nodes[0]
    queue = [root]
    i = 1
    
    while i < len(nodes):
        current = queue.pop(0)
        
        if current is not None:
            current.left = nodes[i]
            i += 1
            queue.append(current.left)
            
            if i < len(nodes):
                current.right = nodes[i]
                i += 1
                queue.append(current.right)
    
    return root

solution = Solution()

# Test Case 1
input_tree_1 = TreeNode(1)
input_tree_1.left = TreeNode(2)
input_tree_1.right = TreeNode(3)
expected_output_1 = 6
result_1 = solution.maxPathSum(input_tree_1)
print("Test Case 1:")
print("Input:")
# Displaying the corrected tree structure
#   1
#  / \
# 2   3
print("Output:", result_1)
if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_tree_2 = TreeNode(-10)
input_tree_2.left = TreeNode(9)
input_tree_2.right = TreeNode(20)
input_tree_2.right.left = TreeNode(15)
input_tree_2.right.right = TreeNode(7)
expected_output_2 = 42
result_2 = solution.maxPathSum(input_tree_2)
print("\nTest Case 2:")
print("Input:")
# Displaying the corrected tree structure
#     -10
#     / \
#    9  20
#      /  \
#     15   7
print("Output:", result_2)
if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

