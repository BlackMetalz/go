# Ref/Source:
- https://refactoring.guru/design-patterns/flyweight

# Flyweight Design Pattern trong Golang

Nhào vô tiếp nào bro! Flyweight là một pattern khá đặc biệt, nó giúp tiết kiệm bộ nhớ khi bạn cần tạo nhiều object giống nhau.

## Flyweight Pattern là gì?

Flyweight giống như câu chuyện về thư viện sách. Thay vì mỗi người đều mua một cuốn sách riêng, nhiều người có thể dùng chung một cuốn từ thư viện - họ chỉ "mượn" nó khi cần.

Pattern này giúp bạn tiết kiệm RAM bằng cách chia sẻ phần dữ liệu chung giữa nhiều đối tượng tương tự nhau, thay vì lưu trữ dữ liệu đó trong mỗi đối tượng.

## Phân biệt trạng thái bên trong/bên ngoài

Để hiểu Flyweight, bạn cần phân biệt:
- **Trạng thái bên trong (intrinsic state)**: Dữ liệu không thay đổi, có thể chia sẻ (như hình dạng, màu sắc cơ bản)
- **Trạng thái bên ngoài (extrinsic state)**: Dữ liệu thay đổi theo ngữ cảnh, không thể chia sẻ (như vị trí, tỷ lệ)

## Ví dụ Flyweight trong Golang:

Hãy xây dựng một trò chơi đơn giản với hàng ngàn cây trong rừng:

```go
package main

import (
    "fmt"
    "math/rand"
    "time"
)

// TreeType - flyweight object lưu trữ trạng thái bên trong chia sẻ
type TreeType struct {
    name      string
    color     string
    texture   string
    // Khác với thực tế, ở đây hình ảnh sẽ là một chuỗi đơn giản
    // Nhưng trong game thật, nó có thể là file ảnh lớn, mesh 3D, v.v.
    meshData  string 
}

func (t *TreeType) Render(x, y float64, age int) {
    fmt.Printf("Vẽ cây %s màu %s ở vị trí (%.1f, %.1f), tuổi: %d năm\n", 
               t.name, t.color, x, y, age)
}

// TreeFactory - quản lý việc tạo và tái sử dụng các flyweight
type TreeFactory struct {
    treeTypes map[string]*TreeType
}

func NewTreeFactory() *TreeFactory {
    return &TreeFactory{
        treeTypes: make(map[string]*TreeType),
    }
}

func (f *TreeFactory) GetTreeType(name, color, texture string) *TreeType {
    // Tạo key để xác định TreeType duy nhất
    key := name + "_" + color + "_" + texture
    
    // Kiểm tra xem TreeType đã tồn tại chưa
    if treeType, ok := f.treeTypes[key]; ok {
        fmt.Printf("Tái sử dụng TreeType đã có: %s\n", key)
        return treeType
    }
    
    // Nếu chưa có, tạo mới một TreeType
    fmt.Printf("Tạo TreeType mới: %s\n", key)
    newType := &TreeType{
        name:     name,
        color:    color,
        texture:  texture,
        meshData: fmt.Sprintf("Dữ liệu mesh 3D phức tạp cho %s (khoảng ~10MB)", name),
    }
    
    // Lưu vào cache để tái sử dụng sau này
    f.treeTypes[key] = newType
    return newType
}

// Tree - đối tượng context lưu trữ cả trạng thái bên ngoài và tham chiếu đến flyweight
type Tree struct {
    x, y float64  // Vị trí - trạng thái bên ngoài
    age  int      // Tuổi - trạng thái bên ngoài
    type_ *TreeType // Tham chiếu đến flyweight chia sẻ
}

func NewTree(x, y float64, age int, type_ *TreeType) *Tree {
    return &Tree{
        x:     x,
        y:     y,
        age:   age,
        type_: type_,
    }
}

func (t *Tree) Render() {
    t.type_.Render(t.x, t.y, t.age)
}

// Forest - chứa tất cả các cây
type Forest struct {
    trees []*Tree
}

func NewForest() *Forest {
    return &Forest{
        trees: make([]*Tree, 0),
    }
}

func (f *Forest) PlantTree(x, y float64, age int, name, color, texture string, factory *TreeFactory) {
    treeType := factory.GetTreeType(name, color, texture)
    tree := NewTree(x, y, age, treeType)
    f.trees = append(f.trees, tree)
}

func (f *Forest) Render() {
    for _, tree := range f.trees {
        tree.Render()
    }
}

func main() {
    // Cài đặt seed cho random
    rand.Seed(time.Now().UnixNano())
    
    // Tạo factory và forest
    factory := NewTreeFactory()
    forest := NewForest()
    
    // Các loại cây
    treeData := []struct {
        name    string
        color   string
        texture string
    }{
        {"Cây thông", "xanh đậm", "vỏ thô"},
        {"Cây sồi", "xanh nhạt", "vỏ nứt"},
        {"Cây bạch dương", "trắng", "vỏ mịn"},
    }
    
    // Trồng 10 cây với thông tin ngẫu nhiên
    fmt.Println("===== TRỒNG CÂY TRONG RỪNG =====")
    for i := 0; i < 10; i++ {
        // Chọn ngẫu nhiên một loại cây
        treeInfo := treeData[rand.Intn(len(treeData))]
        
        // Vị trí và tuổi ngẫu nhiên
        x := rand.Float64() * 100
        y := rand.Float64() * 100
        age := rand.Intn(20) + 1
        
        forest.PlantTree(
            x, y, age,
            treeInfo.name, treeInfo.color, treeInfo.texture,
            factory,
        )
    }
    
    // Hiển thị các cây
    fmt.Println("\n===== RENDER RỪNG =====")
    forest.Render()
    
    // Hiển thị thông tin bộ nhớ
    fmt.Println("\n===== THÔNG TIN BỘ NHỚ =====")
    fmt.Printf("Số loại cây (TreeTypes) đã tạo: %d\n", len(factory.treeTypes))
    fmt.Printf("Tổng số cây thực tế: %d\n", len(forest.trees))
    
    // Mô phỏng tiết kiệm bộ nhớ
    memorySaved := (len(forest.trees) - len(factory.treeTypes)) * 10
    fmt.Printf("Tiết kiệm bộ nhớ ước tính: ~%d MB\n", memorySaved)
}
```

