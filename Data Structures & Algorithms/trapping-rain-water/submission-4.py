class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        L, R = 0, n - 1
        leftMax, rightMax = height[L], height[R]
        ans = 0

        while L < R:
            if leftMax <= rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                ans += max(0, leftMax - height[L])
            else:
                R -= 1
                rightMax = max(rightMax, height[R])
                ans += max(0, rightMax - height[R])
        
        return ans