I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

            https://leetcode.com/problems/reconstruct-itinerary/
                                      
                         332. Reconstruct Itinerary
                   Hard | 5755  1850  | 43.3% of 959.1K



You are given a list of airline tickets where tickets[i] = [from_i, to_i] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

	* For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.



󰛨 Example 1:

[img](https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg)

	│ Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
	│ Output: ["JFK","MUC","LHR","SFO","SJC"]

󰛨 Example 2:

[img](https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg)

	│ Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
	│ Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
	│ Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.



 Constraints:

	* 1 <= tickets.length <= 300
	
	* tickets[i].length == 2
	
	* from_i.length == 3
	
	* to_i.length == 3
	
	* from_i and to_i consist of uppercase English letters.
	
	* from_i != to_i







The following is my solution to test:

```
# @leet start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj: Dict = { source: [] for (source, dist) in tickets }
        res = []

        for (src, destination) in tickets:
            adj[src].append(destination)

        for key in adj:
            adj[key].sort()

        def depth_first_search(adj,result, source):
            if source in adj:
                destinations = adj[source][:]
                while destinations:
                    dest = destinations[0]
                    adj[source].pop(0)
                    depth_first_search(adj, res, dest)
                    destinations = adj[source][:]
            res.append(source)

        depth_first_search(adj, res, "JFK")
        res.reverse()

        if len(res) != len(tickets) +1:
            return []

        return res
# @leet end
```
