from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: List[List [str]] = []
        hash_map= {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hash_map:
                hash_map[sorted_word].append(word)
            else:
                hash_map[sorted_word] = [word]

        for group in hash_map.values():
            groups.append(group)

        return groups
