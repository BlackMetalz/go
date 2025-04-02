package main

import (
    "fmt"
    "time"
)

func main() {
    const iterations = 1000000 // Số lần lặp: 1 triệu
    x := 5                       // Giá trị ban đầu

    // Đo thời gian dùng phép nhân (*)
    startMultiply := time.Now()
    for i := 0; i < iterations; i++ {
        _ = x * 8 // Nhân với 8
    }
    durationMultiply := time.Since(startMultiply)

    // Đo thời gian dùng bitwise shift (<<)
    startShift := time.Now()
    for i := 0; i < iterations; i++ {
        _ = x << 3 // Dịch trái 3 lần (tương đương nhân 8)
    }
    durationShift := time.Since(startShift)

    // In kết quả
    fmt.Printf("Thời gian dùng phép nhân (*): %v\n", durationMultiply)
    fmt.Printf("Thời gian dùng bitwise shift (<<): %v\n", durationShift)

    // So sánh
    if durationMultiply > durationShift {
        diff := durationMultiply - durationShift
        fmt.Printf("Bitwise shift nhanh hơn: %v\n", diff)
    } else {
        diff := durationShift - durationMultiply
        fmt.Printf("Phép nhân nhanh hơn: %v\n", diff)
    }
}