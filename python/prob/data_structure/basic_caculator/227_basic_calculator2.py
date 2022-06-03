'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

from collections import deque
import unittest


class TestBasicCalculator2(unittest.TestCase):

    def calculate2(self, s: str) -> int:
        if len(s) == 0:
            return 0
        size = len(s)
        stack = deque()
        sign = '+'
        num = 0
        i = 0
        while i < size:
            if s[i].isdigit():
                numStr = s[i]
                while i + 1 < size and s[i+1].isdigit():
                    numStr += s[i+1]
                    i += 1
                num = int(numStr)
            if (not s[i].isdigit()) and s[i] != ' ' or i == size - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(stack.pop() // num)

                sign = s[i]
                num = 0
            i += 1
        ans = 0
        for val in stack:
            ans += val
        return ans

    def test_calculator2(self):
        res = self.calculate2(" 3/ 2 ")
        self.assertEqual(res, 1)

        res = self.calculate2("3+2*2")
        self.assertEqual(res, 7)

        res = self.calculate2(" 3+5 / 2")
        self.assertEqual(res, 5)


if __name__ == '__main__':
    unittest.main()
