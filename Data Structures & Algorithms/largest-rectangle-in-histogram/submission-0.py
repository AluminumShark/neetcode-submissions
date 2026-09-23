class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        ans = 0
        for i, cur in enumerate(heights):
            while stack and heights[stack[-1]] > cur:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = (i - 1) - (left + 1) + 1
                ans = max(ans, h * width)
            stack.append(i)
        return ans