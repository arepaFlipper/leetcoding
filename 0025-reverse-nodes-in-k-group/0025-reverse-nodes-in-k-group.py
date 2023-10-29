# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.getKth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            (prev, curr) = (kth.next, group_prev.next)

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

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

solution = Solution()

# Test Case 1
input_head_1 = create_linked_list([1, 2, 3, 4, 5])
k_1 = 2
expected_output_1 = create_linked_list([2, 1, 4, 3, 5])
result_1 = solution.reverseKGroup(input_head_1, k_1)

print("Test Case 1:")
print("Input:")
print_linked_list(input_head_1)
print("Output:")
print_linked_list(result_1)

if are_linked_lists_equal(result_1, expected_output_1):
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_head_2 = create_linked_list([1, 2, 3, 4, 5])
k_2 = 3
expected_output_2 = create_linked_list([3, 2, 1, 4, 5])
result_2 = solution.reverseKGroup(input_head_2, k_2)

print("\nTest Case 2:")
print("Input:")
print_linked_list(input_head_2)
print("Output:")
print_linked_list(result_2)

if are_linked_lists_equal(result_2, expected_output_2):
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

