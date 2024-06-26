"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.

Note:
1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
"""

from typing import List
import unittest

def minimal_dominal_rotation(tops: List[int], bottoms: List[int]) -> int:

    count = [0 for _ in range(7)]

    # count freq of each number in both top and bottom lists
    for i in tops:
        count[i] += 1
    for i in bottoms:
        count[i] += 1

    # find most freq #, mark the number and its freq
    max_freq = 0
    target = -1
    for i in range(1, 7):
        if count[i] > max_freq:
            max_freq = count[i]
            target = i

    # the most_freq value should at least equal to len of either top (or bottom)
    if max_freq < len(tops):
        return -1

    top_count = [0 for _ in range(7)]
    bottom_count = [0 for _ in range(7)]

    # count freq of each number in both top and bottom
    for i in tops:
        top_count[i] += 1

    for i in bottoms:
        bottom_count[i] += 1

    # if the target number occurs more on top, then flip the dominos whose number does not equal to target and see if flip side is equal to target.
    # if yes. answer +1. if not, return -1 fast.
    answer = 0
    if top_count[target] > bottom_count[target]:
        for i, _ in enumerate(tops):
            if tops[i] != target:
                if bottoms[i] != target:
                    return -1
                answer += 1
    else:
        for i, _ in enumerate(bottoms):
            if bottoms[i] != target:
                if tops[i] != target:
                    return -1
                answer += 1

    return answer


class test_minimal_dominal_rotation(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(2, minimal_dominal_rotation([2,1,2,4,2,2], [5,2,6,2,3,2]))


if __name__ == '__main__':
    unittest.main()
