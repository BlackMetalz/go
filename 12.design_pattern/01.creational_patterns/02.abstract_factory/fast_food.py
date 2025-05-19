# Abstract Factory Pattern - Chuỗi đồ ăn nhanh

# Sản phẩm abstract
class Burger:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"Đang ăn {self.name} 🍔"

class Drink:
    def __init__(self, name):
        self.name = name
    
    def drink(self):
        return f"Đang uống {self.name} 🥤"

# Sản phẩm cụ thể - McDonald's style
class McBurger(Burger):
    def __init__(self):
        super().__init__("Big Mac")

class McCoke(Drink):
    def __init__(self):
        super().__init__("Coca Cola")

# Sản phẩm cụ thể - KFC style  
class KFCBurger(Burger):
    def __init__(self):
        super().__init__("Zinger Burger")

class KFCDrink(Drink):
    def __init__(self):
        super().__init__("Pepsi")

# Abstract Factory
class FastFoodFactory:
    def create_burger(self):
        pass
    
    def create_drink(self):
        pass

# Concrete Factory - McDonald's
class McdonaldsFactory(FastFoodFactory):
    def create_burger(self):
        return McBurger()
    
    def create_drink(self):
        return McCoke()

# Concrete Factory - KFC
class KFCFactory(FastFoodFactory):
    def create_burger(self):
        return KFCBurger()
    
    def create_drink(self):
        return KFCDrink()

# Client code - Khách hàng order
def order_combo(factory):
    """Khách hàng order combo từ factory"""
    burger = factory.create_burger()
    drink = factory.create_drink()
    
    print(f"🍽️ Combo của bạn:")
    print(f"   - {burger.eat()}")
    print(f"   - {drink.drink()}")
    print("   Chúc ngon miệng! 😋\n")

# Sử dụng
print("=== CHUỖI ĐỒ ĂN NHANH ===\n")

print("Khách 1 đến McDonald's:")
mcdonalds = McdonaldsFactory()
order_combo(mcdonalds)

print("Khách 2 đến KFC:")
kfc = KFCFactory()
order_combo(kfc)

# Bonus: Khách hàng chọn cửa hàng
print("Khách 3 chọn cửa hàng:")
store_choice = "mcdonalds"  # Hoặc "kfc"

if store_choice == "mcdonalds":
    factory = McdonaldsFactory()
    print("🔴 Bạn đã chọn McDonald's")
elif store_choice == "kfc":
    factory = KFCFactory()
    print("🔴 Bạn đã chọn KFC")

order_combo(factory)