class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        R, C = len(matrix), len(matrix[0])
        self.prefix = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            rowSum = 0
            for c in range(C):
                rowSum += matrix[r][c]
                self.prefix[r + 1][c + 1] = rowSum + self.prefix[r][c + 1] 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1 = row1 + 1, col1 + 1
        r2, c2 = row2 + 1, col2 + 1

        return self.prefix[r2][c2] - self.prefix[r1 - 1][c2] - self.prefix[r2][c1 - 1] + self.prefix[r1 - 1][c1 - 1]
        
# 0123
# 1000
# 2000
# 3000
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)