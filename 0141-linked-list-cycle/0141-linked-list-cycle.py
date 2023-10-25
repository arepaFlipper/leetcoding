# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

def create_linked_list(values, pos):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    loop_node = None

    if pos == -1:
        loop_node = None
    else:
        loop_index = 0
        loop_node = head
        while loop_index < pos:
            loop_node = loop_node.next
            loop_index += 1

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    if loop_node:
        current.next = loop_node

    return head

# Test case 1
values1 = [3, 2, 0, -4]
pos1 = 1
expected_result1 = True

solution = Solution()
list1 = create_linked_list(values1, pos1)
result1 = solution.hasCycle(list1)

print("Input List 1:", values1)
print("Position of Cycle:", pos1)
print("Has Cycle:")
print(result1)

if result1 == expected_result1:
    print("✅ Test passed")
else:
    print("❌ Test failed")

# Test case 2
values2 = [1, 2]
pos2 = 0
expected_result2 = True

list2 = create_linked_list(values2, pos2)
result2 = solution.hasCycle(list2)

print("\nInput List 2:", values2)
print("Position of Cycle:", pos2)
print("Has Cycle:")
print(result2)

if result2 == expected_result2:
    print("✅ Test passed")
else:
    print("❌ Test failed")

# Test case 3 (No Cycle)
values3 = [1]
pos3 = -1
expected_result3 = False

list3 = create_linked_list(values3, pos3)
result3 = solution.hasCycle(list3)

print("\nInput List 3:", values3)
print("Position of Cycle:", pos3)
print("Has Cycle:")
print(result3)

if result3 == expected_result3:
    print("✅ Test passed")
else:
    print("❌ Test failed")

