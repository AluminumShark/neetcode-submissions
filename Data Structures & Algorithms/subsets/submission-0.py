class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet, resSet = [], []
        def dfs(i, nums, curSet, resSet):
            if i == len(nums):
                resSet.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            dfs(i + 1, nums, curSet, resSet)

            curSet.pop()
            dfs(i + 1, nums, curSet, resSet)
        
        dfs(0, nums, curSet, resSet)
        return resSet