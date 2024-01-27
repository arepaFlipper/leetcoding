I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

                                              https://leetcode.com/problems/rotting-oranges/
                                                                     
                                                           994. Rotting Oranges
                                                 Medium  | 12214  384  | 53.8% of 1.4M



You are given an m x n grid where each cell can have one of three values:

	* 0 representing an empty cell,
	
	* 1 representing a fresh orange, or
	
	* 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



󰛨 Example 1:

[img](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

	▎	Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
	▎	Output: 4

󰛨 Example 2:

	▎	Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
	▎	Output: -1
	▎	Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

󰛨 Example 3:

	▎	Input: grid = [[0,2]]
	▎	Output: 0
	▎	Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.



 Constraints:

	* m == grid.length
	
	* n == grid[i].length
	
	* 1 <= m, n <= 10
	
	* grid[i][j] is 0, 1, or 2.





The following is my solution to test:

```
# @leet start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        (fresh, time) = (0,0)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row,col))

        directions = [[0,1],[0,-1], [1,0], [-1,0]]
        while fresh > 0 and q:
            length = len(q)
            for idx in range(length):
                (row, col) = q.popleft()

                for (row_direction,col_direction) in directions:
                    (delta_row,delta_col) = (row + row_direction, col + col_direction)
                    if((delta_row in range(len(grid))) and (delta_col in range(len(grid[0]))) and (grid[delta_row][delta_col] == 1)):
                        grid[delta_row][delta_col] = 2
                        q.append((delta_row,delta_col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
# @leet end
```
