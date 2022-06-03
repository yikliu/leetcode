"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:
Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
             Follow up:
             Could you solve it in O(nk) runtime?
"""

import unittest

class paint_house_ii(unittest.TestCase):
    def minCosts(costs: List[List[int]]) -> int:
        if not costs or len(costs) == 0:
            return 0
        n = len(costs)
        k = len(costs[0])
        for house in range(1, n):
            for color in range(0, k):
                min_cost = float('inf')
                for pre_color in range(0, k):
                    if color == pre_color:
                        continue
                    min_cost = min(min_cost, costs[house - 1][pre_color])
                costs[house][color] += min_cost

        ans = min(costs[n-1])
        return ans
