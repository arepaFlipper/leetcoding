from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        slow.next = None
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        (first, second ) = (head, prev)
        while second:
            (tmp1, tmp2) = (first.next, second.next)
            first.next = second
            second.next = tmp1
            (first, second) = (tmp1, tmp2)

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

values1 = [1,2,3,4]
expected1 = [1,4,2,3]
values2 = [1,2,3,4,5]
expected2 = [1,5,2,4,3]

solution = Solution()

# Test case 1
head1 = create_linked_list(values1)
copy1 = create_linked_list(values1)  # Create a copy to compare later
solution.reorderList(head1)

print("Input:", values1)
print("Output:")
print_linked_list(head1)

if are_linked_lists_equal(head1, create_linked_list(expected1)):
    print("✅ Expected:", expected1)
else:
    print("❌ Expected:", expected1)

# Test case 2
head2 = create_linked_list(values2)
copy2 = create_linked_list(values2)  # Create a copy to compare later
solution.reorderList(head2)

print("\nInput:", values2)
print("Output:")
print_linked_list(head2)

if are_linked_lists_equal(head2, create_linked_list(expected2)):
    print("✅ Expected:", expected2)
else:
    print("❌ Expected:", expected2)

