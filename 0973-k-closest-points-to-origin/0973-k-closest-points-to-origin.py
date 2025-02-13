import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        elements = []
        result = []
        squared_distances = []
        for (x,y) in points:
            squrt_dist = (x**2) + (y**2)
            squared_distances.append([squrt_dist, x, y])

        heapq.heapify(squared_distances)

        elements = heapq.nsmallest(k, squared_distances)

        for el in elements:
            (d, x, y) = el
            result.append([x,y])
        
        return result

solution = Solution()

def test_k_closest():
    test_cases = [
        {
            "input": {"points": [[1, 3], [-2, 2]], "k": 1},
            "expected": [[-2, 2]],
        },
        {
            "input": {"points": [[3, 3], [5, -1], [-2, 4]], "k": 2},
            "expected": [[3, 3], [-2, 4]],  # Order may vary
        },
        {
            "input": {"points": [[0, 1], [1, 0], [-1, -1]], "k": 2},
            "expected": [[0, 1], [1, 0]],  # Order may vary
        },
        {
            "input": {"points": [[10, 10], [-5, -5], [2, 2], [0, 0]], "k": 3},
            "expected": [[0, 0], [2, 2], [-5, -5]],  # Order may vary
        },
        {
            "input": {"points": [[10000, 10000], [-10000, -10000]], "k": 1},
            "expected": [[-10000, -10000]],  # This is closer to origin
        },
        {
            "input": {"points": [[1, 2], [2, 3], [3, 4]], "k": 3},
            "expected": [[1, 2], [2, 3], [3, 4]],  # All are returned
        },
    ]

    for i, test in enumerate(test_cases):
        result = Solution().kClosest(**test["input"])

        try:
            assert sorted(result) == sorted(test["expected"]), f"Test {i + 1} failed: Expected {test['expected']}, got {result}"
            print(f"Test {i + 1} passed! ✅")
        except Exception as e:
            print(f"Test {i + 1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_k_closest()

