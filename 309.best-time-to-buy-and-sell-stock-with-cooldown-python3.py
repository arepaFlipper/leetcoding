from typing import List

# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def depth_first_search(idx: int, buying: bool):
            if idx >= len(prices):
                return 0
            if (idx, buying) in dp:
                return dp[(idx, buying)]

            cooldown = depth_first_search(idx + 1, buying)

            if buying:
                buy = depth_first_search(idx + 1, not buying) - prices[idx]
                dp[(idx, buying)] = max(buy, cooldown)
            else:
                sell = depth_first_search(idx + 2, not buying) + prices[idx]
                dp[(idx, buying)] = max(sell, cooldown)
            return dp[(idx, buying)]

        return depth_first_search(0, True)

# @leet end

solution = Solution()

# Test Case 1
prices_1 = [1, 2, 3, 0, 2]
expected_output_1 = 3

print("Test Case 1:")
output_1 = solution.maxProfit(prices_1)
print(f'maxProfit({prices_1}) => Output:', output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
prices_2 = [1]
expected_output_2 = 0

print("\nTest Case 2:")
output_2 = solution.maxProfit(prices_2)
print(f'maxProfit({prices_2}) => Output:', output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

