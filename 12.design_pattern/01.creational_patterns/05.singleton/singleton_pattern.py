# Singleton Pattern - Game Manager

class GameManager:
    """
    Singleton class - Chỉ có 1 game manager duy nhất
    Quản lý toàn bộ game state
    """
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        """Magic method để kiểm soát việc tạo instance"""
        if cls._instance is None:
            print("🎮 Đang khởi tạo Game Manager...")
            cls._instance = super().__new__(cls)
        else:
            print("♻️ Game Manager đã tồn tại, trả về instance cũ")
        return cls._instance
    
    def __init__(self):
        """Chỉ initialize 1 lần duy nhất"""
        if not self._initialized:
            print("✅ Khởi tạo game manager lần đầu")
            self.player_score = 0
            self.game_level = 1
            self.is_paused = False
            self.settings = {
                'sound': True,
                'music': True,
                'difficulty': 'Normal'
            }
            self._initialized = True
        else:
            print("⚠️ Game Manager đã được khởi tạo rồi")
    
    def increase_score(self, points):
        """Tăng điểm cho player"""
        self.player_score += points
        print(f"🏆 +{points} điểm! Tổng: {self.player_score}")
    
    def next_level(self):
        """Chuyển level tiếp theo"""
        self.game_level += 1
        print(f"🆙 Lên level {self.game_level}!")
    
    def pause_game(self):
        """Pause/Resume game"""
        self.is_paused = not self.is_paused
        status = "tạm dừng" if self.is_paused else "tiếp tục"
        print(f"⏸️ Game đã {status}")
    
    def change_setting(self, key, value):
        """Thay đổi setting"""
        if key in self.settings:
            self.settings[key] = value
            print(f"⚙️ Đã đổi {key} = {value}")
        else:
            print(f"❌ Setting '{key}' không tồn tại")
    
    def get_game_status(self):
        """Hiển thị trạng thái game"""
        status = "Tạm dừng" if self.is_paused else "Đang chạy"
        print(f"\n📊 TRẠNG THÁI GAME:")
        print(f"   Điểm: {self.player_score}")
        print(f"   Level: {self.game_level}")
        print(f"   Trạng thái: {status}")
        print(f"   Cài đặt: {self.settings}")


# Decorator approach - Cách khác để tạo Singleton
def singleton(cls):
    """Decorator để biến class thành Singleton"""
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    """Logger singleton sử dụng decorator"""
    
    def __init__(self):
        self.logs = []
        print("📝 Logger được khởi tạo")
    
    def log(self, message):
        """Ghi log"""
        self.logs.append(message)
        print(f"📝 LOG: {message}")
    
    def show_logs(self):
        """Hiển thị tất cả logs"""
        print(f"\n📋 Tất cả logs ({len(self.logs)} dòng):")
        for i, log in enumerate(self.logs, 1):
            print(f"   {i}. {log}")


# Thread-safe Singleton (nâng cao)
import threading

class DatabaseConnection:
    """Thread-safe Singleton for database connection"""
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Double-checked locking
                if cls._instance is None:
                    print("🔗 Tạo kết nối database...")
                    cls._instance = super().__new__(cls)
                    cls._instance.connected = True
        return cls._instance
    
    def query(self, sql):
        """Execute query"""
        if self.connected:
            print(f"🔍 Executing: {sql}")
            return f"Result of '{sql}'"
        else:
            print("❌ Database chưa kết nối")
            return None


# Demo sử dụng Singleton Pattern
print("=== SINGLETON PATTERN DEMO ===\n")

# 1. Test GameManager Singleton
print("1. Test Game Manager:")
manager1 = GameManager()
manager1.increase_score(100)
manager1.next_level()

# Tạo "instance" thứ 2 - thực ra vẫn là cái cũ
manager2 = GameManager()
manager2.increase_score(50)  # Cộng vào tổng điểm cũ

print(f"Manager1 is Manager2: {manager1 is manager2}")  # True
manager1.get_game_status()

# 2. Test Logger Singleton
print("\n2. Test Logger:")
logger1 = Logger()
logger1.log("Game started")
logger1.log("Player joined")

logger2 = Logger()  # Cùng instance
logger2.log("Level completed")

print(f"Logger1 is Logger2: {logger1 is logger2}")  # True
logger1.show_logs()

# 3. Test Database Connection
print("\n3. Test Database Connection:")
db1 = DatabaseConnection()
db1.query("SELECT * FROM users")

db2 = DatabaseConnection()
db2.query("SELECT * FROM products")

print(f"DB1 is DB2: {db1 is db2}")  # True

# 4. Kiểm tra memory address
print(f"\n🔍 Memory addresses:")
print(f"Manager1: {id(manager1)}")
print(f"Manager2: {id(manager2)}")
print(f"Logger1: {id(logger1)}")
print(f"Logger2: {id(logger2)}")

print("\n✅ Singleton Pattern đảm bảo chỉ có 1 instance duy nhất!")
print("💡 Hữu ích cho: Database, Logger, Cache, Config, Game State...")

# Lưu ý về nhược điểm
print("\n⚠️ LƯU Ý:")
print("- Khó test (global state)")
print("- Vi phạm Single Responsibility")
print("- Threading issues (cần thread-safe)")