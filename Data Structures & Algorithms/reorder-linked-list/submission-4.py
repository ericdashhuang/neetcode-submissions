# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findmiddle(node):
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            second = slow.next
            slow.next = None
            return second
            #returns first node of second half, which is equal or smaller
        mid = findmiddle(head)

        def reverselist(node):
            prev, curr = None, node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        newhead = reverselist(mid)

        while newhead:
            temp1 = head.next 
            temp2 = newhead.next 
            head.next = newhead
            newhead.next = temp1
            head = temp1
            newhead = temp2
                    


