# @leet start
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count: Dict = {}
        res: List = []
        (idx, length ) = (0, len(s))
        for jdx in range(length):
            char = s[jdx]
            count[char] = jdx

        cur_len = 0
        goal = 0
        while idx < length:
            char = s[idx]
            goal = max(goal, count[char])
            cur_len += 1

            if goal == idx:
                res.append(cur_len)
                cur_len = 0
            idx += 1
        return res
# @leet end

# Test Case 1
s_1 = "ababcbacadefegdehijhklij"
expected_output_1 = [9, 7, 8]

print("Test Case 1:")
output_1 = Solution().partitionLabels(s_1)
print(f"partitionLabels('{s_1}') => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
s_2 = "eccbbbbdec"
expected_output_2 = [10]

print("\nTest Case 2:")
output_2 = Solution().partitionLabels(s_2)
print(f"partitionLabels('{s_2}') => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
