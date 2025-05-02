from typing import List

# @leet start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]

        for num in nums:
            current_sum = max(current_sum,0)
            current_sum += num
            max_sum = max(max_sum, current_sum)
            print("🧳   \x1b[1;30;47m ","num", num, "max_sum: ",max_sum, "current_sum", current_sum) ## DELETEME:
            print('\x1b[0m') ## DELETEME:

        return max_sum

# @leet end

# Define test cases as (input_list, expected_output)
test_cases = [
    ([4, -1, 2, -7, 3, 4], 7),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
    ([-1, -2, -3, -4], -1),  # Edge case: all negative numbers
    ([1, 2, 3, 4, 5], 15),   # Edge case: all positive numbers
]

# Run the test cases
for idx, (nums, expected) in enumerate(test_cases, 1):
    print(f"\nTest Case {idx}:")
    output = Solution().maxSubArray(nums)
    print(f"maxSubArray({nums}) => Output: {output}")
    if output == expected:
        print("✅ Expected Output")
    else:
        print(f"❌ Unexpected Output (Expected: {expected})")

