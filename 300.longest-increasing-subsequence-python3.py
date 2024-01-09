from typing import List

# @leet start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_increasing_subsequence = [1] * len(nums)

        for idx in range(len(nums) - 1, -1, -1):
            for jdx in range(idx + 1, len(nums)):
                if nums[idx] < nums[jdx]:
                    longest_increasing_subsequence[idx] = max(longest_increasing_subsequence[idx], 1 + longest_increasing_subsequence[jdx])
        return max(longest_increasing_subsequence)

# @leet end

solution = Solution()

# Test Case 1
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
expected_output_1 = 4

print("Test Case 1:")
output_1 = solution.lengthOfLIS(nums1)
print("lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
nums2 = [0, 1, 0, 3, 2, 3]
expected_output_2 = 4

print("\nTest Case 2:")
output_2 = solution.lengthOfLIS(nums2)
print("lengthOfLIS([0, 1, 0, 3, 2, 3]) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
nums3 = [7, 7, 7, 7, 7, 7, 7]
expected_output_3 = 1

print("\nTest Case 3:")
output_3 = solution.lengthOfLIS(nums3)
print("lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
