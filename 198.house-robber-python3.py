from typing import List

# @leet start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robFrom(idx, memo):
            # NOTE: Base case where there are no more houses left to rob
            if idx >= len(nums):
                return 0, []
            
            # NOTE: Check if we already have the result for this index.

            if idx in memo:
                return memo[idx]
            
            # NOTE: Rob the current house and move to the house two steps ahead
            (rob_current, rob_current_list) = robFrom(idx + 2, memo)
            rob_current += nums[idx]
            rob_current_list = [idx] + rob_current_list


            # NOTE: Skip the current house and move to the next house
            (skip_current, skip_current_list) = robFrom(idx+1, memo)

            if rob_current > skip_current:
                result = (rob_current, rob_current_list)
            else:
                result = (skip_current, skip_current_list)

            memo[idx] = result
            print("""🐻   \x1b[1;33;40m198.house-robber-python3.py:25   memo:""") ## DELETEME:
            print(memo) ## DELETEME:
            print('\x1b[0m') ## DELETEME:

            return result

        memo = {}

        (max_money, houses_robbed) = robFrom(0, memo)
        print("""🦜   \x1b[1;32;40m198.house-robber-python3.py:40   houses_robbed:""") ## DELETEME:
        print(houses_robbed) ## DELETEME:
        print('\x1b[0m') ## DELETEME:
        return max_money
        
# @leet end

# Test Case 1
test_input_1_nums = [1, 2, 3, 1]
expected_output_1 = 4
actual_output_1 = Solution().rob(test_input_1_nums)
print("Test Case 1:")
print(f"Input: nums = {test_input_1_nums}")
print(f"Output: {actual_output_1}")
print(f"Expected: {expected_output_1}")
if actual_output_1 == expected_output_1:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

# Test Case 2
test_input_2_nums = [2, 7, 9, 3, 1]
expected_output_2 = 12
actual_output_2 = Solution().rob(test_input_2_nums)
print("\nTest Case 2:")
print(f"Input: nums = {test_input_2_nums}")
print(f"Output: {actual_output_2}")
print(f"Expected: {expected_output_2}")
if actual_output_2 == expected_output_2:
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")

