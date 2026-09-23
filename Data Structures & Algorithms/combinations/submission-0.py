class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curComb, combs = [], []
        
        def dfs(i, n, k, curComb, combs):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return
            
            if i > n:
                return
            
            curComb.append(i)
            dfs(i + 1, n, k, curComb, combs)

            curComb.pop()
            dfs(i + 1, n, k, curComb, combs)
        
        dfs(1, n, k, curComb, combs)

        return combs