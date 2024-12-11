# @leet start
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for idx in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res


solution = Solution()

# Test Case 1
input_1 = [1, 2, 3]
expected_output_1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
result_1 = solution.permute(input_1)

print("Test Case 1:")
print("Input:")
print("nums:", input_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_2 = [0, 1]
expected_output_2 = [[0, 1], [1, 0]]
result_2 = solution.permute(input_2)

print("\nTest Case 2:")
print("Input:")
print("nums:", input_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_3 = [1]
expected_output_3 = [[1]]
result_3 = solution.permute(input_3)

print("\nTest Case 3:")
print("Input:")
print("nums:", input_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
# @leet end
