class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        L, R = 0, len(s) - 1
        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
                continue
            else:
                return False
        return True