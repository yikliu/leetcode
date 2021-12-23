package leetcode

import (
	"fmt"
	"testing"
)

func TestLetterCombination(t *testing.T) {
	digits := "23"
	res := letterCombinations(digits)
	expected := []string{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}
	if len(res) != len(expected) {
		t.Errorf("Res was incorrect")
	}
}

/*
 * @lc app=leetcode id=17 lang=golang
 *
 * [17] Letter Combinations of a Phone Number
 */
func letterCombinations(digits string) []string {
	var res []string
	mapping := map[string]string{
		"0": "0",
		"1": "1",
		"2": "abc",
		"3": "def",
		"4": "ghi",
		"5": "jkl",
		"6": "mno",
		"7": "pqrs",
		"8": "tuv",
		"9": "wxyz"}
	local := ""
	res = backtracking(res, &digits, 0, mapping, &local)
	return res
}

func backtracking(
	res []string,
	digits *string,
	level int,
	mapping map[string]string,
	local *string) []string {
	fmt.Printf("level %d\n", level)
	fmt.Println("local " + (*local))
	fmt.Printf("lens(digits), %v\n", len(*digits))
	if level == len(*digits) {
		res = append(res, *local)
		fmt.Printf("res %v \n", res)
	} else {
		dgt := string((*digits)[level])
		characters := mapping[dgt]
		for _, char := range characters {
			*local += string(char)
			res = backtracking(res, digits, level+1, mapping, local)
			*local = (*local)[:len(*local)-1]
		}
	}
	return res
}
