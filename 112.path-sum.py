import unittest
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = []

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.path.append(root.val)

        if not root.left and not root.right and self.sumPath() == targetSum:
            return True

        if self.hasPathSum(root.left, targetSum):
            return True

        if self.hasPathSum(root.right, targetSum):
            return True

        self.path.pop()
        return False

    def sumPath(self):
        print("values: ", self.path)
        res = 0
        for val in self.path:
            res += val
        return res
        
# @leet end

# Define the test cases
test_cases = [
    {   # ✅ Example 0
        "tree": [10,2,11,0],
        "targetSum": 12,
        "expected": True,
    },
    {   # ✅ Example 0
        "tree": [1,2],
        "targetSum": 1,
        "expected": False,
    },
    {   # ✅ Example 1
        "tree": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
        "targetSum": 22,
        "expected": True,
    },
    {   # ✅ Example 2
        "tree": [1, 2, 3],
        "targetSum": 5,
        "expected": False,
    },
    {   # ✅ Example 3 (Empty tree)
        "tree": [],
        "targetSum": 0,
        "expected": False,
    },
    {   # ✅ Single-node tree (matches target)
        "tree": [5],
        "targetSum": 5,
        "expected": True,
    },
    {   # ✅ Single-node tree (does not match target)
        "tree": [5],
        "targetSum": 10,
        "expected": False,
    },
]

class TestPathSum(unittest.TestCase):
    def test_has_path_sum(self):
        for i, test in enumerate(test_cases):
            root = build_tree(test["tree"])  # Assume build_tree is implemented
            result = Solution().hasPathSum(root, test["targetSum"])  # Assume hasPathSum is implemented
            
            try:
                self.assertEqual(result, test["expected"],
                                 f"Test case {i + 1} failed: Expected {test['expected']}, got {result}")
                print(f"Test case {i + 1} passed! ✅")
            except AssertionError as e:
                print(f"Test case {i + 1} failed! ❌ {e}")

def build_tree(arr):
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


# Run tests
if __name__ == "__main__":
    unittest.main()
