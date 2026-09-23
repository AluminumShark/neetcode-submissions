class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        curComb, combs = [], []
        
        def dfs(i, nums, target, curComb, combs):
            if i == len(nums):
                return
            
            if sum(curComb) == target:
                combs.append(curComb.copy())
                return
            elif sum(curComb) > target:
                return
            
            curComb.append(nums[i])
            dfs(i, nums, target, curComb, combs)

            curComb.pop()
            dfs(i + 1, nums, target, curComb, combs)
        
        dfs(0, nums, target, curComb, combs)

        return combs