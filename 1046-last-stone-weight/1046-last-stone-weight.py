from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones = [-stone for stone in stones]
        heapq.heapify(negative_stones)
        
        while len(negative_stones)>1:
            heaviest_stone = heapq.heappop(negative_stones)
            lighter_stone = heapq.heappop(negative_stones)
            heapq.heappush(negative_stones, heaviest_stone - lighter_stone)

        return -negative_stones[0] 

solution = Solution()

def test_last_stone_weight():
    test_cases = [
        {
            "input": [2, 7, 4, 1, 8, 1],
            "expected": 1,
        },
        {
            "input": [1],
            "expected": 1,
        },
        {
            "input": [3, 3, 3],
            "expected": 3,
        },
        {
            "input": [10, 10, 10, 10],
            "expected": 0,
        },
        {
            "input": [5, 3, 8, 2, 9, 10],
            "expected": 1,
        },
        {
            "input": [9, 3, 2, 10],
            "expected": 0,
        },
        {
            "input": [7, 6, 7, 6, 9],
            "expected": 3,
        },
        {
            "input": [31, 26, 33, 21, 40],
            "expected": 9,
        },
    ]

    for i, test in enumerate(test_cases):
        result = solution.lastStoneWeight(test["input"])

        try:
            assert result == test["expected"], f"Test {i + 1} failed: Expected {test['expected']}, got {result}"
            print(f"Test {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test {i + 1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_last_stone_weight()

