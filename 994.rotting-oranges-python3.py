# @leet start
from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        (fresh, time) = (0, 0)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for idx in range(length):
                (row, col) = q.popleft()

                for (row_direction, col_direction) in directions:
                    (delta_row, delta_col) = (row + row_direction, col + col_direction)
                    if (
                        (delta_row in range(len(grid)))
                        and (delta_col in range(len(grid[0])))
                        and (grid[delta_row][delta_col] == 1)
                    ):
                        grid[delta_row][delta_col] = 2
                        q.append((delta_row, delta_col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

solution = Solution()

# Test Case 1
grid_1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
expected_output_1 = 4

print("Test Case 1:")
output_1 = solution.orangesRotting(grid_1)
print(f"orangesRotting({grid_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
grid_2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
expected_output_2 = -1

print("\nTest Case 2:")
output_2 = solution.orangesRotting(grid_2)
print(f"orangesRotting({grid_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
grid_3 = [[0, 2]]
expected_output_3 = 0

print("\nTest Case 3:")
output_3 = solution.orangesRotting(grid_3)
print(f"orangesRotting({grid_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
# @leet end

