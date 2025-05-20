# Ref/Source:
- https://refactoring.guru/design-patterns/bridge

# Bridge Design Pattern trong Golang

Đúng rồi, sau Adapter thì đến Bridge. Bridge pattern cũng là một trong những mẫu thiết kế cấu trúc (structural) thú vị.

Bạn có thể tưởng tượng Bridge như một cây cầu nối hai bờ sông. Mẫu thiết kế này giúp tách biệt phần trừu tượng (abstraction) khỏi phần thực thi (implementation) của nó. Điều này cho phép hai phần phát triển độc lập mà không ảnh hưởng đến nhau.

## Vấn đề Bridge giải quyết

Giả sử bạn có các lớp hình dạng (Shape) như hình tròn, hình vuông, và bạn muốn thêm màu sắc cho chúng (đỏ, xanh, vàng). Nếu thiết kế thông thường, bạn sẽ phải tạo rất nhiều lớp con: HinhTronDo, HinhTronXanh, HinhVuongDo, HinhVuongXanh...

Với mỗi sự kết hợp mới, số lượng lớp tăng theo cấp số nhân. Bridge pattern giúp giải quyết vấn đề này.

## Ví dụ Bridge pattern trong Golang:

```go
package main

import "fmt"

// Interface cho phần implementation (phần thực thi)
type DrawAPI interface {
    DrawCircle(radius, x, y int)
    DrawSquare(side, x, y int)
}

// Các implementation cụ thể
type RedRenderer struct{}

func (r *RedRenderer) DrawCircle(radius, x, y int) {
    fmt.Printf("Vẽ hình tròn màu ĐỎ [bán kính: %d, x: %d, y: %d]\n", radius, x, y)
}

func (r *RedRenderer) DrawSquare(side, x, y int) {
    fmt.Printf("Vẽ hình vuông màu ĐỎ [cạnh: %d, x: %d, y: %d]\n", side, x, y)
}

type BlueRenderer struct{}

func (b *BlueRenderer) DrawCircle(radius, x, y int) {
    fmt.Printf("Vẽ hình tròn màu XANH [bán kính: %d, x: %d, y: %d]\n", radius, x, y)
}

func (b *BlueRenderer) DrawSquare(side, x, y int) {
    fmt.Printf("Vẽ hình vuông màu XANH [cạnh: %d, x: %d, y: %d]\n", side, x, y)
}

// Phần abstraction (phần trừu tượng)
type Shape interface {
    Draw()
}

// Các lớp cụ thể của abstraction
type Circle struct {
    x, y, radius int
    drawAPI      DrawAPI // Đây là Bridge (cầu nối)
}

func NewCircle(radius, x, y int, drawAPI DrawAPI) *Circle {
    return &Circle{
        x:       x,
        y:       y,
        radius:  radius,
        drawAPI: drawAPI,
    }
}

func (c *Circle) Draw() {
    c.drawAPI.DrawCircle(c.radius, c.x, c.y)
}

type Square struct {
    x, y, side int
    drawAPI    DrawAPI // Đây là Bridge (cầu nối)
}

func NewSquare(side, x, y int, drawAPI DrawAPI) *Square {
    return &Square{
        x:       x,
        y:       y,
        side:    side,
        drawAPI: drawAPI,
    }
}

func (s *Square) Draw() {
    s.drawAPI.DrawSquare(s.side, s.x, s.y)
}

func main() {
    redRenderer := &RedRenderer{}
    blueRenderer := &BlueRenderer{}

    // Tạo một hình tròn với renderer màu đỏ
    redCircle := NewCircle(5, 10, 10, redRenderer)
    
    // Tạo một hình vuông với renderer màu xanh
    blueSquare := NewSquare(4, 20, 20, blueRenderer)

    // Vẽ các hình
    redCircle.Draw()
    blueSquare.Draw()
    
    // Dễ dàng đổi renderer mà không phải tạo lớp mới
    blueCircle := NewCircle(7, 30, 30, blueRenderer)
    blueCircle.Draw()
}
```

## Điểm mấu chốt của Bridge pattern:

1. **Tách biệt hai khía cạnh** (abstraction và implementation) để chúng có thể thay đổi độc lập

2. **Cấu trúc cầu nối**: Abstraction (Shape) chứa một tham chiếu đến Implementation (DrawAPI)

3. **Dễ mở rộng**: Bạn có thể thêm hình dạng mới hoặc cách vẽ mới mà không cần sửa đổi code hiện có

4. **Giảm số lượng lớp**: Thay vì tạo m×n lớp (m hình dạng × n màu sắc), bạn chỉ cần m+n lớp

Ví dụ thực tế: Bạn có thể sử dụng Bridge pattern khi làm việc với nhiều nền tảng đồ họa khác nhau (OpenGL, DirectX), nhiều loại thiết bị (Windows, Linux, Mac), hoặc thậm chí kết nối đến nhiều loại database.

Điều quan trọng là Bridge khác với Adapter ở chỗ nào? 
- Adapter kết nối hai interface **không tương thích**
- Bridge được thiết kế **ngay từ đầu** để tách biệt abstraction và implementation

Mẫu này hơi khó nắm bắt ban đầu nhưng khi bạn hiểu rồi thì nó cực kỳ mạnh mẽ!