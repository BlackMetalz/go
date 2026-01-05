# How to learn structural patterns for noob/code level monkey like me

Để tiếp thu 7 mẫu thiết kế cấu trúc (Structural Patterns) một cách hợp lý, đặc biệt dành cho người mới bắt đầu hoặc ở mức "code level monkey" (người mới, chủ yếu tập trung vào viết code cơ bản), bạn cần một lộ trình học tập đơn giản, thực tiễn và dễ hiểu. Các mẫu thiết kế cấu trúc (Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy) tập trung vào việc tổ chức và quản lý mối quan hệ giữa các đối tượng để tạo ra hệ thống linh hoạt và dễ bảo trì. Dưới đây là hướng dẫn chi tiết:

---

### 1. Hiểu cơ bản về mẫu thiết kế (Design Patterns)
   - **Mục tiêu**: Nắm rõ tại sao cần các mẫu thiết kế cấu trúc và vai trò của chúng.
   - **Hành động**:
     - Đọc khái niệm cơ bản về design patterns. Tìm hiểu rằng Structural Patterns giúp giải quyết các vấn đề về cách tổ chức các lớp/đối tượng để dễ mở rộng, bảo trì.
     - Tài liệu gợi ý:
       - Sách: *Head First Design Patterns* (phù hợp cho người mới, giải thích dễ hiểu, nhiều hình minh họa).
       - Bài viết đơn giản trên các trang như Viblo, Dev.to hoặc Medium (tìm từ khóa "Structural Design Patterns").
     - Xem video ngắn (5-10 phút) trên YouTube về "What are Design Patterns?" để hiểu bối cảnh.
   - **Lưu ý**: Ở giai đoạn này, không cần đi sâu vào từng pattern, chỉ cần hiểu chúng là công cụ để giải quyết vấn đề.

---

