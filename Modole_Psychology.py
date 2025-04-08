from datasets import load_dataset

# Tải dataset từ Hugging Face
dataset = load_dataset("samhog/psychology-6k")

# Xem thông tin dataset
print(dataset)
print(dataset.cache_files)

# Xem 5 dòng đầu tiên
print(dataset['blended_skill_talk'].to_pandas().head())
