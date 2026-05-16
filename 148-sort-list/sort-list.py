# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge_sort(node):
            if not node or not node.next:
                return node

            slow = fast = node
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            mid = slow

            if prev:
                prev.next = None

            left = merge_sort(node)
            right = merge_sort(mid)

            return merge(left, right)

        def merge(left, right):
            dummy = ListNode(0)
            curr = dummy

            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next

            if left:
                curr.next = left
            if right:
                curr.next = right

            return dummy.next

        return merge_sort(head)