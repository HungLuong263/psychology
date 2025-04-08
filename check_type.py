from datasets import load_dataset

# Thay "dataset_name" bằng tên dataset bạn đã tải từ Hugging Face
dataset = load_dataset("Kedreamix/psychology-10k-Deepseek-R1-zh")
dataset = load_dataset("jkhedri/psychology-dataset")

# Xem một số dòng đầu tiên
print(dataset["train"][:3])  # Nếu có nhiều tập, chọn tập train/test/validation
