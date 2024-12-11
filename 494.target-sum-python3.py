from typing import List
# @leet start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp: Dict = {}

        def backtrack(idx, total):
            if idx == len(nums):
                return 1 if (total == target) else 0
            
            if (idx, total) in dp:
                return dp[(idx, total)]

            dp[(idx,total)] = backtrack(idx+1, total + nums[idx]) + backtrack(idx+1, total - nums[idx])
            return dp[(idx,total)]

        return backtrack(0, 0)

# @leet end

solution = Solution()

# Test Case 1
nums_1 = [1, 1, 1, 1, 1]
target_1 = 3
expected_output_1 = 5

print("Test Case 1:")
output_1 = solution.findTargetSumWays(nums_1, target_1)
print(f'findTargetSumWays({nums_1}, {target_1}) => Output:', output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
nums_2 = [1]
target_2 = 1
expected_output_2 = 1

print("\nTest Case 2:")
output_2 = solution.findTargetSumWays(nums_2, target_2)
print(f'findTargetSumWays({nums_2}, {target_2}) => Output:', output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
