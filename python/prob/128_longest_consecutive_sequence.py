'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

import unittest

class TestLongestConsecutiveSequence(unittest.TestCase):

    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set()
        for n in nums:
            numSet.add(n)

        longest = 0

        for n in numSet:
            if not n - 1 in numSet:
                currentNum = n
                streak = 1
                while currentNum + 1 in numSet:
                    currentNum += 1
                    streak += 1

                longest = max(longest, streak)

        return longest

    def test_calculator2(self):
        res = self.longestConsecutive([100, 4, 200, 1, 3, 2])
        self.assertEqual(res, 4)


if __name__ == '__main__':
    unittest.main()
