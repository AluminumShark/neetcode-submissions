class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]

        if obstacleGrid[n - 1][m - 1] == 1:
            return 0

        dp[n-1][m-1] = 1
        
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    continue
                
                if r < n - 1:
                    dp[r][c] += dp[r + 1][c]
                if c < m - 1:
                    dp[r][c] += dp[r][c + 1]

        return dp[0][0]