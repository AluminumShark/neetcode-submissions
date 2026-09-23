class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1
        
        maxFreq = max(freq)
        numMax = 0
        for f in freq:
            if f == maxFreq:
                numMax += 1
        minLen = (maxFreq - 1) * (n + 1) + numMax
        return max(len(tasks), minLen)