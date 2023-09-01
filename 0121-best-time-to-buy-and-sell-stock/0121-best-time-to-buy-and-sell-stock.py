class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res: int = 0
        l_idx = 0
        r_idx = 1
        while r_idx < len(prices):
            if prices[l_idx] < prices[r_idx]:
                profit = prices[r_idx] - prices[l_idx]
                res = max(res, profit)
            else:
                l_idx = r_idx
            r_idx += 1
        return res
