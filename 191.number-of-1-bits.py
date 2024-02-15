# @leet start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res: int = 0
        while n:
            n &= n - 1
            res += 1
        return res
# @leet end
# Test Case 1
n_1 = int('00000000000000000000000000001011', 2)
expected_output_1 = 3

print("Test Case 1:")
output_1 = Solution().hammingWeight(n_1)
print(f"hammingWeight({n_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
n_2 = int('00000000000000000000000010000000', 2)
expected_output_2 = 1

print("\nTest Case 2:")
output_2 = Solution().hammingWeight(n_2)
print(f"hammingWeight({n_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
n_3 = int('11111111111111111111111111111101', 2)
expected_output_3 = 31

print("\nTest Case 3:")
output_3 = Solution().hammingWeight(n_3)
print(f"hammingWeight({n_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

