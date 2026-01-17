package main

import "fmt"

func main() {
	s := "ézbro"
	fmt.Printf("%8T %[1]v\n", s)
	fmt.Printf("%8T %[1]v\n", []rune(s))
	fmt.Printf("%8T %[1]v\n", []byte(s))
}
