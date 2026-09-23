class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return
        
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            
            if grid[r][c] != 1:
                return 0

            grid[r][c] = 0

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        ans = []
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    ans.append(dfs(i, j))

        return max(ans) if ans else 0
