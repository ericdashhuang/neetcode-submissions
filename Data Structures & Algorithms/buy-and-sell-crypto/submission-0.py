class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        bestprice = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - bestprice
            res = max(res, profit)
            bestprice = min(bestprice, prices[i])
        return res
