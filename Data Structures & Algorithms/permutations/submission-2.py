class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        
        result = []

        for i in range(len(nums)):
            cur = nums.pop(0)
            remain = self.permute(nums)
            
            for p in remain:
                p.append(cur)
            
            result.extend(remain)

            nums.append(cur)

        return result