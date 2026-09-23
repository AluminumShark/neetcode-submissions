import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        h = []
        for n, f in cnt.items():
            heapq.heappush(h, (f, n))
            if len(h) > k:
                heapq.heappop(h)
        
        return [n for f, n in h]