from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0

        bestLen = float('inf')
        bestL = 0

        L = 0
        for R, ch in enumerate(s):
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1
            
            while formed == required:
                if R - L + 1 < bestLen:
                    bestLen = R - L + 1
                    bestL = L
                
                leftCh = s[L]
                window[leftCh] -= 1
                if leftCh in need and window[leftCh] < need[leftCh]:
                    formed -= 1
            
                L += 1

        return "" if bestLen == float('inf') else s[bestL : bestL + bestLen]