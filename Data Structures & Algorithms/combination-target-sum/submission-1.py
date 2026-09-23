class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        curComb, combs = [], []

        def dfs(start, remain):
            if remain == 0:
                combs.append(curComb.copy())
                return
            
            for i in range(start, len(nums)):
                x = nums[i]
                if x > remain:
                    break
                curComb.append(x)
                dfs(i, remain - x)
                curComb.pop()

        dfs(0, target)
        return combs
