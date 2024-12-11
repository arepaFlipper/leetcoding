from typing import List, Dict
# @leet start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req: Dict = {course: [] for course in range(numCourses)}
        for (course, pre) in prerequisites:
            pre_req[course].append(pre)

        output: List = []
        (visit, cycle) = (set(),set())

        def depth_first_search(course):
            if course in cycle:
                return False
            
            if course in visit:
                return True

            cycle.add(course)
            for pre in pre_req[course]:
                if depth_first_search(pre) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if depth_first_search(c) == False:
                return []
        return output
# @leet end

# Test Case 1
numCourses_1 = 2
prerequisites_1 = [[1, 0]]
expected_output_1 = [0, 1]

print("Test Case 1:")
solution_instance = Solution()
output_1 = solution_instance.findOrder(numCourses_1, prerequisites_1)
print(f"findOrder({numCourses_1}, {prerequisites_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
numCourses_2 = 4
prerequisites_2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
expected_output_2 = [0, 1, 2, 3]

print("\nTest Case 2:")
solution_instance = Solution()
output_2 = solution_instance.findOrder(numCourses_2, prerequisites_2)
print(f"findOrder({numCourses_2}, {prerequisites_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
numCourses_3 = 1
prerequisites_3 = []
expected_output_3 = [0]

print("\nTest Case 3:")
solution_instance = Solution()
output_3 = solution_instance.findOrder(numCourses_3, prerequisites_3)
print(f"findOrder({numCourses_3}, {prerequisites_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

