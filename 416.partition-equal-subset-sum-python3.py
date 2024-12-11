from typing import List

# @leet start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for idx in range(len(nums) - 1, -1, -1):
            next_dp = set()
            for t in dp:
                if (t + nums[idx]) == target:
                    return True
                next_dp.add(t + nums[idx])
                next_dp.add(t)
            dp = next_dp
        return False

# @leet end

solution = Solution()

# Test Case 1
nums1 = [1, 5, 11, 5]
expected_output_1 = True

print("Test Case 1:")
output_1 = solution.canPartition(nums1)
print("canPartition([1, 5, 11, 5]) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
nums2 = [1, 2, 3, 5]
expected_output_2 = False

print("\nTest Case 2:")
output_2 = solution.canPartition(nums2)
print("canPartition([1, 2, 3, 5]) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
