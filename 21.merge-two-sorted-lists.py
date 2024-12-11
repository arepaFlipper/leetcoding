from typing import Optional
# @leet start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = res = ListNode()
        

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return res.next

        
# @leet end



# Helper functions to convert between list and ListNode
def list_to_nodes(lst):
    if not lst:
        return None
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def nodes_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Test functions
def test_merge_two_lists_case_1():
    solution = Solution()
    list1 = list_to_nodes([1, 2, 4])
    list2 = list_to_nodes([1, 3, 4])
    expected = [1, 1, 2, 3, 4, 4]
    result = nodes_to_list(solution.mergeTwoLists(list1, list2))
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 1 succeed 👍")

def test_merge_two_lists_case_2():
    solution = Solution()
    list1 = list_to_nodes([])
    list2 = list_to_nodes([])
    expected = []
    result = nodes_to_list(solution.mergeTwoLists(list1, list2))
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 2 succeed 👍")

def test_merge_two_lists_case_3():
    solution = Solution()
    list1 = list_to_nodes([])
    list2 = list_to_nodes([0])
    expected = [0]
    result = nodes_to_list(solution.mergeTwoLists(list1, list2))
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Case 3 succeed 👍")

def main():
    # Simulate running tests
    test_merge_two_lists_case_1()
    test_merge_two_lists_case_2()
    test_merge_two_lists_case_3()

if __name__ == "__main__":
    main()
