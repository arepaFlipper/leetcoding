# @leet start
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for idx in range(k+1):
            tmp_prices = prices.copy()

            for s,d,p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmp_prices[d]:
                    tmp_prices[d] = prices[s] + p
            prices = tmp_prices
        return -1 if prices[dst] == float("inf") else prices[dst]

# @leet end
# Test Case 1
n_1 = 4
flights_1 = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src_1 = 0
dst_1 = 3
k_1 = 1
expected_output_1 = 700

print("Test Case 1:")
output_1 = Solution().findCheapestPrice(n_1, flights_1, src_1, dst_1, k_1)
print(f"findCheapestPrice({n_1}, {flights_1}, {src_1}, {dst_1}, {k_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
n_2 = 3
flights_2 = [[0,1,100],[1,2,100],[0,2,500]]
src_2 = 0
dst_2 = 2
k_2 = 1
expected_output_2 = 200

print("\nTest Case 2:")
output_2 = Solution().findCheapestPrice(n_2, flights_2, src_2, dst_2, k_2)
print(f"findCheapestPrice({n_2}, {flights_2}, {src_2}, {dst_2}, {k_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
n_3 = 3
flights_3 = [[0,1,100],[1,2,100],[0,2,500]]
src_3 = 0
dst_3 = 2
k_3 = 0
expected_output_3 = 500

print("\nTest Case 3:")
output_3 = Solution().findCheapestPrice(n_3, flights_3, src_3, dst_3, k_3)
print(f"findCheapestPrice({n_3}, {flights_3}, {src_3}, {dst_3}, {k_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

