class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        length = float('inf')
        curSum = 0
        for R in range(len(nums)):
            curSum += nums[R]
            while curSum >= target:
                if (R - L + 1) < length:
                    length = R - L + 1
                curSum -= nums[L]
                L += 1
        return 0 if length == float('inf') else length