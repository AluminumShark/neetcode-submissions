from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid and not grid[0]:
            return -1
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        visit.add((0, 0))
        queue = deque()
        queue.append((0, 0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    
                    if grid[nr][nc] == 1:
                        continue

                    if (nr, nc) in visit:
                        continue

                    visit.add((nr, nc))
                    queue.append((nr, nc))

            length += 1

        return -1