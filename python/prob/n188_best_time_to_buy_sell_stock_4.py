"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

from typing import List

def max_profit(prices:List[int], k:int) -> int:

    if not prices or len(prices) == 0:
        return 0

    n = len(prices)

    if k > n / 2:
        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                max_profit += diff
        return max_profit

    dp = [[0 for x in range(n+1)] for y in range(k+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            for x in range(1, i+1):
                dp[i][j] = max(dp[i][j], dp[i][j-1] + profit(prices, x + 1, i))
    return dp[n][k]

def profit(prices:List[int], i:int, j:int)->int:
    if i >=j:
        return 0
    left_min = float('inf')
    profit = 0
    for t in range(i, j):
        profit = max(profit, prices[t] - left_min)
        left_min = min(left_min, prices[t])
    return profit
