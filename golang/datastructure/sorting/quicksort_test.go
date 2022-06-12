package sorting

import (
	"fmt"
	array "golib/datastructure/arraylist"
	"testing"
)

func TestQuickSort(t *testing.T) {
	arr := array.NewWithElements(3, 6, 9, 1, 0, 11, 8)
	fmt.Printf("before quick sort: ")
	arr.Print()

	// choose how to select pivot element
	fn := SelectRandomPivot()
	//fn := SelectRightAsPivot()

	QuickSort(arr, 0, arr.Size()-1, fn)
	fmt.Printf("after quick sort: ")
	arr.Print()

	expected := array.NewWithElements(0, 1, 3, 6, 8, 9, 11)

	if !arr.IsMemeberWiseEqual(expected) {
		t.Errorf("Sorting error")
	}
}
