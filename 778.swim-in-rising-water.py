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


# ---------- Vanilla test suite ----------
test_cases = [
    (
        [[0, 2],
         [1, 3]],                         # grid
        3                                  # expected output
    ),
    (
        [[0,  1,  2,  3,  4],
         [24, 23, 22, 21, 5],
         [12, 13, 14, 15, 16],
         [11, 17, 18, 19, 20],
         [10,  9,  8,  7,  6]],            # grid
        16                                 # expected output
    ),
]

for idx, (grid, expected) in enumerate(test_cases, start=1):
    print(f"\nTest Case {idx}:")
    output = Solution().swimInWater(grid)
    print(f"swimInWater({grid}) => Output:", output)
    if output == expected:
        print("✅ Expected Output")
    else:
        print(f"❌ Unexpected Output (expected {expected})")

