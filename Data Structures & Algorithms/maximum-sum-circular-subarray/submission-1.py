class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        curMax = maxSum = nums[0]
        curMin = minSum = nums[0]

        for i in nums[1:]:
            curMax = max(i, curMax + i)
            maxSum = max(curMax, maxSum)
            curMin = min(i, curMin + i)
            minSum = min(curMin, minSum)

        if maxSum < 0:
            return maxSum
        
        return max(maxSum, total - minSum)