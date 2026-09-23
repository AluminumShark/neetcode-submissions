class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        buckets = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                
                if cur == '.':
                    continue
                
                bucketId = (r // 3) * 3 + c // 3
                if (cur in rows[r]) or (cur in cols[c]) or (cur in buckets[bucketId]):
                    return False
                
                rows[r].add(cur)
                cols[c].add(cur)
                buckets[bucketId].add(cur)
        
        return True