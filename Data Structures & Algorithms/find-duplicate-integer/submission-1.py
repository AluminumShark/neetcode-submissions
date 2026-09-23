class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for i in range(n):
            cur = nums[i]
            freq[cur] = 1 + freq.get(cur, 0)
            if freq[cur] > 1:
                return nums[i]