from typing import Optional

# @leet start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       (prev, current) = (None, head)

        while curr:
            next = current.next
            current.next = prev
            prev = next
            current.val = prev.val
        
# @leet end

# Helper functions to create a linked list from a list and to convert a linked list to a list
def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

# Test functions
def test_reverse_list_case_1():
    solution = Solution()
    head = list_to_linked_list([1, 2, 3, 4, 5])
    expected = [5, 4, 3, 2, 1]
    result = solution.reverseList(head)
    result_list = linked_list_to_list(result)
    assert result_list == expected, f"Expected {expected}, but got {result_list}"
    print("Case 1 succeed 👍")

def test_reverse_list_case_2():
    solution = Solution()
    head = list_to_linked_list([1, 2])
    expected = [2, 1]
    result = solution.reverseList(head)
    result_list = linked_list_to_list(result)
    assert result_list == expected, f"Expected {expected}, but got {result_list}"
    print("Case 2 succeed 👍")

def test_reverse_list_case_3():
    solution = Solution()
    head = list_to_linked_list([])
    expected = []
    result = solution.reverseList(head)
    result_list = linked_list_to_list(result)
    assert result_list == expected, f"Expected {expected}, but got {result_list}"
    print("Case 3 succeed 👍")

def main():
    # Simulate running tests
    test_reverse_list_case_1()
    test_reverse_list_case_2()
    test_reverse_list_case_3()

if __name__ == "__main__":
    main()

