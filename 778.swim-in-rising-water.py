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
# Test Case 1
grid_1 = [[0,2],[1,3]]
expected_output_1 = 3

print("Test Case 1:")
output_1 = Solution().swimInWater(grid_1)
print(f"swimInWater({grid_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
grid_2 = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
expected_output_2 = 16

print("\nTest Case 2:")
output_2 = Solution().swimInWater(grid_2)
print(f"swimInWater({grid_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

