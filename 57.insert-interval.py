from typing import List

# @leet start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res: List = []

        for idx in range(len(intervals)):
            if newInterval[1]< intervals[idx][0]:
                res.append(newInterval)
                return res + intervals[idx:]
            elif newInterval[0] > intervals[idx][1]:
                res.append(intervals[idx])
            else:
                newInterval = [
                    min(newInterval[0], intervals[idx][0]),
                    max(newInterval[1], intervals[idx][1]),
                ]
        res.append(newInterval)
        return res
        
# @leet end

# Test Case 1
intervals_1 = [[1, 3], [6, 9]]
newInterval_1 = [2, 5]
expected_output_1 = [[1, 5], [6, 9]]

print("Test Case 1:")
solution_instance = Solution()
output_1 = solution_instance.insert(intervals_1, newInterval_1)
print(f"insert({intervals_1}, {newInterval_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
intervals_2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval_2 = [4, 8]
expected_output_2 = [[1, 2], [3, 10], [12, 16]]

print("\nTest Case 2:")
solution_instance = Solution()
output_2 = solution_instance.insert(intervals_2, newInterval_2)
print(f"insert({intervals_2}, {newInterval_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
