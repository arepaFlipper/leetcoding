I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

              https://leetcode.com/problems/partition-labels/
                                      
                           763. Partition Labels
             Medium | 10127  377  | 79.8% of 645.3K | 󰛨 Hints



You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.



󰛨 Example 1:

	▎ Input: s = "ababcbacadefegdehijhklij"
	▎ Output: [9,7,8]
	▎ Explanation:
	▎ The partition is "ababcbaca", "defegde", "hijhklij".
	▎ This is a partition so that each letter appears in at most one part.
	▎ A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

󰛨 Example 2:

	▎ Input: s = "eccbbbbdec"
	▎ Output: [10]



 Constraints:

	* 1 <= s.length <= 500
	
	* s consists of lowercase English letters.






The following is my solution to test:

```
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
```
