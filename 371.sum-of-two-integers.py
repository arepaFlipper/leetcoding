# @leet start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(a, b):
            if not a or not b:
                return a or b
            return add(a^b, (a&b)<<1)
        
        if a * b < 0:
            if a > 0:
                return self.getSum(b,a)
            if add(~a,1) == b:
                return 0
            if add(~a,1) < b:
                return add(~add(add(~a,1), add(~b,1)), 1)
        return add(a,b)
# @leet end

# Test Case 1
a_1, b_1 = 1, 2
expected_output_1 = 3

print("Test Case 1:")
output_1 = Solution().getSum(a_1, b_1)
print(f"getSum({a_1}, {b_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
a_2, b_2 = 2, 3
expected_output_2 = 5

print("\nTest Case 2:")
output_2 = Solution().getSum(a_2, b_2)
print(f"getSum({a_2}, {b_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

