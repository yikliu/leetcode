package comparable

import (
	"fmt"
	"reflect"
)

type Comparable func(c1 interface{}, c2 interface{}) int

func Compare(x interface{}, y interface{}) int {
	typex := reflect.TypeOf(x)
	typey := reflect.TypeOf(y)

	if typex.Kind() != typey.Kind() {
		panic(fmt.Sprintf("golib/comparable/Compare: x (%T) and y (%T) are of different types", typex, typey))
	}

	if !typex.Comparable() {
		panic(fmt.Sprintf("golib/comparable/Compare: type (%T) is not comparable", typex))
	}

	switch t := x.(type) {
	default:
		panic(fmt.Sprintf("unexpected type %T", t)) // %T prints whatever type t has
	case int:
		return IntComparator(x, y)
	case string:
		return StringComparator(x, y)

	}
}

func IntComparator(a, b interface{}) int {
	aInt := a.(int)
	bInt := b.(int)
	switch {
	case aInt > bInt:
		return 1
	case aInt < bInt:
		return -1
	default:
		return 0
	}
}

func StringComparator(a, b interface{}) int {
	s1 := a.(string)
	s2 := b.(string)
	min := len(s2)
	if len(s1) < len(s2) {
		min = len(s1)
	}
	diff := 0
	for i := 0; i < min && diff == 0; i++ {
		diff = int(s1[i]) - int(s2[i])
	}
	if diff == 0 {
		diff = len(s1) - len(s2)
	}
	if diff < 0 {
		return -1
	}
	if diff > 0 {
		return 1
	}
	return 0
}
