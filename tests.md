I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

                                              https://leetcode.com/problems/walls-and-gates/
                                                                     
                                                           286. Walls and Gates
                                                 Medium  | 12214  384  | 53.8% of 1.4M



You are given an m x n grid rooms initialized with these three possible values

	* -1 A wall or an obstacle.
	
	* 0 A gate.
	
	* `INF` Infinity means an empty room, We use the value `2^31 -1 = 2147483647` to represent `INF` as you may assume that the distance to a gate is less than `2147483647`.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with `INF`.


󰛨 Example 1:

[img](https://assets.leetcode.com/uploads/2019/02/16/example.png)

	▎	Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
	▎	Output: [[3,-1,0,1], [2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]


 Constraints:

	* m == rooms.length
	
	* n == rooms[i].length
	
	* 1 <= m, n <= 10
	
	* rooms[i][j] is 0, 1, or 2.





The following is my solution to test:

```
# @leet start
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRooms(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or rooms[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1

# @leet end
```
