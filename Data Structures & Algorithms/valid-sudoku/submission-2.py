class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] is '.':
                    continue
                boxId = (r // 3) * 3 + c // 3
                target = board[r][c]
                if (target in rows[r]) or (target in cols[c]) or (target in boxs[boxId]):
                    return False
                
                rows[r].add(target)
                cols[c].add(target)
                boxs[boxId].add(target)

        return True