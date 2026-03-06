# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        length = 0
        while current.next:
            length += 1
            current = current.next
        
        current = head
        for _ in range(length//2):
            current = current.next
        return current
