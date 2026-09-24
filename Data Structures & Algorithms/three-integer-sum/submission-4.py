class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                tmp = nums[i] + nums[L] + nums[R]
                if tmp == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L - 1] == nums[L]:
                        L += 1
                    while L < R and nums[R + 1] == nums[R]:
                        R -= 1
                elif tmp < 0:
                    L += 1
                else:
                    R -= 1
        return res