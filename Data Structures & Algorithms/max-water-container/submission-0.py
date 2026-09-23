class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        ans = 0
        while L < R:
            ans = max(ans, (R - L) * min(heights[R], heights[L]))
            if heights[L] >= heights[R]:
                R -= 1
            else:
                L += 1
        return ans