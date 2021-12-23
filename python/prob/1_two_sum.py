# pylint: skip-file

import unittest


def two_sum(nums, target):
    hash_nums = {}
    for i, num in enumerate(nums):
        if num in hash_nums:
            return [hash_nums[num], i]

        hash_nums[target - num] = i
    return []


class TestTwoSum(unittest.TestCase):
    def test_two_sum_simple(self):
        res = two_sum([3, 2, 4], 6)
        self.assertEqual(res, [1, 2])


if __name__ == '__main__':
    unittest.main()
