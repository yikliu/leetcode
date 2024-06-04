from typing import List
import unittest

def maxSumTwoNonOverlappingSubArrays(a: List[int], l: int, m: int) -> int:
    return max(two_subarray_max_sum(a, l, m), two_subarray_max_sum(a, m, l))

def two_subarray_max_sum(a: List[int], l:int, m: int) -> int:

    sum_l = 0
    sum_m = 0

    for i in range(l + m):
        if i < l:
            sum_l += a[i]
        else:
            sum_m += a[i]

    max_l = 0
    ans = 0

    for i in range(i + m, len(a)):
        sum_l += a[i - m] - a[i - m - l]
        sum_m += a[i] - a[i - m]
        max_l = max(max_l, sum_l)
        ans = max(ans, max_l + sum_m)

    return ans

