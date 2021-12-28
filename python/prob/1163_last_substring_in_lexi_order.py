'''
Given a string s, return the last substring of s in lexicographical order.

Example 1:
Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

Example 2:
Input: "leetcode"
Output: "tcode"

Note:
1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.
'''

class LastSubStringInLexiOrder:

    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i, j, offset = 0, 1, 0
        while i + offset < n and j + offset < n:
            c = s[i + offset]
            d = s[j + offset]
            if c == d:
                offset += 1
            elif c < d:
                i = max(i + offset + 1, j + 1)
            else:
                j = max(j + offset + 1, i + 1)

            offset = 0

        return s[min(i, j)]
