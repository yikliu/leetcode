package arraylist

import (
	"testing"
)

func TestArraylist(t *testing.T) {
	list := NewWithElements(1, 2, 3, 4)

	/*  Alternatively
	list := New()
	list.Add(1, 2, 3, 4)
	*/

	if actualSize := list.Size(); actualSize != 4 {
		t.Errorf("Got %v; expected %v", actualSize, 4)
	}

	if actualElement, _ := list.Get(2); actualElement != 3 {
		t.Errorf("Got %v; expected %v", actualElement, 3)
	}

	if found := list.Contains(5); found {
		t.Errorf("Got %v; expected %v", found, false)
	}

	if err := list.Remove(2); err != nil || list.Size() != 3 {
		t.Errorf("Remove has error  %v, size is %v, expected size: %v", err, list.Size(), 3)
	}
	//remaining [1,2,4]
	list.Swap(1, 2)
	if val, _ := list.Get(1); val != 4 {
		t.Errorf("Swap failed. val: %v", val)
	}

	if res, _ := list.Compare(2, 1); res >= 0 {
		t.Errorf("arr[2] = 2 should be smaller than arr[1] = 4")
	}

	list.Print()
	var toCopy = []interface{}{7, 8, 9}
	list.CopyRange(1, toCopy)
	list.Print() //should output (1,7,8,9)

	var toCopy2 = []interface{}{11, 12, 13}

	list.CopyRange(3, toCopy2)
	list.Print() //should output (1,7,8, 11,12,13)
	var toCopy3 = []interface{}{14, 15}
	list.CopyRange(1, toCopy3)
	list.Print()

}
