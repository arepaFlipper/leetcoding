# @leet start
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(idx, subset):
            if idx == len(nums):
                res.append(subset[::])
                return
            
            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1, subset)

        backtrack(0, [])
        return res


solution = Solution()

# Test Case 1
input_1 = [1, 2, 2]
expected_output_1 = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
result_1 = solution.subsetsWithDup(input_1)

print("Test Case 1:")
print("Input:")
print("nums:", input_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_2 = [0]
expected_output_2 = [[], [0]]
result_2 = solution.subsetsWithDup(input_2)

print("\nTest Case 2:")
print("Input:")
print("nums:", input_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# @leet end
