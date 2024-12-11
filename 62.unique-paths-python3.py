# @leet start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for idx in range(m - 1):
            new_row = [1] * n
            for jdx in range(n - 2, -1, -1):
                new_row[jdx] = new_row[jdx + 1] + row[jdx]
            row = new_row
        return row[0]

# @leet end

solution = Solution()

# Test Case 1
m1, n1 = 3, 7
expected_output_1 = 28

print("Test Case 1:")
output_1 = solution.uniquePaths(m1, n1)
print("uniquePaths(3, 7) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
m2, n2 = 3, 2
expected_output_2 = 3

print("\nTest Case 2:")
output_2 = solution.uniquePaths(m2, n2)
print("uniquePaths(3, 2) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
