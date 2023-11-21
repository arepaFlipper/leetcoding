class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word: str):
        current = self
        current.refs += 1
        for char in word:
            if char not in current.children:
                 current.children[char] = TrieNode()
            current = current.children[char]
            current.refs += 1
        current.isWord = True

    def removeWord(self,word: str):
        current = self
        current.refs -= 1
        for char in word:
            if char in current.children:
                current = current.children[char]
                current.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        (ROWS,COLS) = (len(board), len(board[0]))
        (res,visit) = (set(),set())

        def dfs(row: List[str],char: List[str],node,word):
            if (
                row not in range(ROWS) or
                char not in range(COLS) or
                board[row][char] not in node.children or
                node.children[board[row][char]].refs < 1 or
                (row,char) in visit
            ):
                return

            value = board[row][char]
            visit.add((row,char))
            node = node.children[value]
            word += value

            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(row+1,char, node, word)
            dfs(row-1,char, node, word)
            dfs(row, char+1, node, word)
            dfs(row, char-1, node, word)
            visit.remove((row,char))

        for row in range(ROWS):
            for char in range(COLS):
                dfs(row,char, root,"")

        return list(res)
