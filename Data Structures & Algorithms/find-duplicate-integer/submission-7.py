class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = set()
        for n in nums:
            if n not in mp:
                mp.add(n)
            else:
                return n