import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        h = [-cnt for cnt in counter.values()]
        heapq.heapify(h)
        q = deque()
        time = 0

        while h or q:
            time += 1
            if not h:
                time = q[0][1]
            
            else:
                cnt = 1 + heapq.heappop(h)

                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
            
        return time