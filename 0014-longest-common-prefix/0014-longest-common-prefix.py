class Solution:
    def find_shortest(self, strs: List[str]):
        shortest = strs[0]
        for word in strs:
            if len(shortest) > len(word):
                shortest = word
        return shortest

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        idx = 0
        shortest_word = self.find_shortest(strs)
        print("shortest: ",shortest_word) ## DELETEME:
        while (idx < len(shortest_word)-1):
            char = shortest_word[idx]
            for word in strs:
                print("word: ",word) ## DELETEME:
                if char != word[idx]:
                    idx = len(shortest_word)
                    break
            prefix += char
            if (idx < len(shortest_word)):
                break
            idx += 1
            print("prefix: ",prefix) ## DELETEME:
        return prefix
