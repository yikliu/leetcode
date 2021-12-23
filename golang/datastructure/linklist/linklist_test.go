package linklist

import (
	"testing"
)

func TestLinkList(t *testing.T) {
	llist := New()
	llist.Append("first")
	llist.Append("second")
	llist.Append("third")

	//size
	curSize := llist.Size()
	if curSize != 3 {
		t.Errorf("Current Link Size: %v, expected %v ", curSize, 3)
	}

	//Get
	pSecondNode, err := llist.Get(1)
	if err != nil {
		t.Errorf("Error in getting element : %q", err.Error())
	}

	if (*pSecondNode).element != "second" {
		t.Errorf("second element is not second %v", (*pSecondNode).element)
	}

	pFail, err := llist.Get(-1)
	if err == nil || pFail != nil {
		t.Errorf("getting item at index -1 should have throw error.")
	}

	//insert
	insertAtHead := LinkNode{
		element: "newHead",
		next:    nil,
	}

	err = llist.InsertAt(0, &insertAtHead)
	if err != nil {
		t.Errorf("Insert error %v", err)
	}

	size := llist.Size()
	if size != 4 {
		t.Errorf("after insertion, there should be 4 items, but there are %v items", size)
	}

	var getNewHead, _ = llist.Get(0)
	if (*getNewHead).element != "newHead" {
		t.Errorf("after insersion at head, the head element is not right.")
	}

	insertAtTail := LinkNode{
		element: "newTail",
		next:    nil,
	}
	err = llist.InsertAt(4, &insertAtTail)
	if err != nil {
		t.Errorf("Insert error %v", err)
	}
	size = llist.Size()
	if size != 5 {
		t.Errorf("after insersion, there should be 5 items, but there are %v itmes.", size)
	}

	var getNewTail, _ = llist.Get(4)
	if (*getNewTail).element != "newTail" {
		t.Errorf("after insersion at tail, the tail element is not right.")
	}

	_ = llist.DeleteAt(0)
	if llist.Size() != 4 {
		t.Errorf("after deletion, there should be only 4 items")
	}

	headAfterDeletion, _ := llist.Get(0)
	if (*headAfterDeletion).element != "first" {
		t.Errorf("after deletion at head, the head should be first, not %v", (*headAfterDeletion).element)
	}

}
