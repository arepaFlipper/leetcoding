# @leet start
class Solution:
    def checkValidString(self, s: str) -> bool:
        dp: Dict = {(len(s), 0): True}

        def depth_first_search(idx, left):
            if idx == len(s) or left < 0:
                return left == 0
            if (idx,left) in dp:
                return dp[(idx, left)]

            if s[idx] == "(":
                dp[(idx, left)] = depth_first_search(idx+1, left +1)
            elif s[idx] == ")":
                dp[(idx,left)] = depth_first_search(idx +1, left -1)
            else: 
                dp[(idx, left)] = (
                    depth_first_search(idx+1, left +1) or depth_first_search(idx+1, left -1) or depth_first_search(idx+1, left)
                )
            return dp[(idx,left)]
        return depth_first_search(0,0)

# @leet end
# Test Case 1
s_1 = "()"
expected_output_1 = True

print("Test Case 1:")
output_1 = Solution().checkValidString(s_1)
print(f"checkValidString('{s_1}') => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
s_2 = "(*)"
expected_output_2 = True

print("\nTest Case 2:")
output_2 = Solution().checkValidString(s_2)
print(f"checkValidString('{s_2}') => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
s_3 = "(*))"
expected_output_3 = True

print("\nTest Case 3:")
output_3 = Solution().checkValidString(s_3)
print(f"checkValidString('{s_3}') => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

