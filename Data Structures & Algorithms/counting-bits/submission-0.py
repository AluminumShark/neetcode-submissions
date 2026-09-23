class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOne(x: int):
            count = 0
            while x > 0:
                if x & 1:
                    count += 1
                x = x >> 1
            return count
        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = countOne(i)
        return ans