### 2. Học từng mẫu thiết kế theo thứ tự dễ đến khó
   Để dễ tiếp thu, hãy học các mẫu theo mức độ đơn giản và áp dụng thực tế. Dưới đây là thứ tự gợi ý:

   #### a. **Facade Pattern** (Dễ nhất)
   - **Tại sao học đầu tiên?**: Facade đơn giản, giống như một "lớp vỏ" che giấu sự phức tạp của hệ thống bên dưới. Nó dễ hình dung với người mới.
   - **Cách học**:
     - Hiểu khái niệm: Facade cung cấp một giao diện đơn giản để tương tác với một hệ thống phức tạp.
     - Ví dụ thực tế: Một hệ thống đặt vé máy bay có nhiều bước (kiểm tra chuyến bay, thanh toán, gửi email xác nhận). Facade sẽ gói gọn các bước này thành một hàm `bookTicket()`.
     - **Thực hành**:
       - Viết một chương trình nhỏ (dùng ngôn ngữ bạn quen, ví dụ Java, Python, JS) mô phỏng một hệ thống phức tạp (như hệ thống đặt hàng online) và tạo một lớp Facade để đơn giản hóa việc gọi các chức năng.
       - Ví dụ Python:
         ```python
         class OrderSystem:
             def checkInventory(self): print("Checking inventory...")
             def processPayment(self): print("Processing payment...")
             def sendConfirmation(self): print("Sending confirmation...")

         class OrderFacade:
             def __init__(self): self.order_system = OrderSystem()
             def placeOrder(self):
                 self.order_system.checkInventory()
                 self.order_system.processPayment()
                 self.order_system.sendConfirmation()

         # Sử dụng
         facade = OrderFacade()
         facade.placeOrder()
         ```

   #### b. **Adapter Pattern**
   - **Tại sao?**: Adapter dễ hiểu, giống như một "bộ chuyển đổi" trong đời thực (như cáp USB-C sang USB-A).
   - **Cách học**:
     - Hiểu khái niệm: Adapter giúp hai giao diện không tương thích làm việc với nhau.
     - Ví dụ thực tế: Một ứng dụng cũ chỉ chấp nhận định dạng JSON, nhưng hệ thống mới trả về XML. Adapter chuyển đổi XML sang JSON.
     - **Thực hành**:
       - Tạo một chương trình mô phỏng hai hệ thống không tương thích (ví dụ: một lớp đọc file CSV và một lớp chỉ chấp nhận JSON). Viết Adapter để kết nối chúng.
       - Ví dụ Python:
         ```python
         class OldSystem:
             def getJson(self): return {"name": "Monkey", "level": "Beginner"}

         class NewSystem:
             def getXml(self): return "<data><name>Monkey</name><level>Beginner</level></data>"

         class XmlToJsonAdapter:
             def __init__(self, new_system): self.new_system = new_system
             def getJson(self):
                 xml_data = self.new_system.getXml()
                 # Giả lập chuyển đổi XML sang JSON
                 return {"name": "Monkey", "level": "Beginner"}

         # Sử dụng
         new_system = NewSystem()
         adapter = XmlToJsonAdapter(new_system)
         print(adapter.getJson())
         ```

   #### c. **Decorator Pattern**
   - **Tại sao?**: Decorator giống như việc thêm tính năng mà không sửa đổi code gốc, dễ hình dung qua các ví dụ thực tế.
   - **Cách học**:
     - Hiểu khái niệm: Decorator bọc một đối tượng để thêm hành vi mà không thay đổi cấu trúc gốc.
     - Ví dụ thực tế: Một quán cà phê có cà phê cơ bản, bạn có thể thêm sữa, đường, caramel (mỗi thứ là một decorator).
     - **Thực hành**:
       - Viết chương trình mô phỏng một hệ thống cà phê, thêm các decorator như sữa, đường.
       - Ví dụ Python:
         ```python
         class Coffee:
             def cost(self): return 5
             def description(self): return "Basic Coffee"

         class MilkDecorator:
             def __init__(self, coffee): self.coffee = coffee
             def cost(self): return self.coffee.cost() + 2
             def description(self): return self.coffee.description() + ", Milk"

         # Sử dụng
         coffee = Coffee()
         milk_coffee = MilkDecorator(coffee)
         print(milk_coffee.description(), milk_coffee.cost())  # Basic Coffee, Milk 7
         ```

   #### d. **Composite Pattern**
   - **Tại sao?**: Composite giúp quản lý cấu trúc cây (tree structure), như thư mục và file trong hệ thống tập tin.
   - **Cách học**:
     - Hiểu khái niệm: Composite cho phép đối xử với các đối tượng đơn lẻ và nhóm đối tượng theo cách thống nhất.
     - Ví dụ thực tế: Một thư mục (folder) chứa các file và thư mục con, tất cả đều có thể gọi hàm `showDetails()`.
     - **Thực hành**:
       - Tạo một chương trình mô phỏng hệ thống file, với folder và file đều có thể hiển thị thông tin.
       - Ví dụ Python:
         ```python
         class Component:
             def showDetails(self): pass

         class File(Component):
             def __init__(self, name): self.name = name
             def showDetails(self): print(f"File: {self.name}")

         class Folder(Component):
             def __init__(self, name): self.name = name; self.children = []
             def add(self, component): self.children.append(component)
             def showDetails(self):
                 print(f"Folder: {self.name}")
                 for child in self.children:
                     child.showDetails()

         # Sử dụng
         folder = Folder("Documents")
         folder.add(File("note.txt"))
         folder.add(File("photo.jpg"))
         folder.showDetails()
         ```

   #### e. **Proxy Pattern**
   - **Tại sao?**: Proxy giống như một "người trung gian" kiểm soát truy cập, dễ liên hệ với thực tế.
   - **Cách học**:
     - Hiểu khái niệm: Proxy đứng giữa client và đối tượng thực để kiểm soát truy cập, như lazy loading hoặc bảo mật.
     - Ví dụ thực tế: Một proxy kiểm tra quyền truy cập trước khi cho phép tải hình ảnh từ server.
     - **Thực hành**:
       - Viết chương trình mô phỏng proxy kiểm tra quyền trước khi truy cập tài nguyên.
       - Ví dụ Python:
         ```python
         class Image:
             def display(self): print("Displaying image")

         class ImageProxy:
             def __init__(self): self.image = None
             def display(self):
                 if self.image is None:
                     print("Loading image...")
                     self.image = Image()
                 self.image.display()

         # Sử dụng
         proxy = ImageProxy()
         proxy.display()  # Loading image... Displaying image
         ```

   #### f. **Bridge Pattern**
   - **Tại sao?**: Bridge tách biệt giao diện và triển khai, hơi phức tạp hơn nhưng vẫn có thể hiểu qua ví dụ thực tế.
   - **Cách học**:
     - Hiểu khái niệm: Bridge tách logic chính (abstraction) khỏi cách triển khai (implementation).
     - Ví dụ thực tế: Một ứng dụng vẽ hình (hình tròn, hình vuông) với các công cụ vẽ khác nhau (bút chì, cọ vẽ).
     - **Thực hành**:
       - Viết chương trình mô phỏng vẽ hình với các công cụ khác nhau.
       - Ví dụ Python:
         ```python
         class Renderer:
             def render_circle(self): pass

         class PencilRenderer(Renderer):
             def render_circle(self): print("Drawing circle with pencil")

         class BrushRenderer(Renderer):
             def render_circle(self): print("Drawing circle with brush")

         class Shape:
             def __init__(self, renderer): self.renderer = renderer
             def draw(self): pass

         class Circle(Shape):
             def draw(self): self.renderer.render_circle()

         # Sử dụng
         circle = Circle(PencilRenderer())
         circle.draw()  # Drawing circle with pencil
         ```

   #### g. **Flyweight Pattern** (Khó nhất)
   - **Tại sao học cuối?**: Flyweight phức tạp hơn, liên quan đến tối ưu hóa bộ nhớ, phù hợp khi bạn đã quen với các pattern khác.
   - **Cách học**:
     - Hiểu khái niệm: Flyweight chia sẻ các đối tượng nhỏ để tiết kiệm tài nguyên.
     - Ví dụ thực tế: Một game có hàng nghìn cây, nhưng tất cả cây cùng loại chia sẻ cùng một texture.
     - **Thực hành**:
       - Viết chương trình mô phỏng một rừng cây, chia sẻ texture giữa các cây cùng loại.
       - Ví dụ Python:
         ```python
         class TreeType:
             def __init__(self, texture): self.texture = texture
             def draw(self, x, y): print(f"Drawing tree with {self.texture} at ({x}, {y})")

         class TreeFactory:
             tree_types = {}
             @staticmethod
             def get_tree_type(texture):
                 if texture not in TreeFactory.tree_types:
                     TreeFactory.tree_types[texture] = TreeType(texture)
                 return TreeFactory.tree_types[texture]

         class Tree:
             def __init__(self, x, y, texture):
                 self.x = x
                 self.y = y
                 self.type = TreeFactory.get_tree_type(texture)
             def draw(self): self.type.draw(self.x, self.y)

         # Sử dụng
         forest = [Tree(1, 1, "Pine"), Tree(2, 2, "Pine"), Tree(3, 3, "Oak")]
         for tree in forest:
             tree.draw()
         ```

