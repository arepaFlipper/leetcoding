from typing import List

# @leet start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache: Dict = {}

        def depth_first_search(idx, target):
            if target == amount:
                return 1
            
            if target > amount:
                return 0
        
            if idx == len(coins):
                return 0

            if (idx, target) in cache:
                return cache[(idx, target)]
    
            cache[(idx, target)] = depth_first_search(idx, target + coins[idx]) + depth_first_search(idx + 1, target)
            return cache[(idx, target)]

        return depth_first_search(0, 0)

# @leet end

solution = Solution()

# Test Case 1
amount_1 = 5
coins_1 = [1, 2, 5]
expected_output_1 = 4

print("Test Case 1:")
output_1 = solution.change(amount_1, coins_1)
print(f'change({amount_1}, {coins_1}) => Output:', output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
amount_2 = 3
coins_2 = [2]
expected_output_2 = 0

print("\nTest Case 2:")
output_2 = solution.change(amount_2, coins_2)
print(f'change({amount_2}, {coins_2}) => Output:', output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
amount_3 = 10
coins_3 = [10]
expected_output_3 = 1

print("\nTest Case 3:")
output_3 = solution.change(amount_3, coins_3)
print(f'change({amount_3}, {coins_3}) => Output:', output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
