# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        l, r = 0, len(arr) - 1
        dummy = ListNode()
        tail = dummy
        while l <= r:
            tail.next = ListNode(arr[l])
            tail = tail.next
            l += 1
            if l <= r:
                tail.next = ListNode(arr[r])
                tail = tail.next
                r -= 1
        head.next = dummy.next.next
            

