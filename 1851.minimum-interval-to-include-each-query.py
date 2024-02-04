from typing import List
import heapq

# @leet start
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                (left, right) = intervals[i]
                heapq.heappush(min_heap, (right - left +1, right))
                i += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1
        return [res[q] for q in queries]

# @leet end

# Test Case 1
intervals_1 = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries_1 = [2, 3, 4, 5]
expected_output_1 = [3, 3, 1, 4]

print("Test Case 1:")
solution_instance = Solution()
output_1 = solution_instance.minInterval(intervals_1, queries_1)
print(f"minInterval({intervals_1}, {queries_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
intervals_2 = [[2, 3], [2, 5], [1, 8], [20, 25]]
queries_2 = [2, 19, 5, 22]
expected_output_2 = [2, -1, 4, 6]

print("\nTest Case 2:")
solution_instance = Solution()
output_2 = solution_instance.minInterval(intervals_2, queries_2)
print(f"minInterval({intervals_2}, {queries_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

