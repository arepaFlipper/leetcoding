from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for (idx, num) in enumerate(nums):
            if num in hashmap:
                return [hashmap[num], idx]
            res = target - num
            hashmap[res] = idx




            
            

solution = Solution()

def testTwoSum():
    test_cases = [
        {
            "input": {
                "nums": [2,7,11,15],
                "target": 9
            },
            "output": [0, 1]
        },
        {
            "input": {
                "nums": [3,2,4],
                "target": 6
            },
            "output": [1, 2]
        },
        {
            "input": {
                "nums": [3,3],
                "target": 6
            },
            "output": [0, 1]
        }
    ]

    for idx, test in enumerate(test_cases):
        result = solution.twoSum(**test["input"])
        try:
            assert result.sort() == test["output"].sort(), f"Test {idx + 1} failed. Expected {test['output']}, but got {result}"
            print(f"Test {idx + 1} passed! ✅")
        except Exception as e:
            print(f"Test {idx + 1} failed with error: {e} ❌")


if __name__ == "__main__":
    testTwoSum()
