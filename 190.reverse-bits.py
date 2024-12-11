# @leet start
class Solution:
    def reverseBits(self, n: int) -> int:
        res: int = 0
        for idx in range(32):
            bit: int = (n >> idx) & 1
            res += (bit << (31 - idx))
        return res
# @leet end
# Test Case 1

n_1 = int("00000010100101000001111010011100", 2)
expected_output_1 = int("00111001011110000010100101000000", 2)

print("Test Case 1:")
output_1 = Solution().reverseBits(n_1)
print(f"reverseBits({n_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
n_2 = int("11111111111111111111111111111101", 2)
expected_output_2 = int("10111111111111111111111111111111", 2)

print("\nTest Case 2:")
output_2 = Solution().reverseBits(n_2)
print(f"reverseBits({n_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
n_3 = int("00000000000000000000000000000000", 2)
expected_output_3 = int("00000000000000000000000000000000", 2)

print("\nTest Case 3:")
output_3 = Solution().reverseBits(n_3)
print(f"reverseBits({n_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

