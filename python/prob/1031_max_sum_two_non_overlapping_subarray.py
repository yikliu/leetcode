"""
Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.

Example 1:
Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

Example 2:
Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

Example 3:
Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.

Note:
L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
"""

from typing import List
import unittest

def maxSumTwoNonOverlappingSubArrays(a: List[int], l: int, m: int) -> int:
    return max(maxSum(a, l, m), maxSum(a, m, l))

def maxSum(a: List[int], l: int, m: int) -> int:
    sum_l = 0
    sum_m = 0

    for i in range(l + m):
        if i < l:
            sum_l += a[i]
        else:
            sum_m += a[i]
    max_l = 0
    ans = 0
    
    # shift to find the max
    for i in range(l + m, len(a)):
        sum_l += a[i - m] - a[i - l - m]
        sum_m += a[i] - a[i - m]
        max_l = max(max_l, sum_l)
        ans = max(ans, max_l + sum_m)

    return ans


class testMaxSumTwononOverlappingSubArrays(unittest.TestCase):
    
    def testSuccess(self):
        self.assertEqual(29, maxSumTwoNonOverlappingSubArrays([3,8,1,3,2,1,8,9,0], 3, 2))
    

if __name__ == '__main__':
    unittest.main()
