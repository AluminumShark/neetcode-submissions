class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(k):
            if k == 0:
                return 1

            if k < 0:
                return 0

            return dfs(k - 1) + dfs(k - 2)

        return dfs(n)