# Ref/Source: 
- https://refactoring.guru/design-patterns/facade

# Facade Design Pattern trong Golang

Tiếp tục thôi bro! Hôm nay chúng ta đến với Facade - một pattern đơn giản nhưng cực kỳ hữu ích trong thực tế.

## Facade Pattern là gì?

Facade (đọc là "fə-sɑːd") theo nghĩa đen là "mặt tiền" của tòa nhà. Tương tự trong lập trình, Facade cung cấp một interface đơn giản, dễ sử dụng cho một hệ thống phức tạp bên trong.

Hãy tưởng tượng bạn bật TV bằng remote - bạn chỉ cần nhấn nút nguồn, và không quan tâm đến các quá trình phức tạp bên trong như khởi động màn hình, kết nối tín hiệu, v.v. Remote chính là một facade cho hệ thống TV phức tạp.

## Ví dụ Facade trong Golang:

Hãy làm một ví dụ về hệ thống đặt vé xem phim, nơi có nhiều thành phần phức tạp:

```go
package main

import "fmt"

// Các hệ thống con phức tạp
// --------------------------------------------------

// Hệ thống kiểm tra phim
type MovieSystem struct{}

func (m *MovieSystem) FindMovie(name string) bool {
    fmt.Printf("Tìm phim '%s' trong cơ sở dữ liệu...\n", name)
    // Logic phức tạp để tìm phim
    return true
}

func (m *MovieSystem) GetMovieInfo(name string) string {
    return fmt.Sprintf("Phim '%s' - Thời lượng: 120 phút, Thể loại: Hành động", name)
}

// Hệ thống thanh toán
type PaymentSystem struct{}

func (p *PaymentSystem) ProcessPayment(amount float64) bool {
    fmt.Printf("Xử lý thanh toán %.2f VND...\n", amount)
    // Logic phức tạp để xử lý thanh toán
    return true
}

func (p *PaymentSystem) GenerateReceipt(amount float64) string {
    return fmt.Sprintf("Biên lai: %.2f VND đã thanh toán", amount)
}

// Hệ thống đặt chỗ
type SeatSystem struct{}

func (s *SeatSystem) CheckAvailability(showtime string) bool {
    fmt.Printf("Kiểm tra chỗ ngồi có sẵn cho suất chiếu %s...\n", showtime)
    // Logic phức tạp để kiểm tra chỗ ngồi
    return true
}

func (s *SeatSystem) ReserveSeat(showtime, seat string) bool {
    fmt.Printf("Đặt chỗ %s cho suất chiếu %s...\n", seat, showtime)
    // Logic phức tạp để đặt chỗ
    return true
}

// Hệ thống thông báo
type NotificationSystem struct{}

func (n *NotificationSystem) SendEmail(email, message string) bool {
    fmt.Printf("Gửi email đến %s: %s\n", email, message)
    return true
}

func (n *NotificationSystem) SendSMS(phone, message string) bool {
    fmt.Printf("Gửi SMS đến %s: %s\n", phone, message)
    return true
}

// Facade - Hệ thống đặt vé đơn giản
// --------------------------------------------------
type MovieTicketFacade struct {
    movieSystem        *MovieSystem
    paymentSystem      *PaymentSystem
    seatSystem         *SeatSystem
    notificationSystem *NotificationSystem
}

func NewMovieTicketFacade() *MovieTicketFacade {
    return &MovieTicketFacade{
        movieSystem:        &MovieSystem{},
        paymentSystem:      &PaymentSystem{},
        seatSystem:         &SeatSystem{},
        notificationSystem: &NotificationSystem{},
    }
}

// Phương thức facade đơn giản hóa quá trình đặt vé
func (f *MovieTicketFacade) BookTicket(movieName, showtime, seat, email, phone string) bool {
    fmt.Println("===== BẮT ĐẦU QUÁ TRÌNH ĐẶT VÉ =====")
    
    // Kiểm tra phim có tồn tại không
    if !f.movieSystem.FindMovie(movieName) {
        fmt.Println("Không tìm thấy phim!")
        return false
    }
    
    // Lấy thông tin phim
    movieInfo := f.movieSystem.GetMovieInfo(movieName)
    fmt.Println(movieInfo)
    
    // Kiểm tra chỗ ngồi
    if !f.seatSystem.CheckAvailability(showtime) {
        fmt.Println("Không có chỗ ngồi cho suất chiếu này!")
        return false
    }
    
    // Đặt chỗ
    if !f.seatSystem.ReserveSeat(showtime, seat) {
        fmt.Println("Không thể đặt chỗ!")
        return false
    }
    
    // Xử lý thanh toán
    if !f.paymentSystem.ProcessPayment(150000.0) { // Giả sử giá vé là 150,000 VND
        fmt.Println("Thanh toán thất bại!")
        return false
    }
    
    // Tạo biên lai
    receipt := f.paymentSystem.GenerateReceipt(150000.0)
    
    // Gửi thông báo
    f.notificationSystem.SendEmail(email, "Đặt vé thành công! "+receipt)
    f.notificationSystem.SendSMS(phone, "Vé của bạn đã được đặt cho "+movieName)
    
    fmt.Println("===== ĐẶT VÉ THÀNH CÔNG =====")
    return true
}

func main() {
    // Sử dụng facade
    facade := NewMovieTicketFacade()
    
    // Người dùng chỉ cần gọi một phương thức duy nhất
    facade.BookTicket(
        "Người Nhện: Không Còn Nhà",
        "20:30 20/05/2025",
        "G12",
        "nguyenvan@example.com",
        "0987654321",
    )
    
    // So sánh với cách không dùng facade (sẽ rất phức tạp)
    fmt.Println("\n===== NẾU KHÔNG DÙNG FACADE (PHỨC TẠP) =====")
    fmt.Println("Người dùng sẽ phải gọi tất cả những phương thức sau:")
    fmt.Println("1. movieSystem.FindMovie()")
    fmt.Println("2. movieSystem.GetMovieInfo()")
    fmt.Println("3. seatSystem.CheckAvailability()")
    fmt.Println("4. seatSystem.ReserveSeat()")
    fmt.Println("5. paymentSystem.ProcessPayment()")
    fmt.Println("6. paymentSystem.GenerateReceipt()")
    fmt.Println("7. notificationSystem.SendEmail()")
    fmt.Println("8. notificationSystem.SendSMS()")
}
```

