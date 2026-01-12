package hello

import (
	"testing"
)

func TestSay(t *testing.T) {
	// Ok, unit tests with more subtest
	// Init slice of struct
	subtests := []struct {
		items  []string
		result string
	}{
		{
			result: "Hello, Default without args!",
		}, // First item for default case, if args = 0
		{
			items:  []string{"Kienlt"},
			result: "Hello, Kienlt!",
		},
		{
			items:  []string{"Kienlt", "Bro"},
			result: "Hello, Kienlt, Bro!",
		},
	}
	for _, st := range subtests {
		if s := Say(st.items); s != st.result {
			t.Errorf("wanted %s (%v), got %s", st.result, st.items, s)
		}
	}
}
