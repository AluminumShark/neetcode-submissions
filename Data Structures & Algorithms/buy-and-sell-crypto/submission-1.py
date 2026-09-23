class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestBuy = float('inf')
        best_profit = 0

        for price in prices:
            lowestBuy = min(lowestBuy, price)
            best_profit = max(best_profit, price - lowestBuy)

        return best_profit
