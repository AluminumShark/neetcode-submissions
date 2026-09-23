class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        windowSum = 0
        length = float('inf')

        for R in range(len(nums)):
            windowSum += nums[R]
            while windowSum >= target:
                length = min(length, R - L + 1)
                windowSum -= nums[L]
                L += 1

        return 0 if length == float('inf') else length