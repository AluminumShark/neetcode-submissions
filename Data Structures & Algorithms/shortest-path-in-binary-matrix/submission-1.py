from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        dirs = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        queue = deque()
        queue.append((0, 0, 1))
        
        visit = set()
        visit.add((0, 0))

        while queue:
            r, c, length = queue.popleft()

            if r == n - 1 and c == n - 1:
                return length
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if nr < 0 or nc < 0 or nr >= n or nc >=n:
                    continue

                if grid[nr][nc] == 1:
                    continue

                if (nr, nc) in visit:
                    continue

                visit.add((nr, nc))
                queue.append((nr, nc, length + 1))

        return -1 