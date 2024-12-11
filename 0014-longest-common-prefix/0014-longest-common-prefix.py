class Solution:
    # def find_shortest(self, words: List[str]):
    #     shortest = words[0]
    #     for word in words:
    #         if len(shortest) > len(word):
    #             shortest = word
    #     return shortest

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix: str = ""
        count_chars: dict = defaultdict(int)
        for word in strs:
            for idx in range(len(word)):
                c:Char = word[idx]
                key: str = c + str(idx)
                count_chars[key] += 1
            
        shortest_word: str = strs[0]
        print("count_chars:",count_chars) ## DELETEME:
        for index in range(len(shortest_word)):
            char: Char = shortest_word[index]
            k: str = char + str(index)
            if count_chars[k] == len(strs):
                prefix += char
            else:
                break
        return prefix
