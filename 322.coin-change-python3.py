from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins.sort(reverse=True)
        res = 0
        for coin in coins:
            rem = amount // coin
            mod = amount % coin
            if rem > 0:
                res = res + rem
                print("""🧰   \x1b[1;31;40m322.coin-change-python3.py:15    rem:""") ## DELETEME:
                print(rem, coin) ## DELETEME:
                print('\x1b[0m') ## DELETEME:
                amount = amount - (coin * rem)
            if mod == 0:
                break
            print("""🙉   \x1b[1;30;43m322.coin-change-python3.py:18    amount:""") ## DELETEME:
            print(amount) ## DELETEME:
            print('\x1b[0m') ## DELETEME:
        if amount > 0:
            return -1
        return res
            


solution = Solution()

# Test Case 1
coins_1 = [1, 2, 5]
amount_1 = 11
expected_output_1 = 3
result_1 = solution.coinChange(coins_1, amount_1)

print("Test Case 1:")
print("Input:")
print("coins:", coins_1)
print("amount:", amount_1)
print("Output:", result_1)

if result_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
coins_2 = [2]
amount_2 = 3
expected_output_2 = -1
result_2 = solution.coinChange(coins_2, amount_2)

print("\nTest Case 2:")
print("Input:")
print("coins:", coins_2)
print("amount:", amount_2)
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
coins_3 = [1]
amount_3 = 0
expected_output_3 = 0
result_3 = solution.coinChange(coins_3, amount_3)

print("\nTest Case 3:")
print("Input:")
print("coins:", coins_3)
print("amount:", amount_3)
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")


# Test Case 4
coins_4 = [186,419,83,408]
amount_4 = 6249
expected_output_4 = 20
result_4 = solution.coinChange(coins_4, amount_4)

print("\nTest Case 4:")
print("Input:")
print("coins:", coins_4)
print("amount:", amount_4)
print("Output:", result_4)

if result_4 == expected_output_4:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output\Expected: ", expected_output_4)
