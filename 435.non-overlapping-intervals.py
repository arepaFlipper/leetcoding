from typing import List
# @leet start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
                prev_end = min(end, prev_end)
        return res
# @leet end
# # Test Case 1
intervals_1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
expected_output_1 = 1

print("Test Case 1:")
solution_instance = Solution()
output_1 = solution_instance.eraseOverlapIntervals(intervals_1)
print(f"eraseOverlapIntervals({intervals_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
intervals_2 = [[1, 2], [1, 2], [1, 2]]
expected_output_2 = 2

print("\nTest Case 2:")
solution_instance = Solution()
output_2 = solution_instance.eraseOverlapIntervals(intervals_2)
print(f"eraseOverlapIntervals({intervals_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
intervals_3 = [[1, 2], [2, 3]]
expected_output_3 = 0

print("\nTest Case 3:")
solution_instance = Solution()
output_3 = solution_instance.eraseOverlapIntervals(intervals_3)
print(f"eraseOverlapIntervals({intervals_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

