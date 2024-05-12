import unittest

class TestPermutation(unittest.TestCase):
    def test_permutation(self):
        res = self.permutation([1,2,3])
        ans = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        set0 = set(frozenset(item) for item in res)
        set1 = set(frozenset(item) for item in ans)
        self.assertEqual(set1, set0)

    def permutation(self, nums):
        ans = []
        def backtrack(start, end):
            if start == end:
               ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0, len(nums))
        return
