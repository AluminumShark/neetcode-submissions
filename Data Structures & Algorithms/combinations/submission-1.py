class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curComb, combs = [], []
        
        def dfs(i, n, k, curComb, combs):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return
            
            if i > n:
                return
            
            for j in range(i, n + 1):
                curComb.append(j)
                dfs(j + 1, n, k, curComb, combs)
                curComb.pop()
    
        dfs(1, n, k, curComb, combs)

        return combs