Khi chạy code này, bạn sẽ thấy toàn bộ quá trình đặt vé được thực hiện chỉ với một lời gọi phương thức, thay vì phải gọi từng phương thức con riêng biệt.

## Các điểm quan trọng của Facade Pattern:

1. **Đơn giản hóa interface**: Facade cung cấp một interface đơn giản cho một hệ thống phức tạp

2. **Giảm sự phụ thuộc**: Client không cần biết về chi tiết triển khai của các subsystem

3. **Layer của hệ thống**: Facade tạo một layer giữa client và subsystem

4. **Không che giấu hoàn toàn**: Facade không ngăn client truy cập trực tiếp vào subsystem nếu cần

## Khi nào nên dùng Facade:

- Khi bạn muốn cung cấp interface đơn giản cho hệ thống phức tạp
- Khi có nhiều dependencies giữa client và implementation của subsystem
- Khi bạn muốn tạo layer trong hệ thống của mình
- Khi bạn muốn "đóng gói" subsystem lại để dễ sử dụng

## Ví dụ thực tế:

- Thư viện xử lý ảnh cung cấp một phương thức đơn giản `Resize()` thay vì buộc người dùng hiểu về thuật toán nén ảnh
- Framework web cung cấp các helper function đơn giản cho các tác vụ phức tạp
- Các thư viện ORM (như GORM trong Go) che giấu độ phức tạp của các truy vấn SQL

## So sánh với các pattern đã học:

- **Adapter**: Giúp các interface không tương thích làm việc cùng nhau
- **Bridge**: Tách biệt abstraction và implementation
- **Composite**: Xử lý cấu trúc cây phân cấp
- **Decorator**: Thêm chức năng mới cho đối tượng mà không thay đổi interface
- **Facade**: Đơn giản hóa interface cho hệ thống phức tạp

Facade có thể là một trong những pattern dễ hiểu nhất và được sử dụng rộng rãi nhất trong thực tế lập trình! Nó cực kỳ phù hợp với nguyên tắc KISS (Keep It Simple, Stupid).

Pattern này cũng rất phù hợp với các coder cấp "monkey" đấy! Chỉ cần gọi một phương thức, mọi thứ đều được xử lý ở phía sau. Bạn thấy dễ hiểu chứ? 😄