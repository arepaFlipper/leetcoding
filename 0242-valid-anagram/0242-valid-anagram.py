class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = defaultdict(int) 
        count_t = defaultdict(int) 
        for c in s:
            count_s[c] = count_s[c] + 1

        for char in t:
            if char not in count_s:
                return False
            count_t[char] = count_t[char] + 1

        print(count_t) ## DELETEME:
        print(count_s) ## DELETEME:

        for el in t:
            if count_t[el] != count_s[el]:
                return False
        return True
