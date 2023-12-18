# @leet start
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res


solution = Solution()

# Test Case 1
input_1 = [10, 1, 2, 7, 6, 1, 5]
target_1 = 8
expected_output_1 = [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6]
]
result_1 = solution.combinationSum2(input_1, target_1)

print("Test Case 1:")
print("Input:")
print("candidates:", input_1)
print("target:", target_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_2 = [2, 5, 2, 1, 2]
target_2 = 5
expected_output_2 = [
    [1, 2, 2],
    [5]
]
result_2 = solution.combinationSum2(input_2, target_2)

print("\nTest Case 2:")
print("Input:")
print("candidates:", input_2)
print("target:", target_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
# @leet end
