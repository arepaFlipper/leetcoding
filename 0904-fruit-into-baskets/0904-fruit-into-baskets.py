class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int)
        left, total, res = 0,0,0
        for right in range(len(fruits)):
            count[fruits[right]] +=1
            total += 1

            while len(count) > 2:
                fruit = fruits[left]
                count[fruit] -= 1
                total -= 1
                left += 1
                if not count[fruit]:
                    count.pop(fruit)
            res = max(res, total)
        return res
