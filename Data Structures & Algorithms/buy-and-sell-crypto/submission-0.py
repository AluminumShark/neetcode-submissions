class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minPrice = float('inf')
        maxPrice = float('-inf')
        for p in prices:
            minPrice = min(minPrice, p)
            maxPrice = max(maxPrice, p - minPrice)
        return int(maxPrice)