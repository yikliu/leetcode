'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''

import unittest

class CountingBits(unittest.TestCase):

    def counting_bits(num: int) -> List[int]:
        res = [0 for _ in range(0, num)]
        pow2 = 1
        before = 1
        for i in range(1, num + 1):
            if i == pow2:
                res[i] = 1
                pow2 <<= 1
                before = 1
            else:
                res[i] = res[before] + 1
                before += 1
        return res
