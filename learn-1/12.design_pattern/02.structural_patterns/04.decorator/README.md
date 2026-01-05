# Ref/Source:
- https://refactoring.guru/design-patterns/decorator

# Decorator Design Pattern trong Golang

Đến với Decorator pattern nào bro! Đây là một trong những pattern cực kỳ hữu ích mà tôi rất thích.

## Decorator Pattern là gì?

Hãy tưởng tượng bạn đang đi mua cà phê. Ban đầu bạn chỉ muốn một ly cà phê đen cơ bản, nhưng sau đó bạn muốn thêm sữa, rồi thêm đường, rồi thêm caramel... Decorator pattern hoạt động giống như vậy - cho phép bạn "trang trí" hoặc "bọc" một đối tượng với các chức năng phụ mà không làm thay đổi đối tượng gốc.

Decorator pattern cho phép bạn mở rộng chức năng của đối tượng tại runtime mà không cần sử dụng kế thừa (thừa kế) phức tạp.

## Ví dụ Decorator trong Golang:

Hãy làm một ví dụ về hệ thống thông báo, nơi bạn có thể gửi thông báo qua nhiều kênh khác nhau:

```go
package main

import "fmt"

// Component interface cơ bản
type Notifier interface {
    Send(message string) string
}

// Component cụ thể - notifier cơ bản
type BasicNotifier struct {
    username string
}

func NewBasicNotifier(username string) *BasicNotifier {
    return &BasicNotifier{username: username}
}

func (n *BasicNotifier) Send(message string) string {
    return fmt.Sprintf("[Thông báo cho %s]: %s", n.username, message)
}

// Base Decorator
type NotifierDecorator struct {
    wrappee Notifier
}

func (d *NotifierDecorator) Send(message string) string {
    return d.wrappee.Send(message)
}

// Decorator cụ thể - SMS Notifier
type SMSDecorator struct {
    NotifierDecorator
    phoneNumber string
}

func NewSMSDecorator(notifier Notifier, phoneNumber string) *SMSDecorator {
    return &SMSDecorator{
        NotifierDecorator: NotifierDecorator{wrappee: notifier},
        phoneNumber:       phoneNumber,
    }
}

func (d *SMSDecorator) Send(message string) string {
    // Gọi phương thức gốc trước
    originalMessage := d.NotifierDecorator.Send(message)
    // Thêm chức năng mới
    return fmt.Sprintf("%s\n  [Đã gửi SMS đến %s]", originalMessage, d.phoneNumber)
}

// Decorator cụ thể - Email Notifier
type EmailDecorator struct {
    NotifierDecorator
    email string
}

func NewEmailDecorator(notifier Notifier, email string) *EmailDecorator {
    return &EmailDecorator{
        NotifierDecorator: NotifierDecorator{wrappee: notifier},
        email:             email,
    }
}

func (d *EmailDecorator) Send(message string) string {
    originalMessage := d.NotifierDecorator.Send(message)
    return fmt.Sprintf("%s\n  [Đã gửi email đến %s]", originalMessage, d.email)
}

// Decorator cụ thể - Slack Notifier
type SlackDecorator struct {
    NotifierDecorator
    channel string
}

func NewSlackDecorator(notifier Notifier, channel string) *SlackDecorator {
    return &SlackDecorator{
        NotifierDecorator: NotifierDecorator{wrappee: notifier},
        channel:           channel,
    }
}

func (d *SlackDecorator) Send(message string) string {
    originalMessage := d.NotifierDecorator.Send(message)
    return fmt.Sprintf("%s\n  [Đã đăng lên kênh Slack #%s]", originalMessage, d.channel)
}

func main() {
    // Tạo notifier cơ bản
    basicNotifier := NewBasicNotifier("TechGuru")
    
    // Thông báo cơ bản
    fmt.Println("1. Thông báo cơ bản:")
    fmt.Println(basicNotifier.Send("Hệ thống sẽ bảo trì vào tối nay"))
    fmt.Println()
    
    // Thông báo qua SMS
    fmt.Println("2. Thông báo qua SMS:")
    smsNotifier := NewSMSDecorator(basicNotifier, "0987654321")
    fmt.Println(smsNotifier.Send("Hệ thống sẽ bảo trì vào tối nay"))
    fmt.Println()
    
    // Thông báo qua Email
    fmt.Println("3. Thông báo qua Email:")
    emailNotifier := NewEmailDecorator(basicNotifier, "techguru@example.com")
    fmt.Println(emailNotifier.Send("Hệ thống sẽ bảo trì vào tối nay"))
    fmt.Println()
    
    // Kết hợp nhiều decorator - thông báo qua cả SMS và Email
    fmt.Println("4. Thông báo qua cả SMS và Email:")
    smsAndEmailNotifier := NewEmailDecorator(
        NewSMSDecorator(basicNotifier, "0987654321"),
        "techguru@example.com",
    )
    fmt.Println(smsAndEmailNotifier.Send("Hệ thống sẽ bảo trì vào tối nay"))
    fmt.Println()
    
    // Thêm cả Slack nữa - SMS + Email + Slack
    fmt.Println("5. Thông báo qua SMS, Email và Slack:")
    fullNotifier := NewSlackDecorator(
        NewEmailDecorator(
            NewSMSDecorator(basicNotifier, "0987654321"),
            "techguru@example.com",
        ),
        "system-alerts",
    )
    fmt.Println(fullNotifier.Send("Hệ thống sẽ bảo trì vào tối nay"))
}
```

