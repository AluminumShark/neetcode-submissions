class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        store = 0
        while L < R:
            left = heights[L]
            right = heights[R]
            store = max(store, (R - L) * min(left, right))
            if left <= right:
                L += 1
            elif left > right:
                R -= 1
        return store