I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

  https://leetcode.com/problems/coin-change-ii/
                        
               518. Coin Change II
     Medium | 9037  159  | 63.5% of 896.5K



You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.



󰛨 Example 1:

	▎	Input: amount = 5, coins = [1,2,5]
	▎	Output: 4
	▎	Explanation: there are four ways to make up the amount:
	▎	5=5
	▎	5=2+2+1
	▎	5=2+1+1+1
	▎	5=1+1+1+1+1

󰛨 Example 2:

	▎	Input: amount = 3, coins = [2]
	▎	Output: 0
	▎	Explanation: the amount of 3 cannot be made up just with coins of 2.

󰛨 Example 3:

	▎	Input: amount = 10, coins = [10]
	▎	Output: 1



 Constraints:

	* 1 <= coins.length <= 300
	
	* 1 <= coins[i] <= 5000
	
	* All the values of coins are unique.
	
	* 0 <= amount <= 5000









The following is my solution to test:
```
# @leet start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache: Dict = {}

        def depth_first_search(idx, target):
            if target == amount:
                return 1
            
            if target > amount:
                return 0
        
            if idx == len(coins):
                return 0

            if (idx, target) in cache:
                return cache[(idx,target)]
    
            cache[(idx, target)] = depth_first_search(idx, target + coins[idx]) + depth_first_search(idx + 1, target)
            return cache[(idx, target)]
        return depth_first_search(0,0)
        
# @leet end
```
