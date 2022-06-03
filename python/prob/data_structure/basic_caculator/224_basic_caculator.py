'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus 
sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''
from collections import deque
import unittest


class TestBasicCalculator(unittest.TestCase):

    def calculate(self, s: str) -> int:
        size = len(s)
        sign = 1
        result = 0
        stack = deque()
        i = 0
        while i < size:
            if s[i].isdigit():
                numStr = s[i]
                while i + 1 < size and s[i + 1].isdigit():
                    numStr += s[i + 1]
                    i += 1
                result += int(numStr) * sign
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif s[i] == ')':
                result = result * stack.pop() + stack.pop()
            i = i + 1
        return result

    def test_calculator(self):
        res = self.calculate('3 + ( 4 - 2)')
        self.assertEqual(res, 5)

        res2 = self.calculate("2147483647")
        self.assertEqual(res2, 2147483647)


if __name__ == '__main__':
    unittest.main()
