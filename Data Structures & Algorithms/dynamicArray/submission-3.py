class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.length:
            self.arr[i] = n
    
    # 要增加一個變數 length 紀錄 array 長度
    # 因為一開始初始化 self.arr = [None] * self.capacity 的時候
    # 長度就等於 capacity, None 會被當成長度
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.arr:
            pop = self.arr[self.length-1] # 不能用index -1 會取到 None
            self.arr[-1] = None
            self.length -= 1
            return pop

    # resize 要先擴大 capacity 再初始化新的記憶體空間 然後用新的 array 取代舊的
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