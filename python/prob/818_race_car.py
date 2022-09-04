'''
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.

 

 Example 1:

 Input: target = 3
 Output: 2
 Explanation: 
 The shortest instruction sequence is "AA".
 Your position goes from 0 --> 1 --> 3.
 Example 2:

 Input: target = 6
 Output: 5
 Explanation: 
 The shortest instruction sequence is "AAARA".
 Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.
 '''

import unittest
from collections import deque

def race_car(target: int) -> int:
    q = deque()
    q.append((0, 1, 0)) # current_pos, current_speed, number of moves

    while q:
        cp, cs, nm = q.popleft()

        if cp == target:
            return nm

        # put options into queue
        # first option is to accelerate

        q.append((cp + cs, cs * 2, nm + 1))

        # second option is to reverse, depending on neccessity
        # if car passed target and still going forward, turn backward
        # likewise, if car is not yet past target but is already going backwards, turn forward
        if (cp + cs > target and  cs > 0) or (cp + cs < target and cs < 0):
            if cs > 0:
                q.append((cp, -1, nm + 1))
            else:
                q.append((cp, 1, nm + 1))

class RaceCarTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(5, race_car(6))

if __name__ == '__main__':
    unittest.main()
