I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

  212. Word Search II  
  Given an m x n board of characters and a list of strings words, return all words on the board.  
  Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.  
     
  Example 1:  
  https://assets.leetcode.com/uploads/2020/11/07/search1.jpg  
  Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]  
  Output: ["eat","oath"]  
  Example 2:  
  https://assets.leetcode.com/uploads/2020/11/07/search2.jpg  
  Input: board = [["a","b"],["c","d"]], words = ["abcb"]  
  Output: []  
     
  Constraints:  
  	m == board.length  
  	n == board[i].length  
  	1 <= m, n <= 12  
  	board[i][j] is a lowercase English letter.  
  	1 <= words.length <= 3 * 104  
  	1 <= words[i].length <= 10  
  	words[i] consists of lowercase English letters.  
  	All the strings of words are unique.  

The following is my solution to test:
```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        
    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else: 
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
