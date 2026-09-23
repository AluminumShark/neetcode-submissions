class prefixSum:
    def __init__(self, nums: List):
        self.prefix = []
        curSum = 0
        for n in nums:
            curSum += n
            self.prefix.append(curSum)

    def rangeSum(self, L: int, R: int):
        if L > R:
            return 0
        rightSum = self.prefix[R]
        leftSum = self.prefix[L - 1] if L > 0 else 0
        return rightSum - leftSum

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixArr = prefixSum(nums)
        for i in range(n):
            leftSum = prefixArr.rangeSum(0, i - 1)
            rightSum = prefixArr.rangeSum(i + 1, n - 1)
            if leftSum == rightSum:
                return i
        return -1