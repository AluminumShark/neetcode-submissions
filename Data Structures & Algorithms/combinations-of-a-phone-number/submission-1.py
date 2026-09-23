class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            key = digits[i]
            for ch in mp[key]:
                dfs(i + 1, curStr + ch)

        if digits:
            dfs(0, '')
        
        return res