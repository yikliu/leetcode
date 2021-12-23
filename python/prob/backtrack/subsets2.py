import unittest

"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10


"""

class SubSetsTest2Case(unittest.TestCase):
    def test_subsets(self):
        res = self.subsets2([1, 2, 2])
        self.assertEqual(len(res), 6)

    def subsets2(self, nums):
        def backtrack(tmp, start, end):
            ans.append(tmp[:])
            for i in range(start, end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                backtrack(tmp, i + 1, end)
                tmp.pop()
        ans = []
        nums.sort()
        backtrack([], 0, len(nums))
        return ans


if __name__ == '__main__':
    unittest.main()
