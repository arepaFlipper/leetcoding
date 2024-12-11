# @leet start
class Solution:
    def isHappy(self, n: int) -> bool:
        (slow, fast) = (n,self.sumSquareDigits(n))

        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n%10) ** 2
            n = n // 10
        return output
# @leet end
# Test Case 1
test_input_1 = 19
expected_output_1 = True
output_1 = Solution().isHappy(test_input_1)
print("Test Case 1:")
print(f"Input: {test_input_1}")
print(f"Output: {output_1}")
print(f"Expected: {expected_output_1}")
if output_1 == expected_output_1:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

# Test Case 2
test_input_2 = 2
expected_output_2 = False
output_2 = Solution().isHappy(test_input_2)
print("\nTest Case 2:")
print(f"Input: {test_input_2}")
print(f"Output: {output_2}")
print(f"Expected: {expected_output_2}")
if output_2 == expected_output_2:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

