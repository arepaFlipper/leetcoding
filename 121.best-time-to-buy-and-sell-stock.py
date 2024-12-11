# @leet start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest= price
            profit = max(profit, price-lowest)
        return profit
        
# @leet end

# Test functions
def test_max_profit_case_1():
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    expected = 5
    result = solution.maxProfit(prices)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 1 succeed 👍")

def test_max_profit_case_2():
    solution = Solution()
    prices = [7, 6, 4, 3, 1]
    expected = 0
    result = solution.maxProfit(prices)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 2 succeed 👍")

def test_max_profit_case_3():
    solution = Solution()
    prices = [2, 4, 1]
    expected = 2
    result = solution.maxProfit(prices)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 3 succeed 👍")

def main():
    # Simulate running tests
    test_max_profit_case_1()
    test_max_profit_case_2()
    test_max_profit_case_3()

if __name__ == "__main__":
    main()
