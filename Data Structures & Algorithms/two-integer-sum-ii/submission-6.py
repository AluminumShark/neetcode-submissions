class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            L, R = i + 1, len(numbers) - 1
            cur = target - numbers[i]
            while L <= R:
                mid = (L + R) // 2
                if numbers[mid] == cur:
                    return [i + 1, mid + 1]
                elif numbers[mid] < cur:
                    L = mid + 1
                else:
                    R = mid - 1
        return []