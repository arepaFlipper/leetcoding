# @leet start
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        (ROWS, COLS) = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                (row, col) = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for (dr, dc) in directions:
                    (r, c) = (row + dr, col + dc)
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
# @leet end

solution = Solution()

# Test Case 1
grid_1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
expected_output_1 = 1

print("Test Case 1:")
output_1 = solution.numIslands(grid_1)
print(f"numIslands({grid_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
grid_2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
expected_output_2 = 3

print("\nTest Case 2:")
output_2 = solution.numIslands(grid_2)
print(f"numIslands({grid_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

