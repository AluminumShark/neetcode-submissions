class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        maxLeft = height[0]
        maxRight = height[-1]
        res = 0
        L, R = 0, len(height) - 1

        while L < R:
            if maxLeft < maxRight:
                L += 1
                maxLeft = max(maxLeft, height[L])
                res += maxLeft - height[L]
            else:
                R -= 1
                maxRight = max(maxRight, height[R])
                res += maxRight - height[R]
        
        return res