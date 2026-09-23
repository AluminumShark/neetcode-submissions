class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        L = 0
        for R in range(n):
            arr = s[L : R + 1]
            if len(set(arr)) == len(arr):
                ans = max(ans, len(arr))
            else:
                L += 1
        return ans

# asfdffet
            

