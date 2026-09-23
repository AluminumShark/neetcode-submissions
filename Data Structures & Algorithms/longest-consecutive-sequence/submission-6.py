class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numSet = set(nums)
        res = 0

        for n in numSet:
            if n - 1 not in numSet:
                cur = n
                cnt = 1
            
                while cur + 1 in numSet:
                    cnt += 1
                    cur += 1

                res = max(res, cnt)

        return res