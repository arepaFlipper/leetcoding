# @leet start
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = set()
        positive_diagonal = set()
        negative_diagonal = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for char in range(n):
                if (
                    char in column
                    or (row + char) in positive_diagonal
                    or (row - char) in negative_diagonal
                ):
                    continue

                column.add(char)
                positive_diagonal.add(row + char)
                negative_diagonal.add(row - char)
                board[row][char] = "Q"

                backtrack(row + 1)

                column.remove(char)
                positive_diagonal.remove(row + char)
                negative_diagonal.remove(row - char)
                board[row][char] = "."

        backtrack(0)
        return res


solution = Solution()

# Test Case 1
input_n_1 = 4
result_1 = solution.solveNQueens(input_n_1)

print("Test Case 1:")
print("Input:")
print("n:", input_n_1)
print("Output:", result_1)

# Test Case 2
input_n_2 = 1
result_2 = solution.solveNQueens(input_n_2)

print("\nTest Case 2:")
print("Input:")
print("n:", input_n_2)
print("Output:", result_2)
# @leet end
