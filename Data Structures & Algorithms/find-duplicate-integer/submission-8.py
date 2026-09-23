class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        S, F = nums[0], nums[0]
        while True:
            S = nums[S]
            F = nums[nums[F]]
            if S == F:
                break
        
        ptr1 = nums[0]
        ptr2 = S
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1