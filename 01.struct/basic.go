// Declare and init a basic struct
package main

import (
	"encoding/json"
	"fmt"
)

type Person struct {
	Name string `json:"name"` // struct tags
	Age  int    `json:"age,string"` // struct tags
	Income float64 `json:"income,omitempty"` // struct tags
	Title string `json:"title"` // struct tags
}

func main() {
	// Declare and init a struct
	var p1 Person
	p1.Name = "John"
	p1.Age = 30
	p1.Income = 50000.99
	p1.Title = "Software Engineer"

	fmt.Println(p1)
	fmt.Println(p1.Name)
	fmt.Println(p1.Age)
	fmt.Println(p1.Income)
	fmt.Println(p1.Title)

	p2 := Person{Name: "Jane", Age: 25, Income: 60000.99, Title: "Data Scientist"}
	fmt.Println("\n", p2)

	jsonData, _ := json.Marshal(p2)
	fmt.Println(jsonData) // raw, binary data
	fmt.Println(string(jsonData))
}