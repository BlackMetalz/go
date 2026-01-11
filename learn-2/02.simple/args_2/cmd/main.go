package main

import (
	"fmt"
	"learn-2/args_2/hello"
	"os"
)

func main() {
	if len(os.Args) > 1 {
		fmt.Println(hello.Say(os.Args[1]))
	} else {
		fmt.Println(hello.Say("no args"))
	}
}
