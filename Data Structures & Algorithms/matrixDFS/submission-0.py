class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            
            if grid[r][c] == 1 or (r, c) in visit:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visit.add((r, c))

            count = 0
            count += dfs(r + 1, c, visit)
            count += dfs(r - 1, c, visit)
            count += dfs(r, c + 1, visit)
            count += dfs(r, c - 1, visit)

            visit.remove((r, c))

            return count
        
        return dfs(0, 0, set())