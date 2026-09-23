class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        cur = self.head
        for i in range(index + 1):
            cur = cur.next

        return cur.val

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        self.size += 1

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size or index < 0:
            return False

        cur = self.head
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1

        return True

    def getValues(self) -> List[int]:
        res = []
        cur = self.head
        for i in range(self.size):
            cur = cur.next
            res.append(cur.val)
        
        return res
        
