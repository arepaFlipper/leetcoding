from typing import List

# @leet start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for target in range(1, amount +1 ):
            for idx in range(len(coins) -1, -1, -1):
                dp[target][idx] = dp[target][idx +1]
                if target - coins[idx] >= 0:
                    dp[target][idx] += dp[target - coins[idx]][idx]
        return dp[amount][0]

# @leet end

solution = Solution()

# Test Case 1
amount_1 = 5
coins_1 = [1, 2, 5]
expected_output_1 = 4

print("Test Case 1:")
output_1 = solution.change(amount_1, coins_1)
print(f'change({amount_1}, {coins_1}) => Output:', output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
amount_2 = 3
coins_2 = [2]
expected_output_2 = 0

print("\nTest Case 2:")
output_2 = solution.change(amount_2, coins_2)
print(f'change({amount_2}, {coins_2}) => Output:', output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
amount_3 = 10
coins_3 = [10]
expected_output_3 = 1

print("\nTest Case 3:")
output_3 = solution.change(amount_3, coins_3)
print(f'change({amount_3}, {coins_3}) => Output:', output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
