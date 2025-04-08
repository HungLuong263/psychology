from sentence_transformers import SentenceTransformer
import numpy as np
from pymongo import MongoClient
from sklearn.metrics.pairwise import cosine_similarity

# Kết nối MongoDB Atlas (sửa lại URI nếu cần)
client = MongoClient("mongodb+srv://minhquan13092003:0392827738Mquan@ai.83vsk.mongodb.net/")
db = client["chatbot_db"]
collection = db["conversations"]

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Hàm tìm câu trả lời phù hợp nhất
def find_best_answer(query):
    query_vector = model.encode(query).reshape(1, -1)

    # Lấy dữ liệu đã có vector từ MongoDB
    data = list(collection.find({"vector": {"$exists": True}}))

    if not data:
        raise ValueError("❌ Không tìm thấy dữ liệu vector trong MongoDB!")

    # Lấy toàn bộ vectors từ database
    corpus_vectors = np.array([item["vector"] for item in data])

    # Tính độ tương đồng cosine
    similarities = cosine_similarity(query_vector, corpus_vectors)

    # Tìm câu có độ tương tự cao nhất
    best_match_index = np.argmax(similarities)
    best_match = data[best_match_index]
    similarity_score = similarities[0][best_match_index]

    print("Các trường trong best_match:", best_match.keys())

    return best_match["text"], best_match["response"], similarity_score

# Giao diện người dùng đơn giản
if __name__ == "__main__":
    query = input("💬 Nhập câu hỏi của bạn: ")
    question, response, similarity = find_best_answer(query)

    print("\n📌 Câu hỏi giống nhất trong hệ thống:", question)
    print("🤖 Phản hồi gợi ý:", response)
    print(f"📈 Mức độ tương đồng: {similarity:.4f}")
