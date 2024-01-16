# @leet start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2)+1) for i in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True

        for idx in range(len(s1), -1, -1):
            for jdx in range(len(s2), -1, -1):
                if idx < len(s1) and (s1[idx] == s3[idx + jdx]) and dp[idx+1][jdx]:
                    dp[idx][jdx] = True
                if jdx < len(s2) and s2[jdx] == s3[idx + jdx] and dp[idx][jdx +1]:
                    dp[idx][jdx] = True
        return dp[0][0]

# @leet end

solution = Solution()

# Test Case 1
s1_1 = "aabcc"
s2_1 = "dbbca"
s3_1 = "aadbbcbcac"
expected_output_1 = True

print("Test Case 1:")
output_1 = solution.isInterleave(s1_1, s2_1, s3_1)
print(f'isInterleave("{s1_1}", "{s2_1}", "{s3_1}") => Output:', output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
s1_2 = "aabcc"
s2_2 = "dbbca"
s3_2 = "aadbbbaccc"
expected_output_2 = False

print("\nTest Case 2:")
output_2 = solution.isInterleave(s1_2, s2_2, s3_2)
print(f'isInterleave("{s1_2}", "{s2_2}", "{s3_2}") => Output:', output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
s1_3 = ""
s2_3 = ""
s3_3 = ""
expected_output_3 = True

print("\nTest Case 3:")
output_3 = solution.isInterleave(s1_3, s2_3, s3_3)
print(f'isInterleave("{s1_3}", "{s2_3}", "{s3_3}") => Output:', output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
