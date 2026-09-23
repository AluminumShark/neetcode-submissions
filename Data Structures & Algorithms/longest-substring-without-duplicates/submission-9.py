class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        window = set()
        length = float('-inf')
        L = 0
        for R in range(n):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            length = max(length, R - L + 1)
        return length
