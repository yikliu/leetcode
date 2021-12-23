# pylint: skip-file

import unittest

"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

"""


class SubSetsTestCase(unittest.TestCase):
    def test_subsets(self):
        res = self.subsets([1, 2, 3])
        self.assertEqual(len(res), 8)

    def subsets(self, nums):
        def backtrack(tmp, start, end):
            ans.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(tmp, i + 1, end)
                tmp.pop()
        ans = []
        backtrack([], 0, len(nums))
        return ans


if __name__ == '__main__':
    unittest.main()
