I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

   https://leetcode.com/problems/coin-change/
                        
                322. Coin Change
     Medium | 18210  426  | 43.3% of 3.8M



You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



󰛨 Example 1:

	▎	Input: coins = [1,2,5], amount = 11
	▎	Output: 3
	▎	Explanation: 11 = 5 + 5 + 1

󰛨 Example 2:

	▎	Input: coins = [2], amount = 3
	▎	Output: -1

󰛨 Example 3:

	▎	Input: coins = [1], amount = 0
	▎	Output: 0



 Constraints:

	* 1 <= coins.length <= 12
	
	* 1 <= coins[i] <= 2^31 - 1
	
	* 0 <= amount <= 10^4









The following is my solution to test:
```

# @leet start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount +1)
        dp[0] = 0

        for target in range(1, amount +1):
            for coin in coins:
                if target - coin >= 0:
                    dp[target] = min(dp[target], 1 + dp[target - coin])

        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1
# @leet end
        
```
