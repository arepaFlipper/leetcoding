from typing import List, collections
from queue import deque

# @leet start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
    
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei_word in nei[pattern]:
                        if nei_word not in visit:
                            visit.add(nei_word)
                            q.append(nei_word)
            res += 1
        return 0
# @leet end

# Test Case 1
beginWord_1 = "hit"
endWord_1 = "cog"
wordList_1 = ["hot", "dot", "dog", "lot", "log", "cog"]
expected_output_1 = 5

print("Test Case 1:")
solution_instance = Solution()
output_1 = solution_instance.ladderLength(beginWord_1, endWord_1, wordList_1)
print(f"ladderLength('{beginWord_1}', '{endWord_1}', {wordList_1}) => Output:", output_1)

if output_1 == expected_output_1:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
beginWord_2 = "hit"
endWord_2 = "cog"
wordList_2 = ["hot", "dot", "dog", "lot", "log"]
expected_output_2 = 0

print("\nTest Case 2:")
solution_instance = Solution()
output_2 = solution_instance.ladderLength(beginWord_2, endWord_2, wordList_2)
print(f"ladderLength('{beginWord_2}', '{endWord_2}', {wordList_2}) => Output:", output_2)

if output_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

