class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        L = 0
        for R in range(n):
            if len(set(s[L : R + 1])) == len(s[L : R + 1]):
                ans = R - L + 1
            else:
                L += 1
        return ans

# asfdffet
            

