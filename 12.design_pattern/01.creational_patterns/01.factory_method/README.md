# This shit is hard to understand :(
https://refactoring.guru/design-patterns/factory-method

# Better to learn in mother language xD

Haha đọc tiếng Anh mà choáng váng à bro! Để anh giải thích Factory Method pattern bằng tiếng Việt cho dễ hiểu nhé:

## Factory Method là gì?
Nói đơn giản, Factory Method giống như một "xưởng sản xuất" có thể tạo ra nhiều loại sản phẩm khác nhau tùy theo yêu cầu.

## Ví dụ thực tế
Tưởng tượng bro mở một cửa hàng pizza:

```python
# Thay vì viết code cứng như này:
if pizza_type == "margherita":
    pizza = MargheritaPizza()
elif pizza_type == "pepperoni":
    pizza = PepperoniPizza()
elif pizza_type == "hawaiian":
    pizza = HawaiianPizza()

# Ta dùng Factory Method:
class PizzaFactory:
    def create_pizza(self, pizza_type):
        if pizza_type == "margherita":
            return MargheritaPizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        elif pizza_type == "hawaiian":
            return HawaiianPizza()
        else:
            raise ValueError("Không có loại pizza này!")

# Sử dụng:
factory = PizzaFactory()
pizza = factory.create_pizza("margherita")
```

## Tại sao dùng Factory Method?

1. **Dễ mở rộng**: Muốn thêm pizza mới? Chỉ cần thêm vào factory, không phải sửa code cũ
2. **Tập trung logic**: Tất cả việc tạo object đều ở một chỗ
3. **Giảm coupling**: Code client không cần biết cách tạo object cụ thể

## Những điểm cần nhớ:

1. **Factory Method ẩn cách tạo object** - Client chỉ cần gọi method, không cần biết bên trong làm gì

2. **Dễ test** - Mock factory dễ hơn mock từng class riêng lẻ

3. **Single Responsibility** - Mỗi class chỉ lo một việc: tạo object của mình

4. **Open/Closed Principle** - Muốn thêm loại mới chỉ cần extend, không modify code cũ

Bây giờ hiểu rồi chứ bro? Factory Method giúp code gọn gàng, dễ maintain và dễ mở rộng. Như kiểu có một "thợ làm" chuyên nghiệp, cần gì cứ order, còn cách làm thì để thợ lo! 😄