import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointsHeap = [(-(x ** 2 + y ** 2), x, y) for x, y in points]
        heapq.heapify(pointsHeap)

        while len(pointsHeap) > k:
            heapq.heappop(pointsHeap)
        
        ans = []
        for _, x, y in pointsHeap:
            ans.append([x, y])
        
        return ans