---

### 3. Phương pháp học hiệu quả
   - **Học qua ví dụ thực tế**: Mỗi pattern, hãy liên hệ với một tình huống thực tế (như quán cà phê, hệ thống file, game) để dễ hình dung.
   - **Thực hành là chính**: Viết code cho từng pattern, bắt đầu bằng các ví dụ nhỏ. Dùng ngôn ngữ bạn quen thuộc (Python, Java, JS đều tốt).
   - **Học từng pattern một**: Dành 1-2 ngày cho mỗi pattern, thực hành xong mới chuyển sang pattern tiếp theo.
   - **So sánh các pattern**: Sau khi học xong, thử so sánh chúng (ví dụ: Adapter vs Bridge, Decorator vs Proxy) để hiểu sự khác biệt.
   - **Dùng tài liệu trực quan**:
     - Xem sơ đồ UML của từng pattern (có thể tìm trên Google hoặc sách *Head First Design Patterns*).
     - Xem video minh họa trên YouTube (tìm kênh như "Derek Banas" hoặc "Christopher Okhravi").
   - **Áp dụng vào dự án nhỏ**: Tạo một dự án đơn giản (như game, ứng dụng quản lý) và cố gắng áp dụng ít nhất 2-3 pattern vào đó.

---

### 4. Lộ trình học trong 2-3 tuần
   - **Tuần 1**:
     - Ngày 1-2: Hiểu khái niệm Design Patterns + Facade Pattern.
     - Ngày 3-4: Adapter Pattern + thực hành.
     - Ngày 5-6: Decorator Pattern + thực hành.
   - **Tuần 2**:
     - Ngày 1-2: Composite Pattern + thực hành.
     - Ngày 3-4: Proxy Pattern + thực hành.
     - Ngày 5-6: Bridge Pattern + thực hành.
   - **Tuần 3**:
     - Ngày 1-2: Flyweight Pattern + thực hành.
     - Ngày 3-4: Ôn tập, so sánh các pattern.
     - Ngày 5-6: Áp dụng 2-3 pattern vào một dự án nhỏ.

---

### 5. Lưu ý cho "code level monkey"
   - **Đừng sợ lý thuyết**: Chỉ cần hiểu khái niệm cơ bản, tập trung vào code và ví dụ.
   - **Code càng đơn giản càng tốt**: Không cần viết chương trình phức tạp, chỉ cần đúng ý tưởng pattern.
   - **Học qua lỗi**: Nếu code không chạy, thử debug hoặc tìm ví dụ tương tự trên GitHub.
   - **Hỏi cộng đồng**: Nếu gặp khó, đăng câu hỏi lên các diễn đàn như Stack Overflow, Reddit, hoặc nhóm lập trình trên X.

---

### 6. Tài nguyên bổ sung
   - **Sách**: *Head First Design Patterns* (Eric Freeman), *Design Patterns: Elements of Reusable Object-Oriented Software* (Gang of Four, nhưng khó hơn).
   - **Website**: Refactoring.Guru (giải thích chi tiết, có hình minh họa và code mẫu).
   - **Video**: Kênh YouTube như "Derek Banas", "Christopher Okhravi".
   - **Thực hành**: Tìm bài tập trên LeetCode hoặc HackerRank liên quan đến OOP để áp dụng pattern.

---

### 7. Kiểm tra tiến độ
   - Sau mỗi pattern, tự hỏi: “Mình có thể giải thích pattern này cho người khác không?” Nếu chưa, xem lại ví dụ và code thêm.
   - Cuối lộ trình, thử viết một bài blog hoặc giải thích ngắn trên X về cách bạn hiểu các pattern (giúp củng cố kiến thức).

---

Chúc bạn học tốt! Nếu cần giải thích chi tiết hơn về bất kỳ pattern nào hoặc ví dụ cụ thể, cứ hỏi mình nhé!