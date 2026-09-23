class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        f0, f1 = 1, 2
        for _ in range(n-2):
            f0, f1 = f1, f0 + f1
        
        return f1