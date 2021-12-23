package comparable

import (
	"testing"
)

func TestComparable(t *testing.T) {
	if ret := Compare(2, 3); ret >= 0 {
		t.Errorf("error.")
	}

	if ret := Compare("2", "3"); ret >= 0 {
		t.Error("Compare error")
	}
}
