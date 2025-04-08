import json
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

# Kết nối MongoDB
client = MongoClient("mongodb+srv://minhquan13092003:0392827738Mquan@ai.83vsk.mongodb.net/")
db = client["chatbot_db"]
collection = db["conversations"]

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Đọc file data.json
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Duyệt qua từng mục trong dữ liệu
for item in data:
    try:
        text = item["question"]  # Lấy câu hỏi
        vector = model.encode(text).tolist()  # Mã hóa câu hỏi thành vector

        # Lưu response_j (phản hồi tích cực)
        if "response_j" in item:
            collection.insert_one({
                "text": text,
                "response": item["response_j"],
                "type": "supportive",  # Hoặc bất kỳ tên nào bạn muốn
                "vector": vector
            })
        
        # Lưu response_k (phản hồi tiêu cực)
        if "response_k" in item:
            collection.insert_one({
                "text": text,
                "response": item["response_k"],
                "type": "harsh",  # Hoặc bất kỳ tên nào bạn muốn
                "vector": vector
            })
        
        print(f"Đã lưu câu hỏi: {text} với vector.")

    except Exception as e:
        print(f"Lỗi khi xử lý item: {item}. Lỗi: {e}")

print("✅ Dữ liệu đã được mã hóa và lưu vào MongoDB thành công.")
