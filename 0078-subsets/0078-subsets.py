from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

solution = Solution()

# Test Case 1
input_nums_1 = [1, 2, 3]
expected_output_1 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
result_1 = solution.subsets(input_nums_1)

print("Test Case 1:")
print("Input:")
print("nums:", input_nums_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_nums_2 = [0]
expected_output_2 = [[], [0]]
result_2 = solution.subsets(input_nums_2)

print("\nTest Case 2:")
print("Input:")
print("nums:", input_nums_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_nums_3 = [5, 7, 9]
expected_output_3 = [[], [5], [7], [5, 7], [9], [5, 9], [7, 9], [5, 7, 9]]
result_3 = solution.subsets(input_nums_3)

print("\nTest Case 3:")
print("Input:")
print("nums:", input_nums_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

