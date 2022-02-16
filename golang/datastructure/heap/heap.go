package heap

import (
	array "golib/datastructure/arraylist"
)

type Heap struct {
	data *array.List
}

func New(arr *array.List) *Heap {
	h := &Heap{data: arr}
	h.BuildHeap()
	return h
}

func (heap *Heap) BuildHeap() {
	size := heap.data.Size()
	for i := size/2 - 1; i >= 0; i-- {
		heap.Heapify(i, size)
	}
}

func (heap *Heap) Size() int {
	return heap.data.Size()
}

func (heap *Heap) Swap(i, j int) error {
	return heap.data.Swap(i, j)
}

func (heap *Heap) Heapify(i int, upto int) {
	var largest = i
	var l = i*2 + 1
	var r = (i + 1) * 2

	if l < upto {
		compare_i_l, err := heap.data.Compare(i, l)
		if err != nil {
			panic(err.Error())
		}
		if compare_i_l < 0 {
			largest = l
		} else {
			largest = i
		}

	}

	if r < upto {
		compare_r_largest, err := heap.data.Compare(largest, r)
		if err != nil {
			panic(err.Error())
		}

		if compare_r_largest < 0 {
			largest = r
		}
	}

	if largest != i {
		heap.data.Swap(largest, i)
		heap.Heapify(largest, upto)
	}
}
