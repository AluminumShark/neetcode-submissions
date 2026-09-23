class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            curSum = numbers[R] + numbers[L]
            if curSum < target:
                L += 1
            elif curSum > target:
                R -= 1
            else:
                return [L + 1, R + 1]