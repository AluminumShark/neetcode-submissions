class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur, res = [], []
        def dfs(i, cur, res, nums):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i + 1, cur, res, nums)

            cur.pop()
            dfs(i + 1, cur, res, nums)
        dfs(0, cur, res, nums)
        return res