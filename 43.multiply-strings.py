# @leet start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
    
        res = [0] * (len(num1)+len(num2))
        (num1, num2) = (num1[::-1], num2[::-1])
        for idx in range(len(num1)):
            for jdx in range(len(num2)):
                digit = int(num1[idx])* int(num2[jdx])
                res[idx + jdx] += digit
                res[idx + jdx + 1] += res[idx + jdx]//10
                res[idx + jdx] = res[idx+jdx] % 10

        (res, beg) = (res[::-1], 0)
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str,res[beg:])
        return "".join(res)
                
        
# @leet end

# Test Case 1
test_input_1_num1 = "2"
test_input_1_num2 = "3"
expected_output_1 = "6"
output_1 = Solution().multiply(test_input_1_num1, test_input_1_num2)
print("Test Case 1:")
print(f"Input: num1 = {test_input_1_num1}, num2 = {test_input_1_num2}")
print(f"Output: {output_1}")
print(f"Expected: {expected_output_1}")
if output_1 == expected_output_1:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

# Test Case 2
test_input_2_num1 = "123"
test_input_2_num2 = "456"
expected_output_2 = "56088"
output_2 = Solution().multiply(test_input_2_num1, test_input_2_num2)
print("\nTest Case 2:")
print(f"Input: num1 = {test_input_2_num1}, num2 = {test_input_2_num2}")
print(f"Output: {output_2}")
print(f"Expected: {expected_output_2}")
if output_2 == expected_output_2:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

