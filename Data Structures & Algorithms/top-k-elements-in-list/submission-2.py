import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
        
        h = []
        for n in cnt:
            heapq.heappush(h, (cnt[n], n))
            if len(h) > k:
                heapq.heappop(h)
        
        return [n for i, n in h]