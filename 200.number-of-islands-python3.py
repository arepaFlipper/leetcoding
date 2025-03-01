# @leet start
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        (ROWS, COLS) = (len(grid),len(grid[0]))
        
        queue = deque([])
        visit = list()
        count = 0

        def flip(r,c):
            if False \
                or min(r,c)>=0 \
                and r<ROWS  \
                and c<COLS  \
                and (r,c) not in visit \
                and grid[r][c]== '1' \
                or False:
                grid[r][c]= '0'
                visit.append((r,c))
                flip(r-1, c)
                flip(r+1, c)
                flip(r, c-1)
                flip(r, c+1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    count += 1
                    flip(r,c)
        return count


# @leet end

solution = Solution()

# Test Case 1
def test_num_islands():
    test_cases = [
        {
            "grid": [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ],
            "expected_output": 1
        },
        {
            "grid": [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ],
            "expected_output": 3
        },
        {
            "grid": [],
            "expected_output": 0
        },
        {
            "grid": [
                ["0", "0", "0", "0", "0"],
                ["0", "1", "0", "0", "0"],
                ["0", "0", "0", "1", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            "expected_output": 2
        },
    ]

    for (idx,test) in enumerate(test_cases):
        result = solution.numIslands(test["grid"])
        try:
            assert result == test["expected_output"], f"Test {idx + 1} failed. Expected {test['expected_output']}, but got {result}"
            print(f"Test {idx + 1} passed! ✅")
        except:
            print(f"Test {idx + 1} failed. Expected {test['expected_output']}, ❌ but got {result}")

if __name__ == "__main__":
    test_num_islands()
