# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def are_linked_lists_equal(head1, head2):
    current1, current2 = head1, head2
    while current1 and current2:
        if current1.val != current2.val:
            return False
        current1, current2 = current1.next, current2.next
    return current1 is None and current2 is None

values1 = [1, 2, 4]
values2 = [1, 3, 4]
expected_merged = [1, 1, 2, 3, 4, 4]

solution = Solution()

# Test case 1
list1 = create_linked_list(values1)
list2 = create_linked_list(values2)
merged = solution.mergeTwoLists(list1, list2)

print("Input List 1:", values1)
print("Input List 2:", values2)
print("Merged List:")
print_linked_list(merged)

if are_linked_lists_equal(merged, create_linked_list(expected_merged)):
    print("✅ Test passed")
else:
    print("❌ Test failed")

# Test case 2 (Empty Lists)
list1_empty = create_linked_list([])
list2_empty = create_linked_list([])
merged_empty = solution.mergeTwoLists(list1_empty, list2_empty)

print("\nInput List 1 (Empty):")
print_linked_list(list1_empty)
print("Input List 2 (Empty):")
print_linked_list(list2_empty)
print("Merged List (Empty):")
print_linked_list(merged_empty)

if are_linked_lists_equal(merged_empty, create_linked_list([])):
    print("✅ Test passed")
else:
    print("❌ Test failed")
