# @leet start
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        (ROWS, COLS) = (len(board), len(board[0]))
        def capture(r, c):
            if (r < 0) or (c < 0) or (r == ROWS) or (c == COLS) or board[r][c] != 'O':
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

solution = Solution()

# Test Case 1
board_1 = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
expected_output_1 = [
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["X", "O", "X", "X"]
]

print("Test Case 1:")
solution.solve(board_1)
print(f"solve({board_1}) => Output:", board_1)

if board_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
board_2 = [["X"]]
expected_output_2 = [["X"]]

print("\nTest Case 2:")
solution.solve(board_2)
print(f"solve({board_2}) => Output:", board_2)

if board_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
# @leet end

