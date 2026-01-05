# Prototype Pattern - Copy nhân vật game

import copy

class GameCharacter:
    """Nhân vật game có thể clone"""
    
    def __init__(self, name, level=1, hp=100, equipment=None):
        self.name = name
        self.level = level
        self.hp = hp
        self.equipment = equipment or []
        self.skills = []
    
    def add_skill(self, skill):
        """Thêm skill cho nhân vật"""
        self.skills.append(skill)
        print(f"✅ {self.name} đã học skill: {skill}")
    
    def add_equipment(self, item):
        """Thêm trang bị"""
        self.equipment.append(item)
        print(f"✅ {self.name} đã trang bị: {item}")
    
    def level_up(self, levels=1):
        """Tăng level"""
        self.level += levels
        self.hp += levels * 20
        print(f"🆙 {self.name} lên level {self.level}! HP: {self.hp}")
    
    def clone(self):
        """Clone nhân vật - đây là method Prototype chính"""
        # Deep copy để không bị share reference
        cloned = copy.deepcopy(self)
        cloned.name = f"{self.name}_Copy"
        print(f"📄 Đã clone {self.name} → {cloned.name}")
        return cloned
    
    def show_stats(self):
        """Hiển thị thông tin nhân vật"""
        print(f"\n👤 {self.name}")
        print(f"   Level: {self.level}")
        print(f"   HP: {self.hp}")
        print(f"   Equipment: {', '.join(self.equipment) if self.equipment else 'Không có'}")
        print(f"   Skills: {', '.join(self.skills) if self.skills else 'Không có'}")

# Prototype Registry - Kho lưu trữ các template
class CharacterRegistry:
    """Kho chứa các mẫu nhân vật để clone"""
    
    def __init__(self):
        self._prototypes = {}
    
    def register_prototype(self, name, prototype):
        """Đăng ký mẫu nhân vật"""
        self._prototypes[name] = prototype
        print(f"📋 Đã lưu mẫu nhân vật: {name}")
    
    def create_character(self, prototype_name, new_name):
        """Tạo nhân vật mới từ mẫu có sẵn"""
        if prototype_name not in self._prototypes:
            print(f"❌ Không tìm thấy mẫu: {prototype_name}")
            return None
        
        # Clone từ mẫu
        character = self._prototypes[prototype_name].clone()
        character.name = new_name
        print(f"🎮 Đã tạo nhân vật {new_name} từ mẫu {prototype_name}")
        return character
    
    def list_prototypes(self):
        """Liệt kê các mẫu có sẵn"""
        print(f"📋 Các mẫu nhân vật: {list(self._prototypes.keys())}")

# Demo sử dụng Prototype Pattern
print("=== GAME CHARACTER CREATOR ===\n")

# 1. Tạo nhân vật mẫu (prototype)
print("1. Tạo nhân vật mẫu:")
warrior_template = GameCharacter("Chiến Binh Mẫu", level=10, hp=200)
warrior_template.add_skill("Chém mạnh")
warrior_template.add_skill("Phòng thủ")
warrior_template.add_equipment("Kiếm thép")
warrior_template.add_equipment("Khiên sắt")
warrior_template.show_stats()

mage_template = GameCharacter("Pháp Sư Mẫu", level=8, hp=150)
mage_template.add_skill("Cầu lửa")
mage_template.add_skill("Heal")
mage_template.add_equipment("Gậy ma thuật")
mage_template.add_equipment("Áo choàng")
mage_template.show_stats()

# 2. Đăng ký vào registry
print("\n2. Đăng ký mẫu nhân vật:")
registry = CharacterRegistry()
registry.register_prototype("warrior", warrior_template)
registry.register_prototype("mage", mage_template)
registry.list_prototypes()

# 3. Tạo nhân vật mới từ mẫu (clone)
print("\n3. Tạo nhân vật mới từ mẫu:")
player1 = registry.create_character("warrior", "Hoàng Anh")
player1.show_stats()

player2 = registry.create_character("mage", "Minh Châu")  
player2.show_stats()

# 4. Modify clone (không ảnh hưởng đến prototype)
print("\n4. Chỉnh sửa nhân vật clone:")
player1.level_up(5)
player1.add_skill("Berserk")
player1.show_stats()

print("\n5. Kiểm tra prototype gốc không đổi:")
warrior_template.show_stats()

# 6. Clone trực tiếp từ character
print("\n6. Clone trực tiếp:")
player3 = player1.clone()
player3.name = "Hùng Vương"
player3.show_stats()

print("\n🎊 Prototype Pattern giúp tạo nhân vật nhanh chóng!")
print("💡 Tip: Hữu ích khi tạo object tốn nhiều resource hoặc có setup phức tạp!")