I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

               https://leetcode.com/problems/course-schedule/
                                      
                            207. Course Schedule
              Medium | 15696  651  | 46.5% of 3.1M | 󰛨 Hints



There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that you must take course b_i first if you want to take course a_i.

	* For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.



󰛨 Example 1:

	▎ Input: numCourses = 2, prerequisites = [[1,0]]
	▎ Output: true
	▎ Explanation: There are a total of 2 courses to take. 
	▎ To take course 1 you should have finished course 0. So it is possible.

󰛨 Example 2:

	▎ Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
	▎ Output: false
	▎ Explanation: There are a total of 2 courses to take. 
	▎ To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.



 Constraints:

	* 1 <= numCourses <= 2000
	
	* 0 <= prerequisites.length <= 5000
	
	* prerequisites[i].length == 2
	
	* 0 <= a_i, b_i < numCourses
	
	* All the pairs prerequisites[i] are unique.





The following is my solution to test:

```
# @leet start
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
# @leet end
```
