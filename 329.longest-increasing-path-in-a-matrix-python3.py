from typing import List
# @leet start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp: Dict = {} 

        def dfs(row,col,prev_val):
            if (row < 0) or (row == ROWS) or (col<0) or (col==COLS) or (matrix[row][col] <= prev_val):
                return 0
            if (row, col) in dp:
                return dp[(row, col)]
            
            res = 1
            res = max(res, 1 + dfs(row + 1, col, matrix[row][col]))
            res = max(res, 1 + dfs(row - 1, col, matrix[row][col]))
            res = max(res, 1 + dfs(row, col + 1, matrix[row][col]))
            res = max(res, 1 + dfs(row, col - 1, matrix[row][col]))
            dp[(row, col)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)
        return max(dp.values())
        
# @leet end

solution = Solution()

# Test Case 1
matrix_1 = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
expected_output_1 = 4

print("Test Case 1:")
output_1 = solution.longestIncreasingPath(matrix_1)
print(f'longestIncreasingPath({matrix_1}) => Output:', output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
matrix_2 = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]
expected_output_2 = 4

print("\nTest Case 2:")
output_2 = solution.longestIncreasingPath(matrix_2)
print(f'longestIncreasingPath({matrix_2}) => Output:', output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
matrix_3 = [
    [1]
]
expected_output_3 = 1

print("\nTest Case 3:")
output_3 = solution.longestIncreasingPath(matrix_3)
print(f'longestIncreasingPath({matrix_3}) => Output:', output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

