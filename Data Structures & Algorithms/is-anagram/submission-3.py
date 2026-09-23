from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cts = Counter(s)
        ctt = Counter(t)
        return cts == ctt