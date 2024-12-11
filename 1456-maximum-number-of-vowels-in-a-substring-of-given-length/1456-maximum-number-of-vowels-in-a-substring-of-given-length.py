class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_set = {'a','e','i','o','u'}

        left, count, res = 0,0,0
        for right in range(len(s)):
            if s[right] in vowel_set:
                count += 1

            if right - left + 1 > k:
                if s[left] in vowel_set:
                    count -= 1
                left += 1
            res = max(res,count)
        return res
        
