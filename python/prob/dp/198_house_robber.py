'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''


import unittest
from unittest import result

class HouseRobber(unittest.TestCase):

    def rob1(self, nums: list[int]) -> int:
        def rob_internal(nums, i, memo):
            if i < 0:
                return 0
            if memo[i] > 0:
                return memo[i]
            res = max(rob_internal(nums, i - 2) +
                      nums[i], rob_internal(nums, i - 1))
            memo[i] = result
            return result

        # top- down
        memo = [-1 for _ in range(len(nums) + 1)]

        return rob_internal(nums, len(nums) - 1, memo)

    def rob2(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0 for _ in range(len(nums) + 1)]
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
        return dp[len(nums)]

    def test(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(4, self.rob2(nums))


if __name__ == '__main__':
    unittest.main()
