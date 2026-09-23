class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            midVal = matrix[mid // n][mid % n]
            if target > midVal:
                left = mid + 1
            elif target < midVal:
                right = mid - 1
            else:
                return True
        return False