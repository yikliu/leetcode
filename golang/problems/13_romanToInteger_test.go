/**
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3

Example 2:

Input: "IV"
Output: 4

Example 3:

Input: "IX"
Output: 9

Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

**/
package leetcode

import (
	"testing"
)

func TestRomanToInteger(t *testing.T) {
	data := map[string]int{
		"MCMXCIV": 1994,
		"LVIII":   58,
		"IX":      9,
		"IV":      4,
		"III":     3,
	}

	var res int
	for key, value := range data {
		res = romanToInteger(key)
		if res != value {
			t.Errorf("Res was incorrect, got: %d, want: %d.", res, value)
		}
	}
}

func romanToInteger(s string) int {
	m := make(map[byte]int)
	m['I'] = 1
	m['V'] = 5
	m['X'] = 10
	m['L'] = 50
	m['C'] = 100
	m['D'] = 500
	m['M'] = 1000
	var res int = 0
	for n := 0; n < len(s); n++ {
		if n == len(s)-1 || m[s[n]] >= m[s[n+1]] {
			res += m[s[n]]
		} else {
			res -= m[s[n]]
		}
	}
	return res
}
