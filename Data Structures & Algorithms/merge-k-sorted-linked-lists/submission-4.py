import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = cur = ListNode(-1)

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        cur.next = None
        return dummy.next