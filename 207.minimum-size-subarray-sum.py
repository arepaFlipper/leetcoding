from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = 9999

        for left in range(len(nums)):
            right = left
            current_sum = 0

            while current_sum < target and right < len(nums):
                current_sum += nums[right]
                if current_sum >= target:
                    min_length = min(min_length, right - left + 1)
                    current_sum = 9999
                right += 1
                

        return 0 if (min_length == 9999) else min_length


test_cases = [
    (7, [2,3,1,2,4,3], 2),
    (4, [1,4,4], 1),
    (11, [1,1,1,1,1,1,1,1], 0),
]

solution = Solution()

for i, (target, nums, expected) in enumerate(test_cases, 1):
    output = solution.minSubArrayLen(target, nums)
    result = "✅" if output == expected else "❌"
    print(f"Test Case {i}: minSubArrayLen({result}, {nums}) => Output: {output} | Expected: {expected} {result}")

# @leet end

