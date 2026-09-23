class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            L, R = i + 1, n - 1
            while L < R:
                s = nums[i] + nums[L] + nums[R]
                if s < 0:
                    L += 1
                elif s > 0:
                    R -= 1
                else:
                    ans.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L - 1] == nums[L]:
                        L += 1
                    while L < R and nums[R + 1] == nums[R]:
                        R -= 1
        return ans