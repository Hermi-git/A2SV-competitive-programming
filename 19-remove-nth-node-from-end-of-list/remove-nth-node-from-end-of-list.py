# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        def nthElementFromRight(h, n):
            nonlocal dummy
            aheadptr = head
            while n > 0:
                aheadptr = aheadptr.next
                n -= 1
            behindptr = dummy
            while aheadptr:
                aheadptr = aheadptr.next
                behindptr = behindptr.next
            return behindptr
        
        node = nthElementFromRight(head, n)  
        node.next = node.next.next
        return dummy.next