class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        L = 0
        while L < len(height) and height[L] == 0:
            L += 1
        
        if L == len(height) - 1:
            return 0

        R = L + 1
        prefix = [0] * len(height)
        while R < len(height):
            if height[L] > height[R]:
                prefix[R] = height[L] - height[R]
                R += 1
            else:
                L = R
                R += 1
        
        R = len(height) - 1
        L = R - 1
        postfix = [0] * len(height)
        while L >= 0:
            if height[R] > height[L]:
                postfix[L] = height[R] - height[L]
                L -= 1
            else:
                R = L
                L -= 1
        
        res = []
        for i in range(len(height)):
            res.append(min(prefix[i], postfix[i]))
        
        return sum(res)
