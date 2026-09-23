class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curSet, resSet = [], []
        
        def dfs(i, nums, curSet, resSet):
            if i == len(nums):
                resSet.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            dfs(i + 1, nums, curSet, resSet)

            curSet.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, nums, curSet, resSet)
        
        dfs(0, nums, curSet, resSet)
        return resSet