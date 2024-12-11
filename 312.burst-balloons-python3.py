from typing import List

# @leet start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1]

        for offset in range(2, len(nums)):
            for left in range(len(nums) - offset):
                right = left + offset
                for pivot in range(left + 1, right):
                    coins = nums[left] * nums[pivot] * nums[right]
                    coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                    cache[(left, right)] = max(coins, cache.get((left, right), 0))
        return cache.get((0, len(nums) - 1), 0)

# @leet end

solution = Solution()

# Test Case 1
nums_1 = [3, 1, 5, 8]
expected_output_1 = 167

print("Test Case 1:")
output_1 = solution.maxCoins(nums_1)
print(f"maxCoins({nums_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
nums_2 = [1, 5]
expected_output_2 = 10

print("\nTest Case 2:")
output_2 = solution.maxCoins(nums_2)
print(f"maxCoins({nums_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

