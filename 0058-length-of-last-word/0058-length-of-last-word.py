class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        size = len(s)
        idx = size -1
        while idx >= 0:
            c= s[idx]
            if c.isalpha():
                word += c
            elif len(word) > 0 :
                idx = 0
            idx -= 1
        return len(word)
