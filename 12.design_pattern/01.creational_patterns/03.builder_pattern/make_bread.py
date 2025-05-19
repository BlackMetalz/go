# Builder Pattern - Làm bánh mì

class BanhMi:
    """Sản phẩm cuối cùng - Cái bánh mì"""
    def __init__(self):
        self.bread = None
        self.meat = []
        self.vegetables = []
        self.sauces = []
        self.extras = []
    
    def __str__(self):
        ingredients = [
            f"🥖 Bánh: {self.bread}" if self.bread else "",
            f"🥩 Thịt: {', '.join(self.meat)}" if self.meat else "",
            f"🥒 Rau: {', '.join(self.vegetables)}" if self.vegetables else "",
            f"🧄 Nước chấm: {', '.join(self.sauces)}" if self.sauces else "",
            f"✨ Thêm: {', '.join(self.extras)}" if self.extras else ""
        ]
        
        result = "🥖 BÁNH MÌ CỦA BẠN:\n"
        for ingredient in ingredients:
            if ingredient:
                result += f"   {ingredient}\n"
        
        return result

class BanhMiBuilder:
    """Builder để làm bánh mì từng bước"""
    
    def __init__(self):
        self.banh_mi = BanhMi()
    
    def add_bread(self, bread_type):
        """Thêm loại bánh"""
        self.banh_mi.bread = bread_type
        print(f"✅ Đã chọn bánh {bread_type}")
        return self  # Return self để chain methods
    
    def add_meat(self, meat_type):
        """Thêm thịt"""
        self.banh_mi.meat.append(meat_type)
        print(f"✅ Đã thêm {meat_type}")
        return self
    
    def add_vegetable(self, vegetable):
        """Thêm rau"""
        self.banh_mi.vegetables.append(vegetable)
        print(f"✅ Đã thêm {vegetable}")
        return self
    
    def add_sauce(self, sauce):
        """Thêm nước chấm"""
        self.banh_mi.sauces.append(sauce)
        print(f"✅ Đã thêm {sauce}")
        return self
    
    def make_spicy(self):
        """Làm cay"""
        self.banh_mi.extras.append("ớt cay 🌶️")
        print("✅ Đã làm cay")
        return self
    
    def add_cheese(self):
        """Thêm phô mai"""
        self.banh_mi.extras.append("phô mai 🧀")
        print("✅ Đã thêm phô mai")
        return self
    
    def extra_crispy(self):
        """Nướng giòn"""
        self.banh_mi.extras.append("nướng giòn 🔥")
        print("✅ Đã nướng giòn")
        return self
    
    def build(self):
        """Hoàn thành bánh mì"""
        print("🎉 Bánh mì đã sẵn sàng!")
        return self.banh_mi
    
    def reset(self):
        """Reset để làm bánh mì mới"""
        self.banh_mi = BanhMi()
        return self

# Director - Người biết cách làm bánh mì chuẩn
class BanhMiDirector:
    """Biết cách làm những loại bánh mì phổ biến"""
    
    def __init__(self, builder):
        self.builder = builder
    
    def make_banh_mi_thit(self):
        """Làm bánh mì thịt cổ điển"""
        return self.builder \
            .add_bread("bánh mì Việt Nam") \
            .add_meat("thịt nướng") \
            .add_meat("chả cá") \
            .add_vegetable("dưa chuột") \
            .add_vegetable("rau ngò") \
            .add_vegetable("cà rót") \
            .add_sauce("tương ớt") \
            .build()
    
    def make_banh_mi_pate(self):
        """Làm bánh mì pate"""
        return self.builder \
            .reset() \
            .add_bread("bánh mì Pháp") \
            .add_meat("pate") \
            .add_meat("chả lụa") \
            .add_vegetable("dưa chuột") \
            .add_sauce("mayo") \
            .build()
    
    def make_banh_mi_chay(self):
        """Làm bánh mì chay"""
        return self.builder \
            .reset() \
            .add_bread("bánh mì nguyên cám") \
            .add_vegetable("nấm nướng") \
            .add_vegetable("dưa chuột") \
            .add_vegetable("cà rót") \
            .add_vegetable("rau xanh") \
            .add_sauce("tương đen") \
            .add_cheese() \
            .build()

# Sử dụng Builder Pattern
print("=== QUÁN BÁNH MÌ ===\n")

# Cách 1: Tự build từng bước
print("1. Khách tự order:")
builder = BanhMiBuilder()
my_banh_mi = builder \
    .add_bread("bánh mì Sài Gòn") \
    .add_meat("thịt nướng") \
    .add_meat("chả cá") \
    .add_vegetable("dưa leo") \
    .add_sauce("tương ớt") \
    .make_spicy() \
    .extra_crispy() \
    .build()

print(my_banh_mi)

# Cách 2: Dùng Director cho combo có sẵn
print("2. Khách order combo có sẵn:")
director = BanhMiDirector(BanhMiBuilder())

print("\n📋 Bánh mì thịt nướng:")
banh_mi_thit = director.make_banh_mi_thit()
print(banh_mi_thit)

print("📋 Bánh mì pate:")
banh_mi_pate = director.make_banh_mi_pate()
print(banh_mi_pate)

print("📋 Bánh mì chay:")
banh_mi_chay = director.make_banh_mi_chay()
print(banh_mi_chay)