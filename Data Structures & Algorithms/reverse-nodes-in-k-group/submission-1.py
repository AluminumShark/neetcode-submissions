# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        groupPrev = dummy

        while True:
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            groupNext = kth.next
            groupStart = groupPrev.next

            prev = groupNext
            cur = groupStart
            while cur != groupNext:
                nxt = cur.next
                cur.next = prev
                prev = cur 
                cur = nxt

            groupPrev.next = kth
            groupPrev = groupStart