# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        return self.mergeRange(lists, 0, len(lists) - 1)
    def mergeRange(self, lists, left, right):
        if left == right:
            return lists[left]
        
        mid = (left + right) // 2

        L = self.mergeRange(lists, left, mid)
        R = self.mergeRange(lists, mid + 1, right)

        return self.mergeTwoLists(L, R)

    def mergeTwoLists(self, list1, list2):
        dummy = cur = ListNode(-1)

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 or list2
        return dummy.next