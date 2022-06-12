package linklist

import (
	"fmt"
)

type LinkNode struct {
	element interface{}
	next    *LinkNode
}

type LinkList struct {
	head *LinkNode
	size int
}

//public methods
func New() *LinkList {
	return &LinkList{head: nil}
}

func (list *LinkList) Append(element interface{}) {
	newNode := LinkNode{
		element: element,
		next:    nil,
	}

	cur := list.head
	if cur == nil {
		list.head = &newNode
	} else {
		for cur.next != nil {
			cur = cur.next
		}
		cur.next = &newNode
	}

	list.size += 1
}

func (list *LinkList) InsertAt(index int, node *LinkNode) error {
	//insert at last
	if index == list.Size() {
		lastNode, err := list.Get(index - 1)
		if err != nil {
			return err
		}
		lastNode.next = node
		list.size += 1
		return nil
	}

	//insert at head
	if index == 0 {
		oldHead := list.head
		list.head = node
		node.next = oldHead
		list.size += 1
		return nil
	}

	//insert at any position between [1, size -1]
	beforeNode, err := list.Get(index - 1)
	if err != nil {
		return fmt.Errorf("/golib/linklist/Insert has error %v", err)
	}

	oldNode := beforeNode.next
	beforeNode.next = node
	node.next = oldNode
	list.size += 1
	return nil
}

func (list *LinkList) DeleteAt(index int) error {
	if index < 0 || index >= list.size {
		return fmt.Errorf("invalid index %d", index)
	}

	if index == 0 {
		list.head = list.head.next
		list.size -= 1
		return nil
	}

	if index == list.size-1 {
		secondLast, _ := list.Get(index - 1)
		secondLast.next = nil
		list.size -= 1
		return nil
	}

	prevNode, _ := list.Get(index - 1)
	prevNode.next = prevNode.next.next
	list.size -= 1
	return nil
}

func (list *LinkList) Size() int {
	return list.size
}

func (list *LinkList) Get(index int) (*LinkNode, error) {
	if index < 0 || index >= list.Size() {
		return nil, fmt.Errorf("/golib/linklist/Get: invalid index (%d), the current size of linklist is (%d)", index, list.Size())
	}

	cur := list.head
	curStep := 0

	for curStep < index {
		cur = cur.next
		curStep = curStep + 1
	}

	return cur, nil
}
