class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        if self.q1:
            self.q2.append(x)
            for i in self.q1:
                self.q2.append(i)
            self.q1 = self.q2
            self.q2 = []
        else:
            self.q1.append(x)


    def pop(self) -> int:
        if not self.q1:
            return
        pop = self.q1[0]
        for i in range(1, len(self.q1)):
            self.q2.append(self.q1[i])
        self.q1 = self.q2
        self.q2 = []
        return pop

    def top(self) -> int:
        if not self.q1:
            return
        return self.q1[0]

    def empty(self) -> bool:
        return False if self.q1 else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()