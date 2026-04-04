import re
import sys
import os

def clean_timestamp(text):
    # タイムスタンプ削除（例: 1:23, 12:34）
    text = re.sub(r'\d{1,2}:\d{2}', '', text)
    
    # スペースとタブのみ整形（改行は維持）
    text = re.sub(r'[ \t]+', ' ', text)
    
    return text.strip()

if __name__ == "__main__":
    # 引数チェック
    if len(sys.argv) != 3:
        print("Usage: python clean_timestamp.py <input_path> <output_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # 入力ファイル存在チェック
    if not os.path.exists(input_path):
        print(f"Error: Input file not found -> {input_path}")
        sys.exit(1)

    # 読み込み
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 処理
    cleaned = clean_timestamp(text)

    # 出力ディレクトリがなければ作成
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    # 書き込み
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print(f"Cleaned file saved to: {output_path}")