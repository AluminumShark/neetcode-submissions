import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointsHeap = [(x ** 2 + y ** 2, x, y) for x, y in points]
        heapq.heapify(pointsHeap)

        ans = []

        for i in range(k):
            _, x, y = heapq.heappop(pointsHeap)
            ans.append([x, y])

        return ans