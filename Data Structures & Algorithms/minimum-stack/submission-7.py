class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mstack or self.mstack[-1] >= val:
            self.mstack.append(val)

    def pop(self) -> None:
        pop = self.stack.pop()
        if self.mstack and self.mstack[-1] == pop:
            self.mstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.mstack:
            return self.mstack[-1]

