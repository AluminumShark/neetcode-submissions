class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        path = []

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                    
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                path.append(nums[i])
                used[i] = True
                dfs()

                path.pop()
                used[i] = False
        dfs()
        return res