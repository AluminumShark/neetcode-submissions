class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            L, R = 0, n - 1
            while L < i < R:
                curSum = nums[L] + nums[i] + nums[R]
                if curSum < 0:
                    L += 1
                elif curSum > 0:
                    R -= 1
                else:
                    ans.append([nums[L], nums[i], nums[R]])
                    L += 1
                    R -= 1
        return [list(t) for t in set(tuple(x) for x in ans)]
            