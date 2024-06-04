'''
Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

Example 1:
Input: "abcd"
Output: 0
Explanation: There is no repeating substring.

Example 2:
Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.

Example 3:
Input: "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.

Example 4:
Input: "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.


Note:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500
'''

def search(L:int, n:int, s:str)->int:
    store = set()

    for i in range(n - L + 1):
        tmp = s.substring(i, i + L)
        if tmp in store:
            return i
        else:
            store.add(tmp)

    return -1

def longestRepeatSubString(s: str) -> int:
    n = len(s)
    left = 0
    right = n
    while left <= right:
        L = left + (right - left) // 2
        if search(L, n, s) == -1:
            right = L - 1
        else:
            left = L + 1

    return left - 1
