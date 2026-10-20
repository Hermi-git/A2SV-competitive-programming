# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        merged = ListNode(0, None)
        tail = merged
        minheap = []
        unique_order = 0

        for lst in lists:
            if lst is not None:
                heapq.heappush(minheap, (lst.val, unique_order, lst))
                unique_order += 1
        while minheap:
            nodeVal, order, node = heapq.heappop(minheap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(minheap, (node.next.val, order, node.next))
                order += 1
        tail.next = None
        return merged.next
