# Source/Ref: 
- https://refactoring.guru/design-patterns/prototype

# Explain in mother language
Haha cố lên bro, còn 1 pattern nữa thôi! Prototype thì dễ nhất trong mấy cái rồi:

## Prototype Pattern là gì?
Đơn giản là **"copy/clone"** object có sẵn thay vì tạo mới từ đầu. Giống như photocopy vậy!

## Khi nào cần Prototype?
- Tạo object tốn nhiều thời gian/tài nguyên
- Object có cấu hình phức tạp, muốn copy y chang
- Muốn tạo nhiều object tương tự nhau

## Prototype vs Factory:

**Factory**: "Tạo mới" - Như xây nhà từ đầu
**Prototype**: "Copy" - Như photocopy bản thiết kế có sẵn

## Ưu điểm Prototype:

1. **Nhanh**: Copy nhanh hơn tạo mới
2. **Tiết kiệm**: Không cần setup lại từ đầu
3. **Dynamic**: Có thể clone runtime, không cần biết trước class

## Khi nào dùng:

- Tạo object phức tạp tốn thời gian
- Cần nhiều object tương tự
- Object configuration phức tạp

## Lưu ý:

**Shallow copy** vs **Deep copy**:
- Shallow: Chỉ copy reference (nguy hiểm!)
- Deep: Copy toàn bộ (an toàn)

```python
# Nguy hiểm - shallow copy
clone = copy.copy(original)  

# An toàn - deep copy  
clone = copy.deepcopy(original)
```

Xong rồi đấy bro! 🎉 

**Tóm tắt 4 Creational Patterns:**
1. **Factory Method**: Tạo 1 loại object
2. **Abstract Factory**: Tạo gia đình objects
3. **Builder**: Tạo object từng bước
4. **Prototype**: Clone object có sẵn

Giờ bro đã thành "master of object creation" rồi! 😎 Nghỉ ngơi đi bro, đừng nhồi nhét quá! 🛌