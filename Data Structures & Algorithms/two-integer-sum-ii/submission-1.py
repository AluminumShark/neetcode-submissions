class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            diff = numbers[R] + numbers[L]
            if diff < target:
                L += 1
            elif diff > target:
                R -= 1
            else:
                return [L + 1, R + 1]