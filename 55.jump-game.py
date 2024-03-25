from typing import List
# @leet start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target: int = len(nums) -1
        # for idx in range(len(nums) -2, -1, -1):
        #     print("idx: ",idx, ",nums[idx]: ", nums[idx])
        #     if idx + nums[idx] >= target:
        #         target = idx
        #         print("new target: ", target)
        reverse_nums = [nums[idx] for idx in range(len(nums)-2,-1,-1)]
        for (value, idx) in enumerate(reverse_nums):
            if idx + value >= target:
                target = idx
                print("new target: ", target)
        return target == 0
        
# @leet end
# Test Case 1
nums_1 = [2, 3, 1, 1, 4]
expected_output_1 = True

print("Test Case 1:")
output_1 = Solution().canJump(nums_1)
print(f"canJump({nums_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
nums_2 = [3, 2, 1, 0, 4]
expected_output_2 = False

print("\nTest Case 2:")
output_2 = Solution().canJump(nums_2)
print(f"canJump({nums_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
nums_3 = [0]
expected_output_3 = True

print("\nTest Case 3:")
output_3 = Solution().canJump(nums_3)
print(f"canJump({nums_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 4
nums_4 = [4, 1, 0, 0, 3, 0, 0,0]
expected_output_4 = True

print("\nTest Case 4:")
output_4 = Solution().canJump(nums_4)
print(f"canJump({nums_4}) => Output:", output_4)

if output_4 == expected_output_4:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
