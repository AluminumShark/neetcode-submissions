class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        hash = {}
        for i in range(n):
            hash[nums[i]] = 1 + hash.get(nums[i], 0)
            if hash[nums[i]] > 1:
                return nums[i]