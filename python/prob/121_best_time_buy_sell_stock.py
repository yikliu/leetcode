"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

class BestTimeToBuySellStock:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0

        max_profit = 0
        left_min = float('inf')
        for p in prices:
            max_profit = max(max_profit, p - left_min)
            left_min = min(p, left_min)
        return max_profit
