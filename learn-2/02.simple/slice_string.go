package main

import (
	"fmt"
)

func main() {
	test_slice := []string{"abc", "asd", "ok"}

	for k, v := range test_slice {
		fmt.Printf("Key: %v and Value: %s \n", k, v)
	}

	fmt.Println("=========")

	for _, v := range test_slice {
		fmt.Printf("Value: %s \n", v)
	}
}

/*
Key: 0 and Value: abc
Key: 1 and Value: asd
Key: 2 and Value: ok
=========
Value: abc
Value: asd
Value: ok
*/