Khi chạy code này, bạn sẽ thấy:
1. Chỉ có một số ít TreeType được tạo
2. Nhiều cây chia sẻ cùng một TreeType
3. Thông tin về bộ nhớ đã tiết kiệm được

## Các điểm quan trọng của Flyweight Pattern:

1. **Tiết kiệm bộ nhớ**: Chia sẻ đối tượng thay vì tạo mới giúp giảm đáng kể bộ nhớ sử dụng

2. **Tách biệt trạng thái**: Phân biệt rõ ràng trạng thái bên trong (chia sẻ) và bên ngoài (ngữ cảnh)

3. **Cache và tái sử dụng**: Sử dụng factory để quản lý việc tạo và lưu trữ các flyweight

4. **Không đổi (Immutable)**: Các flyweight object thường là không đổi để có thể chia sẻ an toàn

## Khi nào nên dùng Flyweight:

- Khi ứng dụng cần tạo rất nhiều đối tượng tương tự nhau
- Khi bộ nhớ là vấn đề quan trọng (ứng dụng di động, game, v.v.)
- Khi đối tượng có thể chia thành phần chia sẻ và phần phụ thuộc ngữ cảnh
- Khi bạn có dữ liệu lớn giống nhau trong nhiều đối tượng (như texture, font, icon)

## Ví dụ thực tế:

- **Trong game**: Các texture, mesh 3D, âm thanh được chia sẻ giữa nhiều đối tượng
- **Trong trình soạn thảo text**: Các ký tự và định dạng văn bản
- **Trong ứng dụng bản đồ**: Biểu tượng địa điểm và texture địa hình

## So sánh với các pattern đã học:

- **Adapter**: Giúp các interface không tương thích làm việc cùng nhau
- **Bridge**: Tách biệt abstraction và implementation
- **Composite**: Xử lý cấu trúc cây phân cấp
- **Decorator**: Thêm chức năng mới cho đối tượng
- **Facade**: Đơn giản hóa interface cho hệ thống phức tạp
- **Flyweight**: Tiết kiệm bộ nhớ bằng cách chia sẻ phần chung giữa các đối tượng

Flyweight pattern rất hữu ích trong các tình huống cần tối ưu hóa bộ nhớ, đặc biệt là trong game development hoặc các ứng dụng xử lý đồ họa nặng. 

Để tổng kết: Flyweight giống như việc nhiều người cùng mượn một quyển sách từ thư viện, thay vì mỗi người mua một bản sao của quyển sách đó về nhà.

Thấy pattern này phức tạp hơn mấy cái trước không bro? 🤔