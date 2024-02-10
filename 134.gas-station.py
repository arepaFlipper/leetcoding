from typing import List
# @leet start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        (total, res) = (0,0)
        for idx in range(len(gas)):
            total += (gas[idx]- cost[idx])
            
            if total < 0:
                total = 0
                res = idx +1
        return res

# Test Case 1
gas_1 = [1, 2, 3, 4, 5]
cost_1 = [3, 4, 5, 1, 2]
expected_output_1 = 3

print("Test Case 1:")
output_1 = Solution().canCompleteCircuit(gas_1, cost_1)
print(f"canCompleteCircuit({gas_1}, {cost_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
gas_2 = [2, 3, 4]
cost_2 = [3, 4, 3]
expected_output_2 = -1

print("\nTest Case 2:")
output_2 = Solution().canCompleteCircuit(gas_2, cost_2)
print(f"canCompleteCircuit({gas_2}, {cost_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
gas_3 = [5, 1, 2, 3, 4]
cost_3 = [4, 4, 1, 5, 1]
expected_output_3 = 4

print("\nTest Case 3:")
output_3 = Solution().canCompleteCircuit(gas_3, cost_3)
print(f"canCompleteCircuit({gas_3}, {cost_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
