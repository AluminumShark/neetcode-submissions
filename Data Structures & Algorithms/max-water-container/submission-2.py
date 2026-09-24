class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        res = 0
        while L < R:
            tmp = (R - L) * min(heights[L], heights[R])
            res = max(res, tmp)
            if heights[L] >= heights[R]:
                R -= 1
            elif heights[R] > heights[L]:
                L += 1
        return res