class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur, res = [], []
        remain = target
        def dfs(start, remain):
            if remain == 0:
                res.append(cur.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break
                cur.append(candidates[i])
                dfs(i + 1, remain - candidates[i])
                cur.pop()

        dfs(0, remain)
        return res