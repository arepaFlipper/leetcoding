# @leet start
from typing import List
from collections import deque

class Solution:
    def canFinish(self, num_courses: int, pre_requisites: List[List[int]]) -> bool:
        indegree = [0] * num_courses
        adjacency_list = [ [] for idx in range(num_courses) ]
        for (source, destination) in pre_requisites:
            indegree[destination] += 1
            element = adjacency_list[source]
            element.append(destination)

        queue = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        finish = 0
        while queue:
            course_node = queue.popleft()
            finish += 1
            for neighbor in adjacency_list[course_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return finish == num_courses

solution = Solution()

test_cases = [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False),
    (5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]], True),
    (3, [[0, 1], [1, 2], [2, 0]], False),  # Cycle case
    (4, [], True),  # No prerequisites
    (1, [], True)  # Single course, no prerequisite
]

for i, (numCourses, prerequisites, expected) in enumerate(test_cases, 1):
    output = solution.canFinish(numCourses, prerequisites)
    result = "✅" if output == expected else "❌"
    print(f"Test Case {i}: canFinish({numCourses}, {prerequisites}) => Output: {output} | Expected: {expected} {result}")

# @leet end

