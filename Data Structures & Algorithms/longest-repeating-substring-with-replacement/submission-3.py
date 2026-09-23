class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        length = maxf = float('-inf')
        count = {}
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxf = max(count[s[R]], maxf)
            while (R - L + 1) - maxf > k:
                count[s[L]] -= 1
                L += 1
            length = max(length, (R - L + 1))
        return length

# XZZXY 2