# @leet start
import math
class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483648

        res = 0
        while x:
            digit = int(math.fmod( x , 10))
            x = int(x/10)

            if (res > MAX // 10) or (res == MAX // 10 and digit > MAX % 10):
                return 0

            if (res < MIN // 10) or (res == MIN // 10 and digit < MIN % 10):
                return 0

            res = (res * 10) + digit
        return res
# @leet end

# Test Case 1
x_1 = 123
expected_output_1 = 321

print("Test Case 1:")
output_1 = Solution().reverse(x_1)
print(f"reverse({x_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
x_2 = -123
expected_output_2 = -321

print("\nTest Case 2:")
output_2 = Solution().reverse(x_2)
print(f"reverse({x_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
x_3 = 120
expected_output_3 = 21

print("\nTest Case 3:")
output_3 = Solution().reverse(x_3)
print(f"reverse({x_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

