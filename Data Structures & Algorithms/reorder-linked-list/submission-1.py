# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        S, F = head, head
        while F and F.next:
            S = S.next
            F = F.next.next
        
        prev, cur = None, S
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        

        list1, list2 = head, prev
        while list2.next:
            tmp1 = list1.next
            tmp2 = list2.next

            list1.next = list2
            list2.next = tmp1

            list1 = tmp1
            list2 = tmp2
        