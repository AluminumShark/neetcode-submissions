# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        S, F = dummy, dummy

        for _ in range(n):
            F = F.next

        while F.next:
            S = S.next
            F = F.next

        S.next = S.next.next

        return dummy.next