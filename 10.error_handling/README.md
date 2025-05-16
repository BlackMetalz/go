Trong Go, `error` là một interface, không phải một type cụ thể. Interface `error` được định nghĩa trong thư viện chuẩn của Go như sau:

```go
type error interface {
    Error() string
}
```

Bất kỳ type nào implement method `Error() string` thì đều được coi là implement interface `error`. Điều này có nghĩa là bạn có thể tạo các type riêng của mình và làm cho chúng trở thành error bằng cách implement method này.

Đúng như bạn nói, mỗi type mà implement interface error (tức là implement method `Error() string`) thì đều có thể được sử dụng ở bất kỳ đâu mà type `error` được yêu cầu. Điều này rất hữu ích vì nó cho phép bạn tạo các loại lỗi tùy chỉnh với thông tin bổ sung mà vẫn duy trì khả năng tương thích với các hàm xử lý lỗi tiêu chuẩn.

Ví dụ:

```go
type MyError struct {
    Code    int
    Message string
}

func (e *MyError) Error() string {
    return fmt.Sprintf("code %d: %s", e.Code, e.Message)
}

func someFunction() error {
    // Trả về lỗi tùy chỉnh
    return &MyError{Code: 500, Message: "something went wrong"}
}

func main() {
    err := someFunction()
    if err != nil {
        fmt.Println(err) // In ra: "code 500: something went wrong"
    }
}
```