Khi chạy code này, bạn sẽ thấy kết quả:

```
1. Thông báo cơ bản:
[Thông báo cho TechGuru]: Hệ thống sẽ bảo trì vào tối nay

2. Thông báo qua SMS:
[Thông báo cho TechGuru]: Hệ thống sẽ bảo trì vào tối nay
  [Đã gửi SMS đến 0987654321]

3. Thông báo qua Email:
[Thông báo cho TechGuru]: Hệ thống sẽ bảo trì vào tối nay
  [Đã gửi email đến techguru@example.com]

4. Thông báo qua cả SMS và Email:
[Thông báo cho TechGuru]: Hệ thống sẽ bảo trì vào tối nay
  [Đã gửi SMS đến 0987654321]
  [Đã gửi email đến techguru@example.com]

5. Thông báo qua SMS, Email và Slack:
[Thông báo cho TechGuru]: Hệ thống sẽ bảo trì vào tối nay
  [Đã gửi SMS đến 0987654321]
  [Đã gửi email đến techguru@example.com]
  [Đã đăng lên kênh Slack #system-alerts]
```

## Các điểm quan trọng của Decorator Pattern:

1. **Mở rộng linh hoạt**: Bạn có thể thêm chức năng mới mà không làm thay đổi code hiện có

2. **Kết hợp tùy ý**: Bạn có thể kết hợp nhiều decorator theo bất kỳ thứ tự nào bạn muốn

3. **Single Responsibility**: Mỗi decorator chỉ có một trách nhiệm cụ thể, dễ quản lý

4. **Thay thế kế thừa**: Decorator sử dụng composition (kết hợp) thay vì inheritance (kế thừa)

## Khi nào nên dùng Decorator:

- Khi bạn muốn thêm chức năng cho đối tượng mà không muốn sửa code của chúng
- Khi việc sử dụng kế thừa không khả thi (quá nhiều lớp con)
- Khi bạn muốn có khả năng thêm/bớt chức năng linh hoạt khi runtime

## Ví dụ thực tế:

- **Trong Go**: Các `io.Reader` và `io.Writer` thường được trang trí (điển hình như `bufio.NewReader`, `gzip.NewReader`)
- **Trong Java**: `InputStream` và các decorator của nó như `BufferedInputStream`, `GZIPInputStream`
- **Trong web**: Middleware trong các web framework là ví dụ điển hình của Decorator pattern

## So sánh với các pattern đã học:

- **Adapter**: Làm cho các interface không tương thích làm việc cùng nhau
- **Bridge**: Tách biệt abstraction và implementation
- **Composite**: Xử lý cấu trúc cây phân cấp
- **Decorator**: Thêm chức năng mới cho đối tượng mà không thay đổi interface

Decorator pattern là một trong những pattern mà bạn sẽ thường xuyên sử dụng trong thực tế! Đặc biệt trong các ngôn ngữ có composition như Go, pattern này cực kỳ hữu ích.

