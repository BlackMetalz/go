package main

import (
	"fmt"
	"learn-2/args_3/hello"
	"os"
)

func main() {

	fmt.Println(hello.Say(os.Args[1:]))

}
