class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
            
        need = [0] * 26
        win = [0] * 26

        for ch in s1:
            need[ord(ch) - ord('a')] += 1
        
        for i in range(m):
            win[ord(s2[i]) - ord('a')] += 1

        if need == win:
            return True
        
        for i in range(m, n):
            win[ord(s2[i]) - ord('a')] += 1
            win[ord(s2[i - m]) - ord('a')] -= 1
            if need == win:
                return True
        return False 
