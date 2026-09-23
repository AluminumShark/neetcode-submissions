class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        n = len(board)

        for r in range(n):
            for c in range(n):
                val = board[r][c]

                if val == '.':
                    continue
                
                boxIdx = (r // 3) * 3 + (c // 3)
                if (val in rows[r]) or (val in cols[c]) or (val in boxs[boxIdx]):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxs[boxIdx].add(val)

        return True