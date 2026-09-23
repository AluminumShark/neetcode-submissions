class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        count = list(count.items())
        count.sort(key = lambda x : x[1], reverse=True)
        ans = []
        for i in range(k):
            num, _ = count[i]
            ans.append(num)
        return ans
