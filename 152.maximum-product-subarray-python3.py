from typing import List
# @leet start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res: int = nums[0]
        (current_min, current_max) = (1, 1)

        for number in nums:
            temp = current_max * number
            current_max = max(number, temp, current_min * number)
            current_min = min(temp, current_min * number, number)
            res = max(res, current_max)
        return res


solution = Solution()

# Test Case 1
nums_1 = [2, 3, -2, 4]
expected_output_1 = 6
result_1 = solution.maxProduct(nums_1)

print("Test Case 1:")
print("Input:")
print("nums:", nums_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
nums_2 = [-2, 0, -1]
expected_output_2 = 0
result_2 = solution.maxProduct(nums_2)

print("\nTest Case 2:")
print("Input:")
print("nums:", nums_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

