class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(k, n + 1):
            cur = max(nums[i - k : i])
            ans.append(cur)
        return ans