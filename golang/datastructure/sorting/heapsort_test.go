package sorting

import (
	array "golib/datastructure/arraylist"
	"testing"
)

func TestHeapSort(t *testing.T) {
	arr := array.NewWithElements(4, 6, 3, 22, 34, 5, 9, 20)

	expected := array.NewWithElements(3, 4, 5, 6, 9, 20, 22, 34)
	HeapSort(arr)

	for i := 0; i < expected.Size(); i++ {
		item1, _ := arr.Get(i)
		item2, _ := expected.Get(i)

		if item1 != item2 {
			t.Errorf("Item[%d] = %d is not equal to the sorted array Item[%d] = %d", i, item1, i, item2)
		}
	}
}
