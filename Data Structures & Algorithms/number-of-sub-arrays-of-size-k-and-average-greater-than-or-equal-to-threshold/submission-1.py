class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        targetSum = k * threshold
        n = len(arr)

        if n < k:
            return 0

        windowSum = sum(arr[0 : k])
        count = 1 if windowSum >= targetSum else 0

        for R in range(k, n):
            windowSum += arr[R]
            windowSum -= arr[R - k]
            if windowSum >= targetSum:
                count += 1

        return count

