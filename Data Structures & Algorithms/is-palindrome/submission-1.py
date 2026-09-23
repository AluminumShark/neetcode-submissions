class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isWord(char: str):
            if char in '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                return True
            return False
    
        L, R = 0, len(s) - 1
        while L < R:
            while s[L] != s[R] and not isWord(s[L]):
                L += 1
            while s[L] != s[R] and not isWord(s[R]):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True
