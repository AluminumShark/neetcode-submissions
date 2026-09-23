class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hashSet = set(nums)
        ans = 0

        for n in hashSet:
            if n - 1 not in hashSet:
                curr = n
                count = 1
                while curr + 1 in hashSet:
                    curr += 1
                    count += 1
                ans = max(ans, count)

        return ans