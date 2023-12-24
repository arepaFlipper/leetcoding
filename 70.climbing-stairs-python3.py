# @leet start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        (n1, n2) = (2, 3)

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2


solution = Solution()

# Test Case 1
input_n_1 = 2
expected_output_1 = 2
result_1 = solution.climbStairs(input_n_1)

print("Test Case 1:")
print("Input:")
print("n:", input_n_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_n_2 = 3
expected_output_2 = 3
result_2 = solution.climbStairs(input_n_2)

print("\nTest Case 2:")
print("Input:")
print("n:", input_n_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Additional Test Case
input_n_3 = 5
expected_output_3 = 8
result_3 = solution.climbStairs(input_n_3)

print("\nAdditional Test Case:")
print("Input:")
print("n:", input_n_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# @leet end
