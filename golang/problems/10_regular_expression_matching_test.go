/**
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

**/
package leetcode

import "testing"

func TestIsRegMatch(t *testing.T) {
	s := "aaa"
	p := "ab*a*c*a"
	res := isRegMatch(s, p)
	if !res {
		t.Error("Failed")
	}
}

func isRegMatch(s string, p string) bool {
	size_s := len(s)
	size_p := len(p)

	dp := make([][]int, size_p + 1)
	for i := range dp {
		dp[i] = make([]int, size_s + 1)
	}

	dp[0][0] = 1

	for j := 0; j < size_p + 1; j++ {
		if j > 1 && p[j-1] == '*' && dp[j-2][0] == 1 {
			dp[j][0] = 1
		}
	}

	for i := 1; i < len(p) + 1; i++ {
		for j := 1; j < len(s) + 1; j++ {
			if p[i-1] == s[j-1] || p[i-1] == '.' {
				dp[i][j] = dp[i-1][j-1]
			} else if p[i-1] == '*' {
				if i >= 2 {
					if p[i-2] == '.' || p[i-2] == s[j-1] {
						dp[i][j] = dp[i][j-1]
					} else {
						dp[i][j] = dp[i-2][j]
					}
				}
			}
		}
	}
	return dp[size_p][size_s] == 1
}
