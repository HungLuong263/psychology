from datasets import load_dataset
import json

# 🟢 Chọn dataset để tải
dataset_names = [
    "jkhedri/psychology-dataset",
    "Kedreamix/psychology-10k-Deepseek-R1-zh",
    "samhog/psychology-6k"
]

# 🟢 Gộp tất cả dữ liệu từ các dataset
all_data = []
for name in dataset_names:
    dataset = load_dataset(name)
    all_data.extend([dict(row) for row in dataset["train"]])  # Chuyển đổi thành dict

# 🟢 Lưu vào file JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=4)

print("✅ Dữ liệu đã được chuyển đổi và lưu thành công!")
print(all_data[:3])  # In thử 3 dòng đầu tiên


