class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        maxLeft[0] = height[0]
        maxRight[-1] = height[-1]

        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        
        res = [min(l, r) - h for l, r, h in zip(maxLeft, maxRight, height)]

        return sum(res)