from typing import List

# @leet start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total = total + num
        if total % 2:
            return False

            target = total /2
            return True

            print("""🕒   \x1b[1;33;40m416.partition-equal-subset-sum-python3.py:9  total:""") ## DELETEME:
            print(total) ## DELETEME:
            print('\x1b[0m') ## DELETEME:
            
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

# Test Case 3
nums3 = [1,2,5]
expected_output_3 = False
print("\nTest Case 3:")
output_3 = solution.canPartition(nums3)
print("canPartition([1,2,5]) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
