I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

             https://leetcode.com/problems/max-area-of-island/
                                      
                          695. Max Area of Island
                   Medium | 9728  198  | 71.8% of 1.1M



You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



󰛨 Example 1:

[img](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

	▎	Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
	▎	Output: 6
	▎	Explanation: The answer is not 11, because the island must be connected 4-directionally.

󰛨 Example 2:

	▎	Input: grid = [[0,0,0,0,0,0,0,0]]
	▎	Output: 0



 Constraints:

	* m == grid.length
	
	* n == grid[i].length
	
	* 1 <= m, n <= 50
	
	* grid[i][j] is either 0 or 1.




The following is my solution to test:

```
# @leet start
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
# @leet end
```
