import unittest

def continuous_subarray_sum(nums, k):
    remainders = set()
    sum = 0
    t = 0
    for num in nums:
        sum += num
        if k > 0:
            t = sum % k
        else:
            t = sum
        if t in remainders:
            return True
        else:
            remainders.add(t)
    return False


class TestContinuousSubArraySum(unittest.TestCase):
    def test_continous_subarray_sum(self):
        res = continuous_subarray_sum([23, 2, 4, 6, 7], 6)
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
