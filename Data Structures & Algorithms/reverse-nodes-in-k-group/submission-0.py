# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.getkthnode(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            cur = group_prev.next
            prev = group_next
            tail = cur
            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            group_prev.next = prev
            group_prev = tail
        return dummy.next

    def getkthnode(self, start, k):
        while start and k > 0:
            start = start.next
            k -= 1
        return start