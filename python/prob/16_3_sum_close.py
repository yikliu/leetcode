'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

from typing import List

def threeSumClose(nums: List[int], target:int) -> int:
    n = len(nums)
    nums = sorted(nums)
    res = nums[0] + nums[1] + nums[2]
    for i in range(n - 2):
        start = i + 1
        end = n - 1
        while start < end:
            temp = nums[i] + nums[start] + nums[end]
            if abs(target - temp) < abs(target - res):
                res = temp
            if res == target:
                return res
            if temp < target:
                start += 1
            else:
                end -= 1
    return res
