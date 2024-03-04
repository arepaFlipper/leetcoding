# @leet start
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        (left, right) = (0, len(matrix[0]))
        (top, bottom) = (0, len(matrix))

        while (left < right) and (top < bottom):
            # get every idx in the top row
            for idx in range(left,right):
                res.append(matrix[top][idx])
            top += 1

            # get every idx in the right col 
            for idx in range(top,bottom):
                res.append(matrix[idx][right-1])
            right -= 1

            if not (left<right and top < bottom):
                break

            # get every idx in the bottom row
            for idx in range(right -1, left - 1, -1):
                res.append(matrix[bottom-1][idx])
            bottom -= 1

            # get every idx in the left col
            for idx in range(bottom -1, top -1, -1):
                res.append(matrix[idx][left])
            left += 1

        return res

# @leet end

# Test Case 1
matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
expected_output_1 = [1,2,3,6,9,8,7,4,5]

print("Test Case 1:")
output_1 = Solution().spiralOrder(matrix_1)
print(f"spiralOrder({matrix_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
matrix_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
expected_output_2 = [1,2,3,4,8,12,11,10,9,5,6,7]

print("\nTest Case 2:")
output_2 = Solution().spiralOrder(matrix_2)
print(f"spiralOrder({matrix_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

