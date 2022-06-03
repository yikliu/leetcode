package sorting

import (
	array "golib/datastructure/arraylist"
	"math/rand"
)

type SelectPivot func(left int, right int) int

func QuickSort(arr *array.List, left int, right int, fn SelectPivot) {
	if (right - left) <= 0 {
		return
	}

	pvt := fn(left, right)
	if pvt != right {
		arr.Swap(pvt, right)
	}

	divider := Partition(arr, left, right)
	QuickSort(arr, left, divider-1, fn)
	QuickSort(arr, divider+1, right, fn)
}

func Partition(arr *array.List, left, right int) int {
	i := left - 1
	j := i + 1
	for j < right {
		if ret, _ := arr.Compare(j, right); ret < 0 {
			i += 1
			arr.Swap(i, j)
			j += 1
		} else {
			j += 1
		}
	}
	arr.Swap(right, i+1)
	return i + 1
}

func SelectRightAsPivot() SelectPivot {
	return func(left int, right int) int {
		return right
	}
}

func SelectRandomPivot() SelectPivot {
	return func(left int, right int) int {
		return left + rand.Intn(right-left)
	}
}
