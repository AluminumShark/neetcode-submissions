# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        return self.mergeRange(lists, 0, len(lists) - 1)

    def mergeRange(self, lists, left, right):
        if left == right:
            return lists[left]

        mid = (left + right) // 2

        L = self.mergeRange(lists, left, mid)
        R = self.mergeRange(lists, mid+1, right)

        return self.mergeTwoLists(L, R)

    def mergeTwoLists(self, L, R):
        dummyHead = ListNode()
        tail = dummyHead

        while L and R:
            if L.val <= R.val:
                tail.next = L
                L = L.next
            else:
                tail.next = R
                R = R.next
            tail = tail.next
            
        tail.next = L or R
        return dummyHead.next