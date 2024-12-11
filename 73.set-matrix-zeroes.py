# @leet start
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        (ROWS, COLS) = (len(matrix), len(matrix[0]))
        row_zero = False

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        row_zero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for row in range(ROWS):
                matrix[row][0] = 0

        if row_zero:
            for column in range(COLS):
                matrix[0][column] = 0

        
# @leet end

# Test Case 1
test_input_1_matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
expected_output_1 = [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1]
]
Solution().setZeroes(test_input_1_matrix)
print("Test Case 1:")
print(f"Input: matrix = {test_input_1_matrix}")
print(f"Output: {test_input_1_matrix}")
print(f"Expected: {expected_output_1}")
if test_input_1_matrix == expected_output_1:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

# Test Case 2
test_input_2_matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
expected_output_2 = [
    [0, 0, 0, 0],
    [0, 4, 5, 0],
    [0, 3, 1, 0]
]
Solution().setZeroes(test_input_2_matrix)
print("\nTest Case 2:")
print(f"Input: matrix = {test_input_2_matrix}")
print(f"Output: {test_input_2_matrix}")
print(f"Expected: {expected_output_2}")
if test_input_2_matrix == expected_output_2:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

