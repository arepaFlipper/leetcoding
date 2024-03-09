I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

              https://leetcode.com/problems/set-matrix-zeroes/
                                      
                           73. Set Matrix Zeroes
             Medium  │ 13999  705  │ 55.1% of 2.4M │ 󰛨 Hints



Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).



󰛨 Example 1:

[img](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

	│ Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
	│ Output: [[1,0,1],[0,0,0],[1,0,1]]

󰛨 Example 2:

[img](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

	│ Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
	│ Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]



 Constraints:

	* m == matrix.length
	
	* n == matrix[0].length
	
	* 1 <= m, n <= 200
	
	* -2^31 <= matrix[i][j] <= 2^31 - 1



Follow up:

	* A straightforward solution using O(mn) space is probably a bad idea.
	
	* A simple improvement uses O(m + n) space, but still not the best solution.
	
	* Could you devise a constant space solution?







The following is my solution to test:

```
# @leet start
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
```
