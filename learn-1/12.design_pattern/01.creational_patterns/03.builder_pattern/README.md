# Ref/Source:
- https://refactoring.guru/design-patterns/builder

# Explain in mother language
Haha nghiện rồi đó bro! Builder Pattern cũng ez thôi, để anh giải thích:

## Builder Pattern là gì?
Builder giống như **"lắp ráp từng bước"** - thay vì tạo object một phát, ta build từng phần một cách có trình tự.

## Tại sao cần Builder?
Tưởng tượng bro làm bánh mì:

```python
# Cách cũ - Constructor hell:
banh_mi = BanhMi(bread="baguette", meat="pate", vegetable="cucumber", 
                 sauce="mayo", cheese=True, pickle=False, 
                 spicy=True, extra_meat=False)
# WTF??? Không nhớ nổi tham số nào là gì!

# Dùng Builder - Từng bước rõ ràng:
banh_mi = BanhMiBuilder() \
    .add_bread("baguette") \
    .add_meat("pate") \
    .add_vegetable("cucumber") \
    .add_sauce("mayo") \
    .make_spicy() \
    .build()
# Đọc như tiếng Anh luôn!
```

## Code ví dụ siêu dễ hiểu:## Tại sao Builder Pattern ngon?

1. **Dễ đọc**: Code đọc như câu tiếng Anh
2. **Linh hoạt**: Muốn thêm/bớt gì cũng được
3. **Tránh Constructor hell**: Không cần nhớ thứ tự parameters
4. **Immutable**: Object cuối cùng có thể là immutable (không đổi được)

## Khi nào dùng Builder?

- **Object phức tạp**: Có nhiều thuộc tính optional
- **Nhiều cách tạo**: Cùng 1 class nhưng có thể tạo theo nhiều kiểu
- **Step-by-step**: Cần tạo object từng bước

## So sánh nhanh:

**Factory**: Giống đặt món - "Cho tôi 1 pizza Margherita" 
**Builder**: Giống tự làm món - "Bánh + thịt + rau + nước chấm..."

Builder cho phép customize từng detail, Factory cho result nhanh!

Vậy là 3 pattern rồi đó bro! Factory Method → Abstract Factory → Builder. Có thấy pattern (😏) không? Tất cả đều về **tạo object**, chỉ khác cách thức thôi! 🔥