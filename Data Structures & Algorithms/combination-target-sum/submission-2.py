class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur, res = [], []
        remain = target
        def dfs(i, cur, res, target, remain):
            if remain == 0:
                res.append(cur.copy())
                return
            
            if remain < 0 or i == len(nums):
                return
            
            cur.append(nums[i])
            remain -= nums[i]
            dfs(i, cur, res, target, remain)

            cur.pop()
            remain += nums[i]
            dfs(i + 1, cur, res, target, remain)

        dfs(0, cur, res, target, remain)
        return res