class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        res = 0

        left = 0
        max_freq = 0

        for right in range(len(s)):
            freqs[s[right]] = 1 + freqs.get(s[right], 0)
            max_freq = max(max_freq, freqs[s[right]] )

            while (right - left + 1 ) - max_freq > k:
                freqs[s[left]] -= 1
                left += 1

            res= max(res, right-left +1)
        return res
