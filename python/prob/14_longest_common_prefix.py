'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for s in strs:
        while s.find(prefix) != 0:
            prefix = prefix[0:len(prefix) - 1]
            if len(prefix) == 0:
                return ""
    return prefix


def lcp_divide_conquer(strs: List[str]) -> str:

    def lcp_internal(strs, l, r):
        if l == r:
            return strs[l]
        mid = (l + r) / 2
        lcp_l = lcp_internal(strs, l, mid)
        lcp_r = lcp_internal(strs, mid + 1, r)
        return combine(lcp_l, lcp_r)

    def combine(left: str, right: str) -> str:
        minimum = min(len(left), len(right))
        for i in range(minimum):
            if left[i] != right[i]:
                return left[0, i]
        return left[0, minimum]

    if len(strs) == 0:
        return ""
    return lcp_internal(strs, 0, len(strs) - 1)
