# @leet start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        (left, right) = (0, len(matrix) -1)
        while left < right:
            for idx in range (right - left):
                (top, bottom) = (left, right)

                # save the top_left
                top_left = matrix[top][left + idx]

                # move bottom left into top left
                matrix[top][left + idx] = matrix[bottom-idx][left]

                # move bottom right into bottom left
                matrix[bottom - idx][left] = matrix[bottom][right - idx]
        
                # move top right into bottom right
                matrix[bottom][right - idx] = matrix[top + idx][right]

                # move top left into top right
                matrix[top + idx][right] = top_left

            right -= 1
            left += 1

# @leet end
