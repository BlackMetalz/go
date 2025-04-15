package main

import (
	"testing"
)

func TestGetUser(t *testing.T) {
	md := &MockDataStore{
		Users: map[int]User{
			1: {ID: 1, First: "John"},
		},
	}

	s := &Service{
		ds: md,
	}

	u ,err := s.GetUser(1)
	if err != nil {
		t.Fatalf("Expected no error, got %v", err)
	}

	if u.First != "John" {
		t.Fatalf("Expected John, got %s", u.First)
	}
}
