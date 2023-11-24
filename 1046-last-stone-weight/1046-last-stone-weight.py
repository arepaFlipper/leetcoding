from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        
        while len(stones)>1:
            max_stone = heapq._heappop_max(stones)
            diff = max_stone - stones[0]
            if diff:
                heapq._heapreplace_max(stones,diff)
            else:
                heapq._heappop_max(stones)

        stones.append(0)
        return stones[0]

solution = Solution()

# Test Case 1
input_stones_1 = [2, 7, 4, 1, 8, 1]
expected_output_1 = 1
result_1 = solution.lastStoneWeight(input_stones_1)

print("Test Case 1:")
print("Input:", input_stones_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_stones_2 = [1]
expected_output_2 = 1
result_2 = solution.lastStoneWeight(input_stones_2)

print("\nTest Case 2:")
print("Input:", input_stones_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_stones_3 = [5, 5, 5, 5]
expected_output_3 = 0
result_3 = solution.lastStoneWeight(input_stones_3)

print("\nTest Case 3:")
print("Input:", input_stones_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

