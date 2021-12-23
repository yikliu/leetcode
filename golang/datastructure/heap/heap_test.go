package heap

import (
	"golib/datastructure/arraylist"
	"testing"
)

func TestHeap(t *testing.T) {
	arr := arraylist.NewWithElements(4, 6, 3, 22, 34, 5, 9, 20)

	heap := New(arr)

	heap.data.Print()

	if head, _ := heap.data.Get(0); head != 34 {
		t.Errorf("heapfiy failed")
	}
}
