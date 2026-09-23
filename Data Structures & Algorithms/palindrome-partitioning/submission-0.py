class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path, res = [], []
        def is_pal(L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True
        
        def dfs(start):
            if start == len(s):
                res.append(path.copy())
                return
            
            for end in range(start, len(s)):
                if is_pal(start, end):
                    path.append(s[start : end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return res