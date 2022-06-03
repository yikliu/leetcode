package leetcode

import "sort"

func threeSum(nums []int) [][]int {
	if len(nums) < 3 {
		return [][]int{}
	}

	sort.Ints(nums)
	lens := len(nums)
	if nums[0] > 0 || nums[lens-1] < 0 {
		return [][]int{}
	}

	var res [][]int
	var target int
	var i, j int
	for k, num := range nums {
		if num > 0 {
			break
		}
		if k > 0 && nums[k] == nums[k-1] {
			continue
		}
		target = 0 - num
		i = k + 1
		j = len(nums) - 1
		for i < j {
			if (nums[i] + nums[j]) == target {
				combo := []int{num, nums[i], nums[j]}
				res = append(res, combo)
				for i < j && nums[i] == nums[i+1] {
					i++
				}
				for i < j && nums[j] == nums[j-1] {
					j--
				}
				i++
				j--
			} else if (nums[i] + nums[j]) > target {
				j--
			} else {
				i++
			}
		}
		if i < j && target == (nums[i]+nums[j]) {

		}
	}
	return res
}
