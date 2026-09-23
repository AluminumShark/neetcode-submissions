class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self) -> bool:
        return False if self.size else True

    def append(self, value: int) -> None:
        prev = self.tail.prev
        next = self.tail
        newNode = ListNode(value)
        
        prev.next = newNode
        newNode.prev = prev

        newNode.next = next
        next.prev = newNode

        self.size += 1

    def appendleft(self, value: int) -> None:
        prev = self.head
        next = self.head.next
        newNode = ListNode(value)

        prev.next = newNode
        newNode.prev = prev

        newNode.next = next
        next.prev = newNode

        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        pop = self.tail.prev
        prev = self.tail.prev.prev
        next = self.tail

        prev.next = next
        next.prev = prev

        self.size -= 1

        return pop.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
            
        pop = self.head.next
        prev = self.head
        next = self.head.next.next

        prev.next = next
        next.prev = prev

        self.size -= 1

        return pop.val
        
        
