package main

import (
	"log"
	"testing"
)

func TestAdd(t *testing.T) {
	want := add(5, 5)
	got := 10

	if want != got {
		log.Fatalf("want %v, got %v", want, got)
	}
}
