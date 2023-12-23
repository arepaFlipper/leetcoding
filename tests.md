I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

     https://leetcode.com/problems/n-queens/
                        
                  51. N-Queens
     Hard | 11727  256  | 67.0% of 965.3K



The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



󰛨 Example 1:

img->(https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)
	▎	Input: n = 4
	▎	Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
	▎	Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

󰛨 Example 2:

	▎	Input: n = 1
	▎	Output: [["Q"]]



 Constraints:

	* 1 <= n <= 9








The following is my solution to test:
```
# @leet start
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
                if char in column or (row + char) in positive_diagonal or (row - char) in negative_diagonal:
                    continue

                column.add(char)
                positive_diagonal.add(row + char)
                negative_diagonal.add(row - char)
                board[row][char] = "Q"

                backtrack(row+1)

                column.remove(char)
                positive_diagonal.remove(row + char)
                negative_diagonal.remove(row - char)
                board[row][char] = "."
        backtrack(0)
        return res
# @leet end
        
```
