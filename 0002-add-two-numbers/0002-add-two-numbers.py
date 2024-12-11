# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

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

# Test case 1
values1 = [2, 4, 3]
values2 = [5, 6, 4]
expected_sum = [7, 0, 8]

solution = Solution()
list1 = create_linked_list(values1)
list2 = create_linked_list(values2)
sum_list = solution.addTwoNumbers(list1, list2)

print("Input List 1:", values1)
print("Input List 2:", values2)
print("Sum List:")
print_linked_list(sum_list)

if are_linked_lists_equal(sum_list, create_linked_list(expected_sum)):
    print("✅ Test passed")
else:
    print("❌ Test failed")

# Test case 2 (Empty Lists)
values1_empty = []
values2_empty = []
expected_sum_empty = []

list1_empty = create_linked_list(values1_empty)
list2_empty = create_linked_list(values2_empty)
sum_list_empty = solution.addTwoNumbers(list1_empty, list2_empty)

print("\nInput List 1 (Empty):")
print_linked_list(list1_empty)
print("Input List 2 (Empty):")
print_linked_list(list2_empty)
print("Sum List (Empty):")
print_linked_list(sum_list_empty)

if are_linked_lists_equal(sum_list_empty, create_linked_list(expected_sum_empty)):
    print("✅ Test passed")
else:
    print("❌ Test failed")

