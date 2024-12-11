from typing import List

# @leet start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for idx in range(len(cost) - 3, -1, -1):
            cost[idx] += min(cost[idx + 1], cost[idx + 2])

        return min(cost[0], cost[1])


solution = Solution()

# Test Case 1
input_cost_1 = [10, 15, 20]
expected_output_1 = 15
result_1 = solution.minCostClimbingStairs(input_cost_1)

print("Test Case 1:")
print("Input:")
print("cost:", input_cost_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_cost_2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
expected_output_2 = 6
result_2 = solution.minCostClimbingStairs(input_cost_2)

print("\nTest Case 2:")
print("Input:")
print("cost:", input_cost_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Additional Test Case
input_cost_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
expected_output_3 = 0
result_3 = solution.minCostClimbingStairs(input_cost_3)

print("\nAdditional Test Case:")
print("Input:")
print("cost:", input_cost_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
# @leet end
