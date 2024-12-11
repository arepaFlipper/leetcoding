# @leet start
from typing import List
import heapq

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
            print("""🫖   \x1b[1;33;40m   min_h:""") ## DELETEME:
            print(min_h) ## DELETEME:
            print('\x1b[0m') ## DELETEME:
            first = min_h[0]
            print("🏫   \x1b[1;30;45m first:", first, '\x1b[0m') ## DELETEME:
            print("🟡\x1b[1;34;40m range:", first, " -> ", first + groupSize , "\x1b[0m") ## DELETEME:
            for idx in range(first, first + groupSize):
                print("💟   \x1b[1;32;40m idx: ", idx) ## DELETEME:
                if idx not in count: 
                    print("📵   \x1b[1;31;40m idx:", idx , '\x1b[0m') ## DELETEME:
                    return False
                count[idx] -= 1
                print("🧑\x1b[1;37;40m decrease count of idx:", idx, ", now count:", count, '\x1b[0m') ## DELETEME:
                if count[idx] == 0:
                    if idx != min_h[0]:
                        print("📵📵   \x1b[1;31;40m idx:", idx , ', min_h[0]: ', min_h[0],  '\x1b[0m') ## DELETEME:
                        return False
                    heapq.heappop(min_h)
                    print("🦨   \x1b[1;35;40m remove idx key:", idx," min_h:", min_h, '\x1b[0m') ## DELETEME:
                    print(min_h) ## DELETEME:
                    print('\x1b[0m') ## DELETEME:
        return True
# @leet end
# # Test Case 1
# hand_1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
# groupSize_1 = 3
# expected_output_1 = True
#
# print("Test Case 1:")
# output_1 = Solution().isNStraightHand(hand_1, groupSize_1)
# print(f"isNStraightHand({hand_1}, {groupSize_1}) => Output:", output_1)
#
# if output_1 == expected_output_1:
#     print("✅ Expected Output")
# else:
#     print("❌ Unexpected Output")
#
# # Test Case 2
# hand_2 = [1, 2, 3, 4, 5]
# groupSize_2 = 4
# expected_output_2 = False
#
# print("\nTest Case 2:")
# output_2 = Solution().isNStraightHand(hand_2, groupSize_2)
# print(f"isNStraightHand({hand_2}, {groupSize_2}) => Output:", output_2)
#
# if output_2 == expected_output_2:
#     print("✅ Expected Output")
# else:
#     print("❌ Unexpected Output")
#
# Test Case 3
hand_3 = [1, 1, 2, 2, 3, 3]
groupSize_3 = 2
expected_output_3 = False

print("\nTest Case 3:")
output_3 = Solution().isNStraightHand(hand_3, groupSize_3)
print(f"isNStraightHand({hand_3}, {groupSize_3}) => Output:", output_3)

if output_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

