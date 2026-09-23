import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(-(x ** 2 + y ** 2), x, y) for x, y in points]
        heapq.heapify(dist)
        while len(dist) > k:
            heapq.heappop(dist)
        ans = [[x, y] for _, x, y in dist]
        return ans