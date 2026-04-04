import re
import os
import glob

def clean_timestamp(text):
    return re.sub(r'\d{1,2}:\d{2}', '', text)

# カレントディレクトリの.txt取得
txt_files = glob.glob("*.txt")

# 自分が生成したファイルを除外（(c)付き）
txt_files = [f for f in txt_files if "(c)" not in f]

if len(txt_files) == 0:
    print("No txt file found.")
    exit()

if len(txt_files) > 1:
    print("Multiple txt files found:", txt_files)
    exit()

input_path = txt_files[0]

# 出力ファイル名生成
base, ext = os.path.splitext(input_path)
output_path = f"{base}(c){ext}"

# 読み込み
with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

# 処理
cleaned = clean_timestamp(text)

# 書き込み
with open(output_path, "w", encoding="utf-8") as f:
    f.write(cleaned)

print(f"Processed: {input_path} -> {output_path}")