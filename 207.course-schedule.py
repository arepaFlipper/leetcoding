# @leet start
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}

        for course, pre_requisite in prerequisites:
            pre_map[course].append(pre_requisite)

        visiting = set()

        def depth_first_search(course):
            if course in visiting:
                return False
            if pre_map[course] == []:
                return True

            visiting.add(course)
            for pre in pre_map[course]:
                if not depth_first_search(pre):
                    return False
            visiting.remove(course)
            pre_map[course] = []
            return True

        for crs in range(numCourses):
            if not depth_first_search(crs):
                return False
        return True

solution = Solution()

# Test Case 1
numCourses_1 = 2
prerequisites_1 = [[1, 0]]
expected_output_1 = True

print("Test Case 1:")
output_1 = solution.canFinish(numCourses_1, prerequisites_1)
print(f"canFinish({numCourses_1}, {prerequisites_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
numCourses_2 = 2
prerequisites_2 = [[1, 0], [0, 1]]
expected_output_2 = False

print("\nTest Case 2:")
output_2 = solution.canFinish(numCourses_2, prerequisites_2)
print(f"canFinish({numCourses_2}, {prerequisites_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
numCourses_3 = 5
prerequisites_3 = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
expected_output_3 = True

print("\nTest Case 3:")
output_3 = solution.canFinish(numCourses_3, prerequisites_3)
print(f"canFinish({numCourses_3}, {prerequisites_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
# Add more test cases as needed
# @leet end

