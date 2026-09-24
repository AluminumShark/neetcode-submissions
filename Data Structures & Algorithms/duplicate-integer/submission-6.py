class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1

        for c in cnt.values():
            if c > 1:
                return True
        
        return False