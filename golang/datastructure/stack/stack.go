package stack

import (
	"golib/datastructure/arraylist"
)

type Stack struct {
	list *arraylist.List
}

func New() *Stack {
	return &Stack{list: arraylist.New()}
}

func (stack *Stack) Push(element interface{}) {
	stack.list.Add(element)
}

func (stack *Stack) Size() int {
	return stack.list.Size()
}

func (stack *Stack) Peek() (element interface{}, err error) {
	element, err = stack.list.Get(stack.list.Size() - 1)
	return
}

func (stack *Stack) Pop() (element interface{}, err error) {
	element, err = stack.list.Get(stack.list.Size() - 1)
	err = stack.list.Remove(stack.list.Size() - 1)
	return
}
