# Ref/Source:
- https://refactoring.guru/design-patterns/proxy

# Proxy Design Pattern trong Golang

Pattern cuối cùng trong ngày hôm nay - Proxy! Đây là một trong những mẫu thiết kế cấu trúc rất phổ biến và hữu ích.

## Proxy Pattern là gì?

Proxy có nghĩa là "người đại diện". Tương tự trong lập trình, Proxy đóng vai trò trung gian, đứng giữa client và đối tượng thực, kiểm soát truy cập đến đối tượng đó.

Hình dung như bạn muốn gọi điện cho sếp, nhưng thư ký (proxy) của sếp sẽ trả lời điện thoại trước. Thư ký có thể:
- Chuyển cuộc gọi cho sếp
- Từ chối nếu sếp bận
- Ghi lại thông tin cuộc gọi
- Thậm chí trả lời thay nếu đó là câu hỏi đơn giản

## Ví dụ Proxy trong Golang:

Hãy làm một ví dụ về hệ thống download file, nơi chúng ta sử dụng proxy để:
1. Cache lại file đã download trước đó (không cần tải lại)
2. Kiểm tra quyền truy cập trước khi cho phép download
3. Ghi log mỗi lần download

```go
package main

import (
    "fmt"
    "time"
)

// Subject interface - định nghĩa hành vi chung cho RealSubject và Proxy
type Downloader interface {
    Download(url string) ([]byte, error)
}

// RealSubject - đối tượng thực hiện chức năng thực sự
type RealDownloader struct{}

func (d *RealDownloader) Download(url string) ([]byte, error) {
    fmt.Printf("Đang download thực từ %s...\n", url)
    // Giả lập quá trình download (sẽ mất thời gian thực tế)
    time.Sleep(2 * time.Second)
    fmt.Println("Download hoàn tất!")
    
    // Trong thực tế, đây sẽ là nội dung file
    // Ở đây chỉ trả về một chuỗi byte giả
    return []byte(fmt.Sprintf("Nội dung của %s", url)), nil
}

// Proxy - đối tượng trung gian
type DownloaderProxy struct {
    realDownloader *RealDownloader
    cache          map[string][]byte  // Cache cho các file đã download
    userRoles      map[string]string  // Vai trò của người dùng
    logFile        string             // File log
}

func NewDownloaderProxy() *DownloaderProxy {
    return &DownloaderProxy{
        realDownloader: &RealDownloader{},
        cache:          make(map[string][]byte),
        userRoles:      map[string]string{
            "admin":    "admin",
            "user1":    "user",
            "user2":    "user",
            "guest":    "guest",
        },
        logFile:        "downloads.log",
    }
}

func (p *DownloaderProxy) Download(url string) ([]byte, error) {
    return p.DownloadByUser(url, "guest")
}

func (p *DownloaderProxy) DownloadByUser(url string, user string) ([]byte, error) {
    // Kiểm tra quyền truy cập (Protection Proxy)
    if !p.checkAccess(url, user) {
        return nil, fmt.Errorf("Từ chối truy cập: Người dùng %s không có quyền download %s", user, url)
    }
    
    // Ghi log (Logging Proxy)
    p.logAccess(url, user)
    
    // Kiểm tra cache (Cache Proxy)
    if data, ok := p.cache[url]; ok {
        fmt.Printf("Trả về từ cache: %s\n", url)
        return data, nil
    }
    
    // Thực hiện download thực sự
    data, err := p.realDownloader.Download(url)
    if err != nil {
        return nil, err
    }
    
    // Lưu vào cache cho lần sau
    p.cache[url] = data
    
    return data, nil
}

// Kiểm tra quyền truy cập
func (p *DownloaderProxy) checkAccess(url string, user string) bool {
    fmt.Printf("Kiểm tra quyền truy cập cho %s...\n", user)
    
    role, exists := p.userRoles[user]
    if !exists {
        return false
    }
    
    // Giả định: Chỉ admin và user mới có thể download
    if role == "admin" || role == "user" {
        return true
    }
    
    return false
}

// Ghi log
func (p *DownloaderProxy) logAccess(url string, user string) {
    timestamp := time.Now().Format("2006-01-02 15:04:05")
    logEntry := fmt.Sprintf("[%s] User: %s, URL: %s\n", timestamp, user, url)
    
    fmt.Printf("Ghi log: %s", logEntry)
    // Trong thực tế, sẽ lưu vào file hoặc database
}

// Ví dụ phương thức phụ trợ
func (p *DownloaderProxy) ClearCache() {
    fmt.Println("Xóa cache...")
    p.cache = make(map[string][]byte)
}

func main() {
    // Tạo proxy
    proxy := NewDownloaderProxy()
    
    fmt.Println("===== TEST 1: DOWNLOAD LẦN ĐẦU =====")
    // Download bằng tài khoản admin
    data1, err := proxy.DownloadByUser("https://example.com/file1.zip", "admin")
    if err != nil {
        fmt.Printf("Lỗi: %v\n", err)
    } else {
        fmt.Printf("Kết quả: %s\n", data1)
    }
    
    fmt.Println("\n===== TEST 2: DOWNLOAD TỪ CACHE =====")
    // Download lại - sẽ dùng cache
    data2, _ := proxy.DownloadByUser("https://example.com/file1.zip", "admin")
    fmt.Printf("Kết quả: %s\n", data2)
    
    fmt.Println("\n===== TEST 3: DOWNLOAD VỚI QUYỀN GUEST (BỊ TỪ CHỐI) =====")
    // Download với tài khoản guest - sẽ bị từ chối
    _, err = proxy.DownloadByUser("https://example.com/file2.zip", "guest")
    if err != nil {
        fmt.Printf("Lỗi: %v\n", err)
    }
    
    fmt.Println("\n===== TEST 4: DOWNLOAD FILE MỚI VỚI USER THƯỜNG =====")
    // Download file khác với tài khoản user thường
    data3, _ := proxy.DownloadByUser("https://example.com/file3.zip", "user1")
    fmt.Printf("Kết quả: %s\n", data3)
    
    fmt.Println("\n===== TEST 5: XÓA CACHE VÀ DOWNLOAD LẠI =====")
    // Xóa cache và download lại
    proxy.ClearCache()
    data4, _ := proxy.DownloadByUser("https://example.com/file1.zip", "user2")
    fmt.Printf("Kết quả: %s\n", data4)
}
```

