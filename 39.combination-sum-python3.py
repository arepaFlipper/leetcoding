from typing import List
# @leet start
class Solution(object):
    def __init__(self):
        self.result = []
        self.target = 0
        self.candidates = []

    def combinationSum(self, candidates: List[int], target: int):
        self.target = target
        self.candidates = candidates
        self.depth_first_search(0, [], 0)
        return self.result

    def depth_first_search(self, idx, current, total):
        if total == self.target:
            self.result.append(current.copy())
            return
        
        if idx >= len(self.candidates) or total > self.target:
            return

        current.append(self.candidates[idx])
        self.depth_first_search(idx, current, total + self.candidates[idx])
        current.pop()
        self.depth_first_search(idx +1, current, total)

    
        
# @leet end

def test_combination_sum():
    test_cases = [
        {"candidates": [2, 3, 6, 7], "target": 7, "expected": [[2, 2, 3], [7]]},
        {"candidates": [2, 3, 5], "target": 8, "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]]},
        {"candidates": [2], "target": 1, "expected": []},
        {"candidates": [1], "target": 2, "expected": [[1, 1]]},
        {"candidates": [10], "target": 10, "expected": [[10]]},
    ]

    for i, test in enumerate(test_cases):
        try:
            result = Solution()
            result = result.combinationSum(test["candidates"], test["target"])
            result.sort()  # Sort to allow order-independent comparison
            expected = test["expected"]
            expected.sort()

            assert result == expected, f"Test {i + 1} failed: Expected {expected}, got {result}"
            print(f"Test {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test {i + 1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_combination_sum()

