class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        record = {}
        for i in range(n):
            diff = target - nums[i]
            record[diff] = (i, nums[i])

        for i in range(n):
            if nums[i] in record:
                idx1, _ = record[nums[i]]
                idx2 = i
                if idx1 != idx2:
                    return sorted([idx1, idx2])