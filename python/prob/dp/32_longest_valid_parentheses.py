'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

import unittest

class LongestValidParentheses(unittest.TestCase):

    def dp_solution_1(s: String) -> int:
        maxans = 0
        dp = []
        for i in range(1, len(s)):
            if s[i] == ')':
                j = i - dp[i - 1]
                if s[i - 1] == '(':
                    if i >= 2: # xxxx()
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2 # ()
                elif j > 0 and s[j - 1] == '(':
                    if j >= 2: 
                        dp[i] = dp[j-2] + dp[i-1] + 2
                    else: # (xxxxx)
                        dp[i] = dp[i-1] + 2

            maxans = max(maxans, dp[i])
        return maxans

    def stack_solution(s: String) -> int:
        maxans = 0
        stack = []
        stack.append(-1)
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.push(i)
                else:
                    maxans = max(maxans, i - stack[len(stack) - 1])
        return maxans







