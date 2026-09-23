class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
            if freq[n] > 1:
                return True
        return False