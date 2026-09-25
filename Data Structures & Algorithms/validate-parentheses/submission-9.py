class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comb = (')(', '][', '}{')
        for p in s:
            if p in '([{':
                stack.append(p)
            else:
                if not stack:
                    return False
                else:
                    if (p + stack[-1]) in comb:
                        stack.pop()
                    else:
                        return False
        
        return not stack 