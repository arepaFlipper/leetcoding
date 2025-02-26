from typing import List

class Solution:
    def __init__(self):
        ROWS, COLS = 0, 0

    def helper(self, grid: List[List[int]], r: int, c: int, visit: set) -> int:
        if False \
            or min(r,c) < 0 \
            or r== self.ROWS \
            or c== self.COLS \
            or (r,c) in visit \
            or grid[r][c] == 1 \
            or False:
            return 0
        
        if (r == self.ROWS-1) and (c==self.COLS-1):
            return 1

        visit.add((r,c))

        count = 0
        count += self.helper(grid, r + 1, c, visit)
        count += self.helper(grid, r - 1, c, visit)
        count += self.helper(grid, r, c + 1, visit)
        count += self.helper(grid, r, c - 1, visit)

        visit.remove((r,c))
        return count

            
    def countPaths(self, grid: List[List[int]]) -> int:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        return self.helper(grid, 0, 0, set())


def test_unique_paths():
    test_cases = [
        # Test 1: Given example
        {
            "grid": [
                [0, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 1],
                [0, 1, 0, 0]
            ],
            "expected": 2
        },

        # Test 2: Single cell grid (trivial case)
        {
            "grid": [[0]],
            "expected": 1
        },

        # Test 3: Single blocked cell grid
        {
            "grid": [[1]],
            "expected": 0
        },

        # Test 4: No valid paths (full block in middle)
        {
            "grid": [
                [0, 0, 1, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 1],
                [0, 1, 0, 0]
            ],
            "expected": 0
        },

        # Test 5: Large open path grid
        {
            "grid": [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            "expected": 184  # Precomputed answer
        },

        # Test 6: Blocked start position
        {
            "grid": [
                [1, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            "expected": 0
        },

        # Test 7: Blocked end position
        {
            "grid": [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 1]
            ],
            "expected": 0
        }
    ]

    for i, test in enumerate(test_cases):
        result = Solution()
        result = result.countPaths(test["grid"])  # Call your DFS function
        try:
            assert result == test["expected"], f"Test {i+1} failed: Expected {test['expected']}, got {result}"
            print(f"Test {i+1} passed! ✅")
        except Exception as e:
            print(f"Test {i+1} failed with error: {e} ❌")


# Run tests
if __name__ == "__main__":
    test_unique_paths()

