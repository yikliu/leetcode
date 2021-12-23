package arraylist

import (
	"fmt"
	"golib/datastructure/comparable"
)

type List struct {
    elements []interface{}
    //size     int
}

func New() *List {
    return &List{}
}

func NewWithElements(elements ...interface{}) *List {
    list := List{}
    list.add(elements)
    return &list
}

func (list *List) Add(elements ...interface{}) {
    list.add(elements)
}

func (list *List) Remove(index int) error {
    if !list.withinRange(index) {
        return fmt.Errorf("golib/Arraylist/Remove: Invalid index %d", index)
    }

    list.elements = append(list.elements[:index], list.elements[index+1:]...)

    if (len(list.elements)+1)*2 < cap(list.elements) {
        list.shrink()
    }

    return nil
}

func (list *List) Get(index int) (interface{}, error) {
	if !list.withinRange(index) {
		return nil, fmt.Errorf("golib/Arraylist/Get: Invalid index: %d", index)
	}

	return list.elements[index], nil
}

func (list *List) Set(val interface{}, index int) error {
	if !list.withinRange(index) {
		return fmt.Errorf("golib/Arraylist/Set: Invalid index: %d", index)
	}

	list.elements[index] = val
	return nil
}

func (list *List) Compare(left int, right int) (int, error) {
	if !list.withinRange(left) {
		return 0, fmt.Errorf("golib/arraylist/Compare: Invalid left index: %d, size: %d", left, list.Size())
	}

	if !list.withinRange(right) {
		return 0, fmt.Errorf("golib/arraylist/Compare: Invalid right index: %d", right)
	}

	return comparable.Compare(list.elements[left], list.elements[right]), nil
}

func (list *List) Size() int {
	return len(list.elements)
}

func (list *List) IsEmpty() bool {
	return len(list.elements) == 0
}

func (lhs *List) IsMemeberWiseEqual(rhs *List) bool {
	if lhs.Size() != rhs.Size() {
		return false
	}

	for i := 0; i < lhs.Size(); i++ {
		lhsVal, _ := lhs.Get(i)
		rhsVal, _ := rhs.Get(i)
		if lhsVal != rhsVal {
			return false
		}
	}

	return true
}

func (list *List) Contains(element interface{}) bool {
	for _, item := range list.elements {
		if element == item {
			return true
		}
	}
	return false
}

func (list *List) Clear() {
	list.elements = []interface{}{}
}

func (list *List) Swap(left, right int) error {
	if !list.withinRange(left) {
		return fmt.Errorf("golib/arraylist/Swap: Invalid left index: %d", left)
	}

	if !list.withinRange(right) {
		return fmt.Errorf("golib/arraylist/Swap: Invalid right index: %d", right)
	}

	temp := list.elements[left]
	list.elements[left] = list.elements[right]
	list.elements[right] = temp
	return nil
}

func (list *List) Print() {
	var output = "["
	for _, elem := range list.elements {
		output += fmt.Sprintf(" %v", elem)
	}
	output += " ]"
	fmt.Println(output)
}

func (list *List) CopyRange(from int, toCopy []interface{}) error {
	if from < 0 || from > list.Size() {
		return fmt.Errorf("golib/ArrayList/CopyRange: Invalid start index: %d", from)
	}

	oldSize := list.Size()
	for i := 0; i < len(toCopy); i++ {
		pos := from + i
		if pos >= oldSize {
			list.elements = append(list.elements[:pos], toCopy[i])
		} else {
			list.elements[pos] = toCopy[i]
		}
	}

	return nil

}

//private funcs
func (list *List) add(elements []interface{}) {
	if cap(list.elements) <= list.Size()+len(elements) {
		list.grow(len(elements))
	}

	for _, element := range elements {
		list.elements = append(list.elements, element)
	}
}

func (list *List) grow(n int) {
	curSize := list.Size()
	newElements := make([]interface{}, curSize, (curSize + n) * 2)
	copy(newElements, list.elements)
	list.elements = newElements
}

func (list *List) shrink() {
	curSize := list.Size()
	newElements := make([]interface{}, curSize, (curSize + 1) * 2)
	copy(newElements, list.elements)
	list.elements = newElements
}

func (list *List) withinRange(index int) bool {
	return index >= 0 && index < list.Size()
}
