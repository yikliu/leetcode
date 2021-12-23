package sorting

import (
	"fmt"
	array "golib/datastructure/arraylist"
	"testing"
)

func TestMergeSort(t *testing.T) {
	arr := array.NewWithElements(3, 6, 9, 1, 0, 11, 8)
	fmt.Printf("before mergesort: ")
	arr.Print()
	MergeSort(arr, 0, arr.Size()-1)
	fmt.Printf("after mergesort: ")
	arr.Print()

	expected := array.NewWithElements(0, 1, 3, 6, 8, 9, 11)

	if !arr.IsMemeberWiseEqual(expected) {
		t.Errorf("Sorting error")
	}
}