## Các kiểu Proxy phổ biến:

1. **Protection Proxy**: Kiểm soát quyền truy cập đến đối tượng (như ví dụ trên)
2. **Cache Proxy**: Lưu trữ kết quả tạm thời để cải thiện hiệu suất
3. **Remote Proxy**: Đại diện cho đối tượng ở xa (qua mạng)
4. **Virtual Proxy**: Trì hoãn việc tạo đối tượng tốn kém cho đến khi thực sự cần
5. **Logging Proxy**: Ghi lại các cuộc gọi đến đối tượng gốc
6. **Smart Reference**: Thực hiện các hành động bổ sung khi đối tượng được truy cập

## Các điểm quan trọng của Proxy Pattern:

1. **Kiểm soát truy cập**: Proxy điều khiển cách client tương tác với đối tượng thực

2. **Cùng interface**: Proxy và đối tượng thực triển khai cùng một interface

3. **Đối tượng thay thế**: Client không biết là nó đang làm việc với proxy hay đối tượng thực

4. **Tách biệt trách nhiệm**: Proxy chỉ quản lý truy cập, đối tượng thực thực hiện logic nghiệp vụ

## Khi nào nên dùng Proxy:

- Khi cần kiểm soát truy cập đến đối tượng
- Khi cần thêm chức năng khi truy cập đối tượng (logging, cache...)
- Khi đối tượng thực tốn kém để tạo hoặc truy cập (lazy loading)
- Khi đối tượng thực nằm trên máy chủ từ xa
- Khi cần giới hạn quyền truy cập vào các phương thức cụ thể

## Ví dụ thực tế:

- **Proxy Server** trong mạng máy tính
- **ORM Framework** cung cấp lazy loading cho các đối tượng database
- **Go HTTP Middleware** là ví dụ của proxy
- **gRPC Client Stubs** đóng vai trò là proxy cho remote services

## So sánh với các pattern đã học:

- **Adapter**: Chuyển đổi interface thành dạng khác
- **Decorator**: Thêm chức năng mới cho đối tượng
- **Facade**: Đơn giản hóa interface phức tạp
- **Proxy**: Kiểm soát truy cập đến đối tượng

Điểm khác biệt giữa Proxy và Decorator:
- **Decorator** tập trung vào việc **thêm** chức năng mới
- **Proxy** tập trung vào việc **kiểm soát** truy cập đến chức năng

Đây là pattern khá phổ biến trong thế giới thực, đặc biệt trong các ứng dụng web, ORM, và hệ thống phân tán.

Như vậy, chúng ta đã hoàn thành cả 7 mẫu thiết kế cấu trúc (Structural Patterns) trong ngày hôm nay! Adapter, Bridge, Composite, Decorator, Facade, Flyweight và Proxy. Bạn thấy mình hiểu được bao nhiêu % rồi? Còn câu hỏi nào nữa không?