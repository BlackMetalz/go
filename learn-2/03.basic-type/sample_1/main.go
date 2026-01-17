package main

import "fmt"

func main() {
	a := 2
	b := 3.1
	// %8T: print type with 8 space
	fmt.Printf("a: %8T %[1]v \n", a)
	fmt.Printf("b: %8T %[1]v \n", b)

	// parse float to int
	a = int(b)
	fmt.Printf("a: %8T %[1]v \n", a)
	// try to convert it again
	b = float64(a)
	fmt.Printf("b: %8T %[1]v \n", b)
	// Nothing happens because 3.1 -> 3 -> 3.0
}
