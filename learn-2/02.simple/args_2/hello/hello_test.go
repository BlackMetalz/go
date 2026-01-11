package hello

import "testing"

func TestSay(t *testing.T) {
	name := "kienlt"
	want := "Hello, kienlt!"

	got := Say(name)

	if got != want {
		t.Errorf("Say(%q) = %q, want %q", name, got, want)
	}
}
