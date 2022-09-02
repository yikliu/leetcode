'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

from typing import List

def maxProduct(nums: List[int])-> int:
    max_i = [nums[0]]
    min_i = [nums[0]]
    res = nums[0]
    for i in range(1, len(nums)):
        max_i.append(max(max_i[i-1] * nums[i], min_i[i-1] * nums[i], nums[i]))
        min_i.append(min(min_i[i-1] * nums[i], max_i[i-1] * nums[i], nums[i]))
        res = max(res, max_i[i])
    return res
