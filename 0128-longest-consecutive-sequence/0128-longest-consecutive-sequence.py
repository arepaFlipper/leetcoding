class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map: Dict = {}
        for (idx, num) in enumerate(nums):
            print("(idx,num)",idx, num) ## DELETEME:
            hash_map[num]=True

        print("hash_map:",hash_map) ## DELETEME:
        res = 0
        for (key,value) in hash_map.items():
            count = 0
            print("key:",key) ## DELETEME:
            for i in range(key, len(nums)+1):
                print(i,"in hash_map",i in hash_map) ## DELETEME:
                if i in hash_map:
                    count += 1
                else:
                    break
            if count > res:
                res= count
        return res
