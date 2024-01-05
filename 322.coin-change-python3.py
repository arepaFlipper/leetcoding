from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for target in range(1, amount + 1):
            for coin in coins:
                if target - coin >= 0:
                    dp[target] = min(dp[target], 1 + dp[target - coin])

        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1


solution = Solution()

# Test Case 1
coins_1 = [1, 2, 5]
amount_1 = 11
expected_output_1 = 3
result_1 = solution.coinChange(coins_1, amount_1)

print("Test Case 1:")
print("Input:")
print("coins:", coins_1)
print("amount:", amount_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
coins_2 = [2]
amount_2 = 3
expected_output_2 = -1
result_2 = solution.coinChange(coins_2, amount_2)

print("\nTest Case 2:")
print("Input:")
print("coins:", coins_2)
print("amount:", amount_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
coins_3 = [1]
amount_3 = 0
expected_output_3 = 0
result_3 = solution.coinChange(coins_3, amount_3)

print("\nTest Case 3:")
print("Input:")
print("coins:", coins_3)
print("amount:", amount_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
