package math

import "testing"

func TestAdd(t *testing.T) {
    if Add(2, 3) != 5 {
        t.Error("Add(2, 3) should be 5")
    }
}