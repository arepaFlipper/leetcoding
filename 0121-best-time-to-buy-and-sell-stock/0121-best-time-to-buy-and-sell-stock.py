class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_idx = 0
        r_idx = 1
        res: int = 0
        while (l_idx< len(prices)):
            l_value = prices[l_idx]
            for r_value in prices[l_idx:]:
                profit = r_value - l_value 
                res = max(res,profit)
                r_idx += 1
            l_idx += 1
        return res
