class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0

        for i in range(n):
            leftMax = 0
            rightMax = 0

            for L in range(0, i + 1):
                leftMax = max(leftMax, height[L])

            for R in range(i, n):
                rightMax = max(rightMax, height[R])

            ans += max(0, min(leftMax, rightMax) - height[i])

        return ans
