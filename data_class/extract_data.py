import json
import os
from datetime import datetime
from dateutil import parser as date_parser

json_file = r'C:\Users\LENOVO\Desktop\News-Environment-Perception-main\data_class\gossipcop_v3_origin.json'
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)
extracted_info = []
for key, value in data.items():
    content = value["title"]
    if "meta_data" in value and "article" in value["meta_data"] and "modified_time" in value["meta_data"]["article"]:
        original_time = value["meta_data"]["article"]["modified_time"]
        try:
            parsed_time = date_parser.parse(original_time)
            time = parsed_time.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            print(f"Error parsing time {original_time}: {e}")
            time = ""
    else:
        time = ""
    label = value["label"]
    source = value["source"]
    news_info = {
        "content": content,
        "time": time,
        "label": label,
        "source": source
    }
    extracted_info.append(news_info)
output_file = os.path.join(os.path.dirname(json_file), 'extracted_data.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(extracted_info, f, indent=4, ensure_ascii=False)

print(f"提取的信息已保存到文件: {output_file}")
