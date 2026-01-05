# Ref/Source:
- https://refactoring.guru/design-patterns/adapter

# Explains
# Adapter Design Pattern

Adapter là một trong những mẫu thiết kế cấu trúc (structural pattern) rất hữu ích và dễ hiểu, bạn ạ. Hãy tưởng tượng như bạn có một cái sạc điện thoại châu Âu nhưng ổ cắm ở Việt Nam lại khác - bạn cần một cái "adapter" để kết nối chúng lại với nhau.

Trong lập trình cũng vậy, Adapter giúp hai interface không tương thích có thể làm việc với nhau. Nó như một "người phiên dịch" giữa các code không hợp nhau.

**Khi nào cần dùng Adapter:**
- Khi bạn muốn sử dụng một class có sẵn, nhưng interface của nó không khớp với code của bạn
- Khi bạn cần tái sử dụng code cũ trong hệ thống mới
- Khi bạn cần tích hợp thư viện bên thứ ba vào code của mình

# Adapter Design Pattern trong Golang
Adapter pattern trong Golang cũng có ý tưởng tương tự, nhưng cách triển khai sẽ khác một chút do Golang dùng interface theo cách khác với các ngôn ngữ hướng đối tượng truyền thống. Để dễ hiểu hơn, tôi sẽ dùng ví dụ tương tự về trình phát nhạc nhé.

```go
package main

import "fmt"

// Interface gốc mà code hiện tại của bạn sử dụng
type MediaPlayer interface {
	Play(fileName string)
}

// Struct hiện tại chỉ chơi được MP3
type MP3Player struct{}

func (m *MP3Player) Play(fileName string) {
	fmt.Println("Đang chơi file MP3:", fileName)
}

// Đây là "service" mới bạn muốn sử dụng, 
// nhưng interface của nó không tương thích
type WAVPlayer struct{}

func (w *WAVPlayer) PlayWAV(fileName string) {
	fmt.Println("Đang chơi file WAV:", fileName)
}

// Adapter để WAVPlayer có thể hoạt động như một MediaPlayer
type WAVPlayerAdapter struct {
	wavPlayer *WAVPlayer
}

func (a *WAVPlayerAdapter) Play(fileName string) {
	// Chuyển đổi lời gọi Play thành PlayWAV
	a.wavPlayer.PlayWAV(fileName)
}

func main() {
	// Sử dụng player MP3 thông thường
	var player MediaPlayer = &MP3Player{}
	player.Play("baihat.mp3")
	
	// Sử dụng adapter cho WAV player
	wavPlayer := &WAVPlayer{}
	wavAdapter := &WAVPlayerAdapter{wavPlayer: wavPlayer}
	
	// Giờ có thể dùng wavAdapter như một MediaPlayer
	wavAdapter.Play("baihat.wav")
}
```

Trong ví dụ này:

1. `MediaPlayer` là interface mà code hiện tại của bạn đang sử dụng
2. `WAVPlayer` là một struct mới có phương thức khác (`PlayWAV` thay vì `Play`)
3. `WAVPlayerAdapter` làm cầu nối giữa hai interface không tương thích

Ưu điểm của Go là bạn không cần phải khai báo rõ ràng rằng một struct implement một interface. Nếu struct của bạn có tất cả các phương thức mà interface yêu cầu, thì nó đã ngầm implement interface đó rồi. 

Điều này làm cho việc tạo adapter trong Go rất thuận tiện, đặc biệt khi bạn muốn sử dụng các thư viện bên thứ ba hoặc tích hợp các hệ thống không cùng thiết kế ban đầu.

Pattern này đặc biệt hữu ích trong Golang khi:
- Bạn cần dùng một thư viện bên ngoài có API khác với code của bạn
- Bạn đang chuyển đổi code cũ sang cách viết mới
- Bạn muốn tích hợp nhiều dịch vụ khác nhau vào một hệ thống

