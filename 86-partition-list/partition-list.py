# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
    
        small = []
        big = []
        current = head
        while current:
            if current.val < x:
                small.append(current.val)
            current = current.next

        current = head  
        while current:
            if current.val >=x:
                big.append(current.val)
            current = current.next
        small.extend(big)
        
        dummy = ListNode(-1)
        cur = dummy

        for num in small:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next
        

