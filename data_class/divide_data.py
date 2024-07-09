import json
import random

# 读取JSON文件
file_path = r'C:\Users\LENOVO\Desktop\News-Environment-Perception-main\data_class\extracted_data.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

random.shuffle(data)

total_len = len(data)
train_len = int(total_len * (3 / 5))
test_len = int(total_len * (1 / 5))
val_len = total_len - train_len - test_len

train_data = data[:train_len]
test_data = data[train_len:train_len + test_len]
val_data = data[train_len + test_len:]

base_path = r'C:\\Users\\LENOVO\\Desktop\\News-Environment-Perception-main\\data_class\\'
with open(base_path + 'train.json', 'w', encoding='utf-8') as f:
    json.dump(train_data, f, ensure_ascii=False, indent=4)

with open(base_path + 'test.json', 'w', encoding='utf-8') as f:
    json.dump(test_data, f, ensure_ascii=False, indent=4)

with open(base_path + 'val.json', 'w', encoding='utf-8') as f:
    json.dump(val_data, f, ensure_ascii=False, indent=4)

print("数据集划分完成")
