'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

Example 1:
Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".

Note:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
'''

import unittest
from typing import List

def longestStrChain(words: List[str]) -> int:
    dp = {}
    # sort by length
    words = sorted(words, key=len)
    ans = 0
    for s in words:
        best = 0
        for i in range(len(s)):
            prev = s[:i] + s[i + 1:]
            if prev in dp:
                best = max(best, dp[prev] + 1)
            else:
                best = max(best, 1)
        dp[s] = best
        ans = max(ans, best)
    return ans

class TestLongestStringChain(unittest.TestCase):

    def testLongestStrChain(self):
        words = ["a", "b", "ba", "bca", "bda", "bdca"]
        ans = longestStrChain(words)
        self.assertEqual(4, ans)

    def testLongestStrChain2(self):
        words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
        ans = longestStrChain(words)
        self.assertEqual(5, ans)

    def test3(self):
        words = ["abcd", "dbqca"]
        self.assertEqual(1, longestStrChain(words))

if __name__ == '__main__':
    unittest.main()
