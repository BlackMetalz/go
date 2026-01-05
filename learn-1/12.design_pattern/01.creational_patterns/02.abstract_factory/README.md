# Ref:
- https://refactoring.guru/design-patterns/abstract-factory

# Explain in mother language
Haha okok, Abstract Factory nghe fancy vậy thôi chứ thực ra dễ hiểu lắm bro!

## Abstract Factory là gì?
Nếu Factory Method tạo ra 1 loại sản phẩm, thì Abstract Factory tạo ra **cả gia đình sản phẩm** có liên quan với nhau.

## Ví dụ siêu đơn giản: Làm UI cho app

Tưởng tượng bro làm app có thể chạy trên nhiều hệ điều hành. Mỗi hệ điều hành có style UI khác nhau:

```python
# Thay vì viết rối rắm như này:
if os_type == "windows":
    button = WindowsButton()
    checkbox = WindowsCheckbox()
elif os_type == "mac":
    button = MacButton()
    checkbox = MacCheckbox()

# Ta dùng Abstract Factory:
class WindowsFactory:
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory:
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()

# Sử dụng:
if os_type == "windows":
    factory = WindowsFactory()
else:
    factory = MacFactory()

button = factory.create_button()
checkbox = factory.create_checkbox()
```

## So sánh với Factory Method:

**Factory Method**: 
- Tạo 1 sản phẩm
- VD: `PizzaFactory.create_pizza("margherita")`

**Abstract Factory**:
- Tạo cả gia đình sản phẩm liên quan
- VD: `McdonaldsFactory` tạo cả burger + drink theo style McDonald's

## Khi nào dùng Abstract Factory?

1. **Khi có nhiều sản phẩm liên quan**: Burger + Drink, Button + Checkbox, Car + Engine
2. **Khi muốn đảm bảo consistency**: Tất cả sản phẩm cùng 1 style/brand
3. **Khi dễ thêm brand/style mới**: Thêm Burger King chỉ cần tạo `BurgerKingFactory`

## Ưu điểm:
- **Đồng nhất**: Tất cả sản phẩm từ 1 factory đều cùng style
- **Dễ thay đổi**: Muốn đổi từ McDonald's sang KFC? Chỉ cần đổi factory
- **Dễ mở rộng**: Thêm brand mới không cần sửa code cũ

Nói tóm lại: Abstract Factory giống như **"chọn thương hiệu"** - chọn McDonald's thì được toàn bộ combo McDonald's, chọn KFC thì được toàn bộ combo KFC. Đảm bảo không bị lẫn burger McDonald's với drink KFC! 😄

Hiểu chưa bro?