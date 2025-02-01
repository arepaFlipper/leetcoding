from typing import List 
from collections import deque

# @leet start
class Solution:
    def __init__(self):
        self.res = []
        self.current = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        def depth_first_search(index):
            if index >= length:
                # WARN: Here is the base case where it hits a leaf.
                self.res.append(self.current.copy())
                return

            # NOTE: decision to include nums[index]
            num = nums[index]
            self.current.append(num)
            depth_first_search(index + 1)

            # BUG: decision NOT to include nums[index]
            self.current.pop()
            depth_first_search(index + 1)

            
        depth_first_search(0)
        return self.res
            
        
# @leet end

def test_subsets():
    test_cases = [
        {"input": [1, 2, 3], "expected": [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]},
        {"input": [0], "expected": [[], [0]]},
        {"input": [1, 2], "expected": [[], [1], [2], [1, 2]]},
        {"input": [-1, 0, 1], "expected": [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]},
        {"input": [], "expected": [[]]},
    ]

    for i, test in enumerate(test_cases):
        try:
            result = Solution()
            result = result.subsets(test.get("input"))
            result.sort()  # Sorting to ensure order-independent comparison
            expected = test["expected"]
            expected.sort()

            assert result == expected, f"Test {i + 1} failed: Expected {expected}, got {result}"
            print(f"Test {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test {i + 1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_subsets()

