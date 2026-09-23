class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.length:
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
            
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.arr:
            pop = self.arr[self.length - 1]
            self.arr[self.length - 1] = None
            self.length -= 1
            return pop

    def resize(self) -> None:
        self.capacity *= 2
        newArr = [None] * self.capacity
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
