I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

https://leetcode.com/problems/min-cost-climbing-stairs/
                        
          746. Min Cost Climbing Stairs
 Easy | 10993  1665  | 65.2% of 1.6M | 󰛨 Hints



You are given an integer array cost where cost[i] is the cost of i^th step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



󰛨 Example 1:

	▎	Input: cost = [10,15,20]
	▎	Output: 15
	▎	Explanation: You will start at index 1.
	▎	- Pay 15 and climb two steps to reach the top.
	▎	The total cost is 15.

󰛨 Example 2:

	▎	Input: cost = [1,100,1,1,1,100,1,1,100,1]
	▎	Output: 6
	▎	Explanation: You will start at index 0.
	▎	- Pay 1 and climb two steps to reach index 2.
	▎	- Pay 1 and climb two steps to reach index 4.
	▎	- Pay 1 and climb two steps to reach index 6.
	▎	- Pay 1 and climb one step to reach index 7.
	▎	- Pay 1 and climb two steps to reach index 9.
	▎	- Pay 1 and climb one step to reach the top.
	▎	The total cost is 6.



 Constraints:

	* 2 <= cost.length <= 1000
	* 0 <= cost[i] <= 999









The following is my solution to test:
```

# @leet start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for idx in range(len(cost)-3,-1,-1):
            cost[idx] += min(cost[idx + 1], cost[idx+2])

        return min(cost[0], cost[1])
        
# @leet end
        
```

csrftoken=0lyCVY3W3FmYqQjEOq7BYpvJ7T8SAax0R0YGQZQsuT1u99FP6uqZ0vRoaRd6EBeT; 
LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzA3MjIxNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDI2NTQzZDg3N2M1MDRjYWJlZDk4M2M1MGYwM2Q1NWMwOGQ1OWJlNDkzMGEwYWFkMjI0NzExM2FlMzQwMjMzNiIsImlkIjozMDcyMjE2LCJlbWFpbCI6ImNyaXN0aWFuMDB0b3ZhckBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImNyaXN0aWFuMDB0b3ZhciIsInVzZXJfc2x1ZyI6ImNyaXN0aWFuMDB0b3ZhciIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9jcml6eTE4Mi9hdmF0YXJfMTU5MjYxMjg4NS5wbmciLCJyZWZyZXNoZWRfYXQiOjE3MDM3MjEwMjQsImlwIjoiMTc5LjMzLjExNi4yMDMiLCJpZGVudGl0eSI6IjBiMzYwNWY0ZDg2YzNlZjcyNjNmNmExMzVhZWVjNDMxIiwic2Vzc2lvbl9pZCI6NTEzMjMxNTUsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.1_iLM1qezxN4VpUjK2h9Ux6HNc8jI4huFCUQkM2NY6c; 
