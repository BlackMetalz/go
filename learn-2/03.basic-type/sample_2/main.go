package main

import (
	"fmt"
	"os"
)

func main() {
	dir, err := os.Getwd()
	if err != nil {
		panic(err)
	}
	fmt.Println("Hello World + os", dir)

	// Ok, fucking loop time bro
	var sum float64
	var n int
	for {
		var val float64

		_, err := fmt.Fscanln(os.Stdin, &val)
		if err != nil {
			break // ctrl+D ==> Exit gracefully
		}
		sum += val
		n++
	}

	if n == 0 {
		fmt.Fprintln(os.Stderr, "No Value")
		os.Exit(-1)
	}

	fmt.Println("The avg: ", sum/float64(n))
}
