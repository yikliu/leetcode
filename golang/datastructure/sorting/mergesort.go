package sorting

import (
	"fmt"
	array "golib/datastructure/arraylist"
)

func MergeSort(arr *array.List, left int, right int) {
	if right-left <= 0 {
		return
	}

	mid := (right + left) / 2

	MergeSort(arr, left, mid)
	MergeSort(arr, mid+1, right)

	Merge(arr, left, mid, right)
}

func Merge(arr *array.List, left int, mid int, right int) {
	i := left
	j := mid + 1
	t := 0
	temp := make([]interface{}, right-left+1)
	for i <= mid && j <= right {
		res, err := arr.Compare(i, j)
		if err != nil {
			panic(fmt.Sprintf("error in compare: %v, index i: %d, index j: %d", err.Error(), i, j))
		}
		if res < 0 {
			temp[t], _ = arr.Get(i)
			i += 1
		} else {
			temp[t], _ = arr.Get(j)
			j += 1
		}
		t += 1
	}

	for i <= mid {
		temp[t], _ = arr.Get(i)
		i += 1
		t += 1
	}

	for j <= right {
		temp[t], _ = arr.Get(j)
		j += 1
		t += 1
	}

	arr.CopyRange(left, temp)
}
