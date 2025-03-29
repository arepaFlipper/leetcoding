# @leet start
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        (fresh, time) = (0,0)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                value = grid[row][col]
                if value == 1:
                    fresh += 1

                if value == 2:
                    queue.append((row,col))

        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        while fresh > 0 and queue:
            length = len(queue)
            for idx in range(length):
                (row,col) = queue.popleft()

                for (row_direction, col_direction) in directions:
                    (delta_row, delta_col) = (row + row_direction, col + col_direction)

                    if (
                        delta_row in range (len(grid))
                        and delta_col in range(len(grid[0]))
                        and grid[delta_row][delta_col] == 1
                    ):
                        grid[delta_row][delta_col] = 2
                        queue.append((delta_row, delta_col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1



solution = Solution()

def test_rotting_oranges():
    test_cases = [
        # Test 1: Given example 1
        {
            "grid" : [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
            "expected": 4
        },
        # Test 2: Given example 2
        {
            "grid": [[2,1,1],[0,1,1],[1,0,1]],
            "expected": -1
        },

        # Test 3: No clear path (blocked start)
        {
            "grid": [[0,2]],
            "expected": 0
        }
    ]


    for i, test in enumerate(test_cases):
        result = Solution()
        result = result.orangesRotting(test["grid"])
        try:
            assert result == test["expected"], f"Test {i+1} failed: Expected {test['expected']}, got {result}"
            print(f"Test {i+1} passed! ✅")
        except Exception as e:
            print(f"Test {i+1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_rotting_oranges()

