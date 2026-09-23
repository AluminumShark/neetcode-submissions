class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        hashSet = set(nums)
        for n in hashSet:
            curr = n
            count = 0
            while True:
                if curr in hashSet:
                    count += 1
                else:
                    break
                curr += 1
            ans = max(ans, count)
        return ans