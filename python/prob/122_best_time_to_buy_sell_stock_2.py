'''
Given an array prices, which represents the price of a stock in each day.

You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, if you already have the stock, you must sell it before you buy again).

Design an algorithm to find the maximum profit.
'''

class BestTimeToBuySellStockII:


    def max_profit(self, prices:List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0

        max_profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                max_profit += diff

        return max_profit
