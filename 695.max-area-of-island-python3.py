# @leet start
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        (ROWS, COLS) = (len(grid), len(grid[0]))
        visit = set()

        def depth_first_search(row, col):
            if(row<0 or row == ROWS or col < 0 or col == COLS or grid[row][col] == 0 or (row,col)in visit):
                return 0
            visit.add((row,col))
            return 1 + depth_first_search(row +1, col) + depth_first_search(row+1,col) + depth_first_search(row-1,col) + depth_first_search(row,col+1) + depth_first_search(row,col-1)
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, depth_first_search(r,c))
        return area

solution = Solution()

# Test Case 1
grid_1 = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
expected_output_1 = 6

print("Test Case 1:")
output_1 = solution.maxAreaOfIsland(grid_1)
print(f"maxAreaOfIsland({grid_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
grid_2 = [[0,0,0,0,0,0,0,0]]
expected_output_2 = 0

print("\nTest Case 2:")
output_2 = solution.maxAreaOfIsland(grid_2)
print(f"maxAreaOfIsland({grid_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
# @leet end

