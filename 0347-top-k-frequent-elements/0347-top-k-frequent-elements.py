
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map: dict = defaultdict(int)
        frequencies: list = [[] for i in range(len(nums)+1)]

        for num in nums:
            hash_map[num] = 1 + hash_map.get(num,0)

        for key, value in hash_map.items():
            frequencies[value].append(key)

        res = []
        for frequency in range(len(frequencies)-1,0,-1):
            for n in frequencies[frequency]:
                res.append(n)
                if len(res) == k:

        return res
