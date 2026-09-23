class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                arr.append(matrix[i][j])

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > arr[mid]:
                left = mid + 1
            elif target < arr[mid]:
                right = mid - 1
            else:
                return True
        return False