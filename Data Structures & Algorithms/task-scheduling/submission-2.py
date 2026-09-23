class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0] * 26
        for t in tasks:
            cnt[ord(t) - ord('A')] += 1
        
        cnt.sort()
        maxf = cnt[25]
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            idle -= min(cnt[i], maxf - 1)
        
        return max(0, idle) + len(tasks)