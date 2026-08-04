class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = 0
        expensive = 0
        profit = 0
        for i in range(0, len(prices)):
            if prices[i] < prices[cheapest]:
                cheapest = i
                expensive = i
            if prices[i] - prices[cheapest] > profit:
                profit = prices[i] - prices[cheapest]
        return profit
        