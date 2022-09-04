
"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

"""

import unittest

def combination_sum_2(candidates, target):

    def backtrack(tmp, start, end, target):
        if target == 0:
            ans.append(tmp[:])
        elif target > 0:
            for i in range(start, end):
                if (i > start and candidates[i] == candidates[i - 1]):
                    continue
                tmp.append(candidates[i])
                backtrack(tmp, i + 1, end, target - candidates[i])
                tmp.pop()
    ans = []
    candidates.sort(reverse=True)
    backtrack([], 0, len(candidates), target)
    return ans

class TestCombinationSum2(unittest.TestCase):
    def test_combination_sum2(self):
        res = combination_sum_2([10, 1, 2, 7, 6, 1, 5], 8)
        self.assertEqual(4, len(res))
