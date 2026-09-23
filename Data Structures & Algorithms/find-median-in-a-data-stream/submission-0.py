class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        if len(self.nums) % 2 == 0:
            idx1 = len(self.nums) // 2
            idx2 = idx1 - 1
            return (self.nums[idx1] + self.nums[idx2]) / 2
        else:
            idx = len(self.nums) // 2
            return self.nums[idx]

        