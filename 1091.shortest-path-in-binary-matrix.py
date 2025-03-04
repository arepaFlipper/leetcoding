from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0,0,1)]) # row, col, length
        visit = set((0,0))
        directions = [
            [0,1],
            [1,0],
            [-1,0],
            [0,-1],
            [-1,-1],
            [1,-1],
            [-1,1],
            [1,1],
        ]

        while q:
            (row, col, length) = q.popleft()
            if (False 
                or min(row,col) < 0
                or max(row,col)>= N
                # or (row,col) in visit
                or grid[row][col]
                ):
                print("""🦚   \x1b[1;33;40m1091.shortest-path-in-binary-matrix.py:27    row, col:""") ## DELETEME:
                print(row, col) ## DELETEME:
                print('\x1b[0m') ## DELETEME:
                continue
            if row == N-1 and col == N - 1: 
                return length

            for (row_direction, col_direction) in directions:
                if (row + row_direction, col + col_direction) not in visit:
                    q.append((row + row_direction, col + col_direction, length + 1))
                    visit.add((row + row_direction, col + col_direction))
        return -1

def test_shortest_path():
    test_cases = [
        # Test 1: Given example 1
        {
            "grid": [
                [0, 1],
                [1, 0]
            ],
            "expected": 2
        },

        # Test 2: Given example 2
        {
            "grid": [
                [0, 0, 0],
                [1, 1, 0],
                [1, 1, 0]
            ],
            "expected": 4
        },

        # Test 3: No clear path (blocked start)
        {
            "grid": [
                [1, 0, 0],
                [1, 1, 0],
                [1, 1, 0]
            ],
            "expected": -1
        },

        # Test 4: No clear path (blocked end)
        {
            "grid": [
                [0, 0, 0],
                [1, 1, 0],
                [1, 1, 1]
            ],
            "expected": -1
        },

        # Test 5: Single cell grid (trivial case)
        {
            "grid": [[0]],
            "expected": 1
        },

        # Test 6: Single cell blocked grid
        {
            "grid": [[1]],
            "expected": -1
        },

        # Test 7: Large open grid (5x5)
        {
            "grid": [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ],
            "expected": 5
        },

        # Test 8: Diagonal path available
        {
            "grid": [
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0]
            ],
            "expected": 3
        },

        # Test 9: Path forced around obstacles
        {
            "grid": [
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [1, 0, 0, 0]
            ],
            "expected": 5
        }
    ]


    for i, test in enumerate(test_cases):
        result = Solution()
        result = result.shortestPathBinaryMatrix(test["grid"])  # Call your BFS function
        try:
            assert result == test["expected"], f"Test {i+1} failed: Expected {test['expected']}, got {result}"
            print(f"Test {i+1} passed! ✅")
        except Exception as e:
            print(f"Test {i+1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_shortest_path()

