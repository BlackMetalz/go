# Ref/Source:
https://refactoring.guru/design-patterns/composite

# Composite Design Pattern trong Golang

Tiếp theo chúng ta có Composite pattern - một mẫu thiết kế cấu trúc rất hữu ích khi bạn cần làm việc với cấu trúc cây (tree).

## Composite Pattern là gì?

Hãy tưởng tượng bạn có một cái cây gia phả, mỗi người trong gia đình có thể là một cá nhân đơn lẻ hoặc có thể là cha/mẹ (có con cái). Composite pattern cho phép bạn xử lý cả "lá" (đối tượng đơn lẻ) và "nhánh" (nhóm đối tượng) theo cùng một cách.

Pattern này giúp bạn tạo ra cấu trúc cây phân cấp, nơi mà bạn có thể xử lý từng đối tượng riêng lẻ hoặc nhóm đối tượng một cách đồng nhất.

## Ví dụ Composite trong Golang:

Hãy làm một ví dụ về cấu trúc thư mục trong máy tính, nơi có cả file (đối tượng đơn lẻ) và folder (nhóm đối tượng):

```go
package main

import "fmt"

// Component interface đại diện cho cả file và folder
type FileSystemComponent interface {
    GetName() string
    GetSize() int
    Print(indent string)
}

// File - đại diện cho "lá" (leaf) - không có con
type File struct {
    name string
    size int
}

func NewFile(name string, size int) *File {
    return &File{name: name, size: size}
}

func (f *File) GetName() string {
    return f.name
}

func (f *File) GetSize() int {
    return f.size
}

func (f *File) Print(indent string) {
    fmt.Printf("%s- %s (%d KB)\n", indent, f.name, f.size)
}

// Folder - đại diện cho "composite" - có thể chứa các component khác
type Folder struct {
    name       string
    components []FileSystemComponent
}

func NewFolder(name string) *Folder {
    return &Folder{
        name:       name,
        components: []FileSystemComponent{},
    }
}

func (f *Folder) Add(component FileSystemComponent) {
    f.components = append(f.components, component)
}

func (f *Folder) GetName() string {
    return f.name
}

// Tính tổng kích thước của tất cả các component con
func (f *Folder) GetSize() int {
    totalSize := 0
    for _, component := range f.components {
        totalSize += component.GetSize()
    }
    return totalSize
}

func (f *Folder) Print(indent string) {
    fmt.Printf("%s+ %s (%d KB)\n", indent, f.name, f.GetSize())
    // In tất cả các component con với thụt lề tăng dần
    for _, component := range f.components {
        component.Print(indent + "  ")
    }
}

func main() {
    // Tạo cấu trúc thư mục
    rootFolder := NewFolder("Root")
    
    documentsFolder := NewFolder("Documents")
    rootFolder.Add(documentsFolder)
    
    // Thêm files vào Documents
    documentsFolder.Add(NewFile("resume.docx", 30))
    documentsFolder.Add(NewFile("cover_letter.pdf", 25))
    
    // Thêm một thư mục con vào Documents
    projectsFolder := NewFolder("Projects")
    documentsFolder.Add(projectsFolder)
    
    // Thêm files vào Projects
    projectsFolder.Add(NewFile("project1.go", 10))
    projectsFolder.Add(NewFile("project2.go", 15))
    
    // Thêm thư mục Pictures vào Root
    picturesFolder := NewFolder("Pictures")
    rootFolder.Add(picturesFolder)
    
    // Thêm files vào Pictures
    picturesFolder.Add(NewFile("vacation.jpg", 50))
    picturesFolder.Add(NewFile("family.png", 40))
    
    // Thêm một file trực tiếp vào Root
    rootFolder.Add(NewFile("config.sys", 2))
    
    // In ra cả cây thư mục
    rootFolder.Print("")
}
```

Khi chạy code này, bạn sẽ thấy cấu trúc thư mục phân cấp với kích thước được tính tự động ở mỗi cấp:

```
+ Root (172 KB)
  + Documents (80 KB)
    - resume.docx (30 KB)
    - cover_letter.pdf (25 KB)
    + Projects (25 KB)
      - project1.go (10 KB)
      - project2.go (15 KB)
  + Pictures (90 KB)
    - vacation.jpg (50 KB)
    - family.png (40 KB)
  - config.sys (2 KB)
```

## Các điểm quan trọng của Composite Pattern:

1. **Tính thống nhất**: Cả đối tượng đơn và nhóm đều được xử lý qua một interface chung

2. **Tính đệ quy**: Composite objects (như Folder) có thể chứa các objects khác và gọi phương thức của chúng một cách đệ quy

3. **Dễ mở rộng**: Bạn có thể thêm đối tượng mới vào hệ thống mà không cần thay đổi code hiện có

4. **Dễ sử dụng**: Client không cần biết nó đang làm việc với lá hay nhánh

## Khi nào nên dùng Composite:

- Khi bạn cần biểu diễn cấu trúc cây (như hệ thống file, tổ chức công ty)
- Khi bạn muốn client xử lý đối tượng đơn và nhóm đối tượng một cách giống nhau
- Khi bạn cần tính toán tổng hợp cho cả cây (như tính tổng kích thước, tổng lương...)

Một ví dụ thực tế khác là UI component trong ứng dụng: một button là component đơn, nhưng một panel chứa nhiều button lại là composite, và cả hai đều là UI components có thể vẽ lên màn hình.

So với các mẫu đã học trước:
- Adapter giúp kết nối các interfaces không tương thích
- Bridge tách biệt abstraction và implementation
- Composite giúp xử lý cấu trúc phân cấp dạng cây

