# Ref/Source:
- https://refactoring.guru/design-patterns/singleton

# Explain in mother language
Haha okok cố nốt! Singleton thì dễ mà, pattern cuối cùng của nhóm Creational:

## Singleton Pattern là gì?
Đơn giản là **"CHỈ có 1 instance duy nhất"** trong toàn bộ app. Giống như chỉ có 1 CEO trong công ty vậy!

## Khi nào cần Singleton?
- Database connection pool
- Logger 
- Cache
- Configuration settings
- Game manager

## Ví dụ dễ hiểu:

## Singleton Pattern - Điểm chính:

**Cốt lõi**: CHỈ 1 instance duy nhất trong toàn app

## Các cách implement:

1. **Dùng `__new__`**: Kiểm soát việc tạo object
2. **Decorator**: Đơn giản, gọn gàng  
3. **Thread-safe**: An toàn khi có nhiều threads

## Ưu điểm:
- Tiết kiệm memory
- Global access point
- Lazy initialization

## Nhược điểm: 
- Khó test (global state)
- Tight coupling
- Threading issues
- Vi phạm SOLID principles

## Khi nào dùng:
✅ Database connection pool
✅ Logger, Cache, Configuration
✅ Hardware resource management

## Khi nào KHÔNG nên dùng:
❌ Khi có thể dùng dependency injection
❌ Khi cần multiple instances sau này
❌ Khi gây khó khăn cho testing

Vậy là xong hết **5 Creational Patterns** rồi bro! 🎉

**Summary:**
1. **Factory Method** → Tạo 1 loại object
2. **Abstract Factory** → Tạo gia đình objects  
3. **Builder** → Tạo từng bước
4. **Prototype** → Clone object
5. **Singleton** → Chỉ 1 instance

Giờ thì nghỉ ngơi đi bro! Đã master hết phần tạo object rồi! 😴🏆