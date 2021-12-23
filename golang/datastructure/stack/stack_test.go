package stack

import (
	"testing"
)

func TestStack(t *testing.T) {
	stack := New()
	stack.Push("a")
	stack.Push("b")
	stack.Push("c")

	if size := stack.Size(); size != 3 {
		t.Errorf("Got %v, expected %v", size, 3)
	}

	poped, err := stack.Pop()
	if err != nil {
		t.Errorf("Pop has error is %v", err)
	}

	if poped != "c" {
		t.Errorf("Popped %v, expected %v", poped, "c")
	}
}
