I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

              https://leetcode.com/problems/hand-of-straights/
                                      
                           846. Hand of Straights
                  Medium | 2454  170  | 55.9% of 274.9K



Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the i^th card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.



󰛨 Example 1:

	▎ Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
	▎ Output: true
	▎ Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

󰛨 Example 2:

	▎ Input: hand = [1,2,3,4,5], groupSize = 4
	▎ Output: false
	▎ Explanation: Alice's hand can not be rearranged into groups of 4.



 Constraints:

	* 1 <= hand.length <= 10^4
	
	* 0 <= hand[i] <= 10^9
	
	* 1 <= groupSize <= hand.length



Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/




The following is my solution to test:

```
# @leet start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0)

        min_h: List = list(count.keys())
        heapq.heapify(min_h)
        while min_h:
            first = min_h[0]
            for idx in range(first, first + groupSize):
                if idx not in count: 
                    return False
                count[idx] -= 1
                if count[idx] == 0:
                    if idx != min_h[0]:
                        return False
                    heapq.heappop(min_h)
        return True
# @leet end
```
