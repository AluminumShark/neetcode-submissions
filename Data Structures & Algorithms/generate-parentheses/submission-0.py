class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur, res = [], []
        def dfs(open, close):
            if open == n and close == n:
                res.append(''.join(cur))
                return
            
            if open < n:
                cur.append('(')
                dfs(open + 1, close)
                cur.pop()
            
            if close < open:
                cur.append(')')
                dfs(open, close + 1)
                cur.pop()
        dfs(0, 0)
        return res