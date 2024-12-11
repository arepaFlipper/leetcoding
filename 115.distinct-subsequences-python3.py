# @leet start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache: Dict = {}

        for idx in range(len(s) + 1):
            cache[(idx, len(t))] = 1
        for jdx in range(len(t)):
            cache[(len(s), jdx)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]
# @leet end

solution = Solution()

# Test Case 1
s_1, t_1 = "rabbbit", "rabbit"
expected_output_1 = 3

print("Test Case 1:")
output_1 = solution.numDistinct(s_1, t_1)
print(f'numDistinct("{s_1}", "{t_1}") => Output:', output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
s_2, t_2 = "babgbag", "bag"
expected_output_2 = 5

print("\nTest Case 2:")
output_2 = solution.numDistinct(s_2, t_2)
print(f'numDistinct("{s_2}", "{t_2}") => Output:', output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

