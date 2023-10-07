# Definition for singly-linked list.
# class ListNode: k
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
