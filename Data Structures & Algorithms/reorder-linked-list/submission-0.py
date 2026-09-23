# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        dummy = ListNode(-1)
        curr = dummy
        L, R = 0, len(nodes) - 1
        while L < R:
            nodes[L].next = nodes[R]
            L += 1
            if L == R:
                break
            nodes[R].next = nodes[L]
            R -= 1
            
        nodes[L].next = None