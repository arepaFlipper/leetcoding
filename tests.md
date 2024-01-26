I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

             https://leetcode.com/problems/surrounded-regions/
                                      
                          130. Surrounded Regions
                   Medium | 8283  1733  | 38.7% of 1.7M



Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



󰛨 Example 1:

[img](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)

	▎	Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
	▎	Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
	▎	Explanation: Notice that an 'O' should not be flipped if:
	▎	- It is on the border, or
	▎	- It is adjacent to an 'O' that should not be flipped.
	▎	The bottom 'O' is on the border, so it is not flipped.
	▎	The other three 'O' form a surrounded region, so they are flipped.

󰛨 Example 2:

	▎	Input: board = [["X"]]
	▎	Output: [["X"]]



 Constraints:

	* m == board.length
	
	* n == board[i].length
	
	* 1 <= m, n <= 200
	
	* board[i][j] is 'X' or 'O'.




The following is my solution to test:

```
# @leet start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        (ROWS,COLS) = (len(board), len(board[0]))
        def capture(r,c):
            if (r<0) or (c<0) or (r == ROWS) or (c == COLS) or board[r][c] != 'O':
                return
            board[r][c] = "T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c +1)
            capture(r, c -1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS -1] or c in [0, COLS -1]):
                    capture(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
# @leet end
```
