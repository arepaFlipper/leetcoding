# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

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
input_lists_1 = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6])
]
expected_output_1 = create_linked_list([1, 1, 2, 3, 4, 4, 5, 6])
result_1 = solution.mergeKLists(input_lists_1)

print("Test Case 1:")
print("Input:")
for input_list in input_lists_1:
    print_linked_list(input_list)

print("Output:")
print_linked_list(result_1)

if are_linked_lists_equal(result_1, expected_output_1):
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 2
input_lists_2 = []
expected_output_2 = None
result_2 = solution.mergeKLists(input_lists_2)

print("\nTest Case 2:")
print("Input: []")
print("Output:", result_2)

if result_2 == expected_output_2:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")

# Test Case 3
input_lists_3 = [[]]
expected_output_3 = None
result_3 = solution.mergeKLists(input_lists_3)

print("\nTest Case 3:")
print("Input: [[]]")
print("Output:", result_3)

if result_3 == expected_output_3:
    print("✅ Expected Output")
else:
    print("❌ Unexpected Output")
