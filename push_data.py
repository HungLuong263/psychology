from pymongo import MongoClient

# Thay YOUR_CONNECTION_STRING bằng chuỗi kết nối của bạn
MONGO_URI = "mongodb+srv://minhquan13092003:0392827738Mquan@ai.83vsk.mongodb.net/"

# Kết nối đến MongoDB
client = MongoClient(MONGO_URI)

# Chọn database (nếu chưa có thì MongoDB sẽ tự tạo)
db = client["AI_Psychology"]

# Chọn collection để lưu dữ liệu (nếu chưa có thì sẽ tự tạo)
collection = db["conversations"]

print("✅ Kết nối thành công với MongoDB!")
