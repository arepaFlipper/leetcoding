# @leet start
from typing import List

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

# Test Case 1
tickets_1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
expected_output_1 = ["JFK","MUC","LHR","SFO","SJC"]

print("Test Case 1:")
output_1 = Solution().findItinerary(tickets_1)
print(f"findItinerary({tickets_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
tickets_2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
expected_output_2 = ["JFK","ATL","JFK","SFO","ATL","SFO"]

print("\nTest Case 2:")
output_2 = Solution().findItinerary(tickets_2)
print(f"findItinerary({tickets_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

