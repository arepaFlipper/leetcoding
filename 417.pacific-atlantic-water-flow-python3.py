# @leet start
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        (ROWS,COLS) = (len(heights), len(heights[0]))
        (pac,atl) = (set(),set())

        def depth_first_search(row, col, visit, prev_height):
            if(((row,col) in visit) or (row < 0) or (col < 0) or (row == ROWS) or (col==COLS) or (heights[row][col] < prev_height)):
                return
            visit.add((row,col))
            depth_first_search(row+1, col, visit, heights[row][col])
            depth_first_search(row-1, col, visit, heights[row][col])
            depth_first_search(row, col+1, visit, heights[row][col])
            depth_first_search(row, col-1, visit, heights[row][col])

        for c in range(COLS):
            depth_first_search(0,c, pac, heights[0][c])
            depth_first_search(ROWS - 1, c, atl, heights[ROWS -1][c])

        for r in range(ROWS):
            depth_first_search(r, 0, pac, heights[r][0])
            depth_first_search(r, COLS -1, atl, heights[r][COLS-1])

        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) in pac and (row,col) in atl:
                    res.append([row,col])
        return res

solution = Solution()

# Test Case 1
heights_1 = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
expected_output_1 = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

print("Test Case 1:")
output_1 = solution.pacificAtlantic(heights_1)
print(f"pacificAtlantic({heights_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
heights_2 = [[1]]
expected_output_2 = [[0,0]]

print("\nTest Case 2:")
output_2 = solution.pacificAtlantic(heights_2)
print(f"pacificAtlantic({heights_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
# @leet end

