package main

import "fmt"

type Address struct {
    Street  string
    City    string
    Country string
}

type Employee struct {
    Name    string
    Age     int
    HomeAddress Address
    WorkAddress *Address  // pointer to Address
}


func main() {
    emp := Employee{
        Name: "Black",
        Age:  30,
        HomeAddress: Address{
            Street:  "123 Main St",
            City:    "Hanoi",
            Country: "Vietnam",
        },
        WorkAddress: &Address{
            Street:  "456 Work Ave",
            City:    "Ho Chi Minh",
            Country: "Vietnam",
        },
    }
    
    fmt.Println(emp.Name)
    fmt.Println(emp.HomeAddress.City)
    fmt.Println(emp.WorkAddress.City)
}

/*
Black
Hanoi
Ho Chi Minh
*/