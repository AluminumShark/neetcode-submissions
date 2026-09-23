class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        maxLeft[0] = height[0]
        maxRight[n - 1] = height[n - 1]
        res = 0

        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])

        for i in range(n):
            res += max(min(maxLeft[i], maxRight[i]) - height[i], 0)

        return res