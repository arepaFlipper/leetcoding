# @leet start
from typing import List

class Solution:
    def __init__(self):
        self.max_area = 0
        self.ROWS = 0
        self.COLS = 0
        self.grid = []

    def calculate_area(self, row, col):
        if False \
            or not (0 <= row < self.ROWS and 0 <= col < self.COLS) \
            or self.grid[row][col] == 0 \
            or False:
            return 0
        self.grid[row][col] = 0
        area = 1

        area += self.calculate_area(row + 1, col)
        area += self.calculate_area(row - 1, col)
        area += self.calculate_area(row, col + 1)
        area += self.calculate_area(row, col - 1)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        (self.ROWS, self.COLS) = (len(grid), len(grid[0]))
        visit = list()
        max_area = 0

        for r in range(self.ROWS):
            for c in range(self.COLS):
                value = grid[r][c]
                if value == 1:
                    max_area = max(max_area, self.calculate_area(r,c))
        return max_area

solution = Solution()

def test_num_islands():
    test_cases = [
        {
            "grid": [
                [0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]
            ],
            "expected_output": 6
        },
        {
            "grid": [
                [1,1,1,1,0],
                [1,1,0,1,0],
                [1,1,0,0,0],
                [0,0,0,0,0]
            ],
            "expected_output": 9
        },
        {
            "grid": [
                [1,1,0,0,0],
                [1,1,0,0,0],
                [0,0,1,0,0],
                [0,0,0,1,1]
            ],
            "expected_output": 4
        },
        {
            "grid": [[0,0,0,0,0,0,0,0,0,0]],
            "expected_output": 0
        },
        {
            "grid": [
                [0,0,0,0,0],
                [0,1,1,1,0],
                [0,0,0,0,0],
                [0,0,0,1,0]
            ],
            "expected_output": 3
        },
    ]

    for (idx,test) in enumerate(test_cases):
        result = solution.maxAreaOfIsland(test["grid"])
        try:
            assert result == test["expected_output"], f"Test {idx + 1} failed. Expected {test['expected_output']}, but got {result}"
            print(f"Test {idx + 1} passed! ✅")
        except:
            print(f"Test {idx + 1} failed. Expected {test['expected_output']}, ❌ but got {result}")

if __name__ == "__main__":
    test_num_islands()

