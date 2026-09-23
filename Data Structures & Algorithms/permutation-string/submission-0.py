class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        hs = set()
        target = ''.join(sorted(s1))
        L = 0
        for R in range(m - 1, n):
            while (R - L + 1) > m:
                L += 1
                
            substr = ''.join(sorted(s2[L : R + 1]))
            hs.add(substr)

            if target in hs:
                return True
        return False