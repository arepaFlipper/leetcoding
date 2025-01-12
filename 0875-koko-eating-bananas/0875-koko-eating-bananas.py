from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        (low, high) = (1, max(piles))
        while low <= high:
            speed = low + (high-low)//2
            total_hours = self.totalHours(piles,speed)
            if (total_hours <= hours):
                high = speed - 1
            elif (hours < total_hours):
                low = speed + 1
        return low

    def countHours(self, bananas: int, speed: int)-> int:
        hours = bananas // speed
        if (bananas % speed):
            hours += 1
        return hours
    
    def totalHours(self, piles: List[int], speed: int) -> int:
        hours = 0
        for pile in piles:
            hours += self.countHours(pile, speed)
        return hours




# Testing framework for Koko Eating Bananas
def test_koko_eating_speed():
    test_cases = [
        {"piles": [3, 6, 7, 11], "h": 8, "expected": 4},
        {"piles": [30, 11, 23, 4, 20], "h": 5, "expected": 30},
        {"piles": [30, 11, 23, 4, 20], "h": 6, "expected": 23},
        {"piles": [1, 1, 1, 1], "h": 4, "expected": 1},  # Edge case: all piles have one banana
        {"piles": [1_000_000_000], "h": 1, "expected": 1_000_000_000},  # Single pile, single hour
        {"piles": [1, 2, 3, 4, 5], "h": 15, "expected": 1},  # Slowest speed possible
        {"piles": [312884470], "h": 312884469, "expected": 2},  # Slowest speed possible
    ]

    for i, test in enumerate(test_cases):
        result = Solution()
        result = result.minEatingSpeed(test["piles"], test["h"])
        assert result == test["expected"], f"❌ Test case {i+1} failed: {result} != {test['expected']} 😭😭"
        print(f"Test case {i+1} passed! ✅")

# Run tests
test_koko_eating_speed()

