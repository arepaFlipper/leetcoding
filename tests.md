I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

                 https://leetcode.com/problems/word-ladder/
                                      
                              127. Word Ladder
                   Hard | 11673  1853  | 38.6% of 2.6M



A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s_1 -> s_2 -> ... -> s_k such that:

	* Every adjacent pair of words differs by a single letter.
	
	* Every s_i for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
	
	* s_k == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



󰛨 Example 1:

	▎ Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
	▎ Output: 5
	▎ Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

󰛨 Example 2:

	▎ Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
	▎ Output: 0
	▎ Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.



 Constraints:

	* 1 <= beginWord.length <= 10
	
	* endWord.length == beginWord.length
	
	* 1 <= wordList.length <= 5000
	
	* wordList[i].length == beginWord.length
	
	* beginWord, endWord, and wordList[i] consist of lowercase English letters.
	
	* beginWord != endWord
	
	* All the words in wordList are unique.





The following is my solution to test:

```
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
```
