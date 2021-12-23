package binarytree

import (
	"testing"
)

func TestBinaryTree(t *testing.T) {
	bt := New()
	bt.Insert(2)
	bt.Insert(3)
	bt.Insert(1)

	if bt.size != 3 {
		t.Errorf("Size should 3")
	}

	Two := bt.root
	if (*Two).element != 2 {
		t.Errorf("after insertion the root item should be 2, instead, it is %d", (*Two).element)
	}

	One := Two.left
	if (*One).element != 1 {
		t.Errorf("Two left should be one")
	}

	Three := Two.right
	if (*Three).element != 3 {
		t.Errorf("Two right should be three")
	}
}

func TestBinaryTreeLookup(t *testing.T) {
	bt := New()
	bt.Insert(10)
	bt.Insert(13)
	bt.Insert(4)
	bt.Insert(7)
	bt.Insert(6)

	_, success := bt.Lookup(13)
	if !success {
		t.Errorf("Should found 13, but couldn't")
	}

	_, success = bt.Lookup(11)
	if success {
		t.Errorf("Shouldn't found 11, but found it")
	}
}
