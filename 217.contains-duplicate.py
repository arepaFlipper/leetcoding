from typing import List 
# @leet start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = 1
        return False


        
# @leet end

solution = Solution()

def testContainsDuplicate():
    test_cases = [
        {
            "nums": [1, 2, 3, 1],
            "expected": True
        },
        {
            "nums": [1, 2, 3, 4],
            "expected": False
        },
        {
            "nums": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
            "expected": True
        }
    ]

    for idx, test in enumerate(test_cases):
        result = solution.containsDuplicate(test["nums"])

        try:
            assert result == test["expected"], f"Test {idx + 1} failed. Expected {test['expected']}, but got {result}"
            print(f"✅ Test {idx + 1} passed")
        except AssertionError:
            print(f"❌ Test {idx + 1} failed Expected {test['expected']}, but got {result}")

if __name__ == "__main__":
    testContainsDuplicate()
