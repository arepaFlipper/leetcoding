# @leet start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        cache[len(s)][len(p)] = True

        for idx in range(len(s), -1, -1):
            for jdx in range(len(p) - 1, -1, -1):
                match = idx < len(s) and (s[idx] == p[jdx] or p[jdx] == ".")

                if (jdx + 1) < len(p) and p[jdx + 1] == "*":
                    cache[idx][jdx] = cache[idx][jdx + 2]
                    if match:
                        cache[idx][jdx] = cache[idx + 1][jdx] or cache[idx][jdx]
                elif match:
                    cache[idx][jdx] = cache[idx + 1][jdx + 1]
        return cache[0][0]

# @leet end

solution = Solution()

# Test Case 1
s_1, p_1 = "aa", "a"
expected_output_1 = False

print("Test Case 1:")
output_1 = solution.isMatch(s_1, p_1)
print(f"isMatch('{s_1}', '{p_1}') => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
s_2, p_2 = "aa", "a*"
expected_output_2 = True

print("\nTest Case 2:")
output_2 = solution.isMatch(s_2, p_2)
print(f"isMatch('{s_2}', '{p_2}') => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
s_3, p_3 = "ab", ".*"
expected_output_3 = True

print("\nTest Case 3:")
output_3 = solution.isMatch(s_3, p_3)
print(f"isMatch('{s_3}', '{p_3}') => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

