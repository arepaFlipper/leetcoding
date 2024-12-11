import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for (x,y) in points:
            dist = (x**2) + (y**2)
            min_heap.append((dist,x,y))

        heapq.heapify(min_heap)
        res = []

        for _ in range(k):
            (distance, x, y) = heapq.heappop(min_heap)
            res.append((x,y))

        return res

solution = Solution()

# Test Case 1
input_points_1 = [[1, 3], [-2, 2]]
input_k_1 = 1
expected_output_1 = [[-2, 2]]
result_1 = solution.kClosest(input_points_1, input_k_1)

print("Test Case 1:")
print("Input:")
print("Points:", input_points_1)
print("k:", input_k_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_points_2 = [[3, 3], [5, -1], [-2, 4]]
input_k_2 = 2
expected_output_2 = [[3, 3], [-2, 4]]
result_2 = solution.kClosest(input_points_2, input_k_2)

print("\nTest Case 2:")
print("Input:")
print("Points:", input_points_2)
print("k:", input_k_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_points_3 = [[0, 0], [1, 1], [2, 2], [3, 3]]
input_k_3 = 3
expected_output_3 = [[0, 0], [1, 1], [2, 2]]
result_3 = solution.kClosest(input_points_3, input_k_3)

print("\nTest Case 3:")
print("Input:")
print("Points:", input_points_3)
print("k:", input_k_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

