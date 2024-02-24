I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

            https://leetcode.com/problems/swim-in-rising-water/
                                      
                         778. Swim in Rising Water
              Hard │ 3517  232  │ 60.5% of 246.8K │ 󰛨 Hints



You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).



󰛨 Example 1:

[img](https://assets.leetcode.com/uploads/2021/06/29/swim1-grid.jpg)

	│ Input: grid = [[0,2],[1,3]]
	│ Output: 3
	│ Explanation:
	│ At time 0, you are in grid location (0, 0).
	│ You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
	│ You cannot reach point (1, 1) until time 3.
	│ When the depth of water is 3, we can swim anywhere inside the grid.

󰛨 Example 2:

[img](https://assets.leetcode.com/uploads/2021/06/29/swim2-grid-1.jpg)

	│ Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
	│ Output: 16
	│ Explanation: The final route is shown.
	│ We need to wait until time 16 so that (0, 0) and (4, 4) are connected.



 Constraints:

	* n == grid.length
	
	* n == grid[i].length
	
	* 1 <= n <= 50
	
	* 0 <= grid[i][j] < n^2
	
	* Each value grid[i][j] is unique.







The following is my solution to test:

```
# @leet start
import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        min_heap = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while min_heap:
            time, row, col = heapq.heappop(min_heap)
            if row == N - 1 and col == N - 1:
                return time
            for x, y in directions:
                nei_row, nei_col = row + x, col + y
                if 0 <= nei_row < N and 0 <= nei_col < N and (nei_row, nei_col) not in visit:
                    visit.add((nei_row, nei_col))
                    heapq.heappush(min_heap, [max(time, grid[nei_row][nei_col]), nei_row, nei_col])


# @leet end
```
