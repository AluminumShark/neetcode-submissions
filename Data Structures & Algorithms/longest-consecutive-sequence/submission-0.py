class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        hashSet = set(nums)
        for n in hashSet:
            count = 0
            while True:
                if n in hashSet:
                    count += 1
                else:
                    break
                n += 1
            ans = max(ans, count)
        return ans