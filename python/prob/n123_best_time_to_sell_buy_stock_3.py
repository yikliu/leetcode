"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List

def maxProfit(self, prices:List[int]) -> int:

    if not prices or len(prices) == 0:
        return 0

    n = len(prices)

    # profit_left[i] means if world ends on day i, what is best profit
    # for buy one and sell one'
    profit_left = [0 for _ in n]
    profit_left[0] = prices[0]
    left_min = float('inf')
    for i in range(1, n):
        profit_left[i] = max(profit_left[i - 1], prices[i] - left_min)
        left_min = min(left_min, prices[i])

    # profit_right[i] means if the market starts at ith day, what is
    # the max profit for buy any day after i and sell later'
    profit_right = [0 for _ in n]
    profit_right[n - 1] = prices[n - 1]
    right_max = float('-inf')
    for j in range(n-2, 1, -1):
        profit_right[j] = max(right_max - prices[j + 1],
                              profit_right[j + 1])
        right_max = max(right_max, prices[j + 1])

    max_profit = 0
    for t in range(n):
        max_profit = max(max_profit, profit_left[t] + profit_right[t])

    return max_profit
