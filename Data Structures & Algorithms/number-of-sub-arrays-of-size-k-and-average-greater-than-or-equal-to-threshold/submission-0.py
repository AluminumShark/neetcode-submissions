from collections import deque

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = deque()
        windowSum = 0
        count = 0
        target = k * threshold

        for x in arr:
            window.append(x)
            windowSum += x
            if len(window) > k:
                windowSum -= window.popleft()
            
            if len(window) == k and windowSum >= target:
                count += 1
        return count
            