/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */
package leetcode

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	var num int
	var v int
	var exist bool
	for i := len(nums) - 1; i >= 0; i-- {
		num = nums[i]
		v, exist = m[target-num]
		if exist {
			return []int{i, v}
		} else {
			m[num] = i
		}
	}
	return []int{}
}
