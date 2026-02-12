"""
Data preparation module
データ前処理モジュール
"""

from pathlib import Path
from datetime import datetime
import pandas as pd


# =========================
# Column rename mapping
# 日本語列 → 英語列 変換マップ
# =========================
RENAME_MAP = {
    "種類": "property_type",
    "価格情報区分": "price_category",
    "市区町村コード": "city_code",
    "都道府県名": "prefecture",
    "市区町村名": "city",
    "地区名": "district",
    "最寄駅：名称": "nearest_station",
    "最寄駅：距離（分）": "station_minutes",
    "取引価格（総額）": "price",
    "間取り": "layout",
    "面積（㎡）": "area_sqm",
    "建築年": "year_built",
    "建物の構造": "structure",
    "用途": "usage",
    "今後の利用目的": "future_use",
    "都市計画": "urban_planning",
    "建ぺい率（％）": "building_coverage_ratio",
    "容積率（％）": "floor_area_ratio",
    "取引時期": "transaction_period",
    "改装": "renovation",
    "取引の事情等": "transaction_note",
}


# =========================
# Robust CSV loader
# 文字コード自動判定読み込み
# =========================
def read_csv_robust(path: str | Path) -> pd.DataFrame:
    """
    Try UTF-8 first, fallback to cp932
    UTF-8で読み込み、失敗したらcp932で再試行
    """
    path = Path(path)
    try:
        return pd.read_csv(path, encoding="utf-8-sig")
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="cp932")


# =========================
# Rename columns if Japanese exists
# 日本語列が存在する場合のみ英語に変換
# =========================
def rename_columns_if_needed(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.strip()

    jp_cols = set(RENAME_MAP.keys())
    if any(c in jp_cols for c in df.columns):
        df = df.rename(columns=RENAME_MAP)

    return df


# =========================
# Convert year_built and create building_age
# 建築年の数値化と築年数生成
# =========================
def add_year_built_and_age(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "year_built" not in df.columns:
        return df

    # Extract 4-digit year (e.g., "2000年")
    # "2000年" のような文字列から4桁年を抽出
    extracted = (
        df["year_built"]
        .astype(str)
        .str.replace(r"\s+", "", regex=True)
        .str.extract(r"(\d{4})")[0]
    )

    df["year_built"] = pd.to_numeric(extracted, errors="coerce")

    current_year = datetime.now().year
    df["building_age"] = current_year - df["year_built"]

    return df


# =========================
# Convert numeric columns safely
# 数値列を安全に変換（不正値はNaN）
# =========================
def coerce_numeric(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    df = df.copy()
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


# =========================
# Main preparation pipeline
# 前処理パイプライン本体
# =========================
def prepare_dataset(
    raw_path: str | Path,
    processed_path: str | Path,
) -> pd.DataFrame:
    """
    Full preprocessing pipeline
    前処理の一連の流れを実行
    """

    raw_path = Path(raw_path)
    processed_path = Path(processed_path)

    # Ensure directory exists
    # 保存先ディレクトリが無ければ作成
    processed_path.parent.mkdir(parents=True, exist_ok=True)

    df = read_csv_robust(raw_path)
    df = rename_columns_if_needed(df)
    df = add_year_built_and_age(df)

    df = coerce_numeric(
        df,
        ["station_minutes", "price", "area_sqm",
         "building_coverage_ratio", "floor_area_ratio"]
    )

    # Select minimal modeling columns
    # モデル用の基本列に絞る
    keep_cols = [
        "price",
        "area_sqm",
        "station_minutes",
        "year_built",
        "building_age",
        "nearest_station",
    ]

    keep_cols = [c for c in keep_cols if c in df.columns]
    df_use = df[keep_cols].copy()

    df_use.to_csv(processed_path, index=False, encoding="utf-8-sig")

    return df_use


# =========================
# Script execution
# スクリプト単体実行時
# =========================
if __name__ == "__main__":

    RAW_PATH = "data/raw/Tokyo_Suginami_Ward_20234_20253.csv"
    PROCESSED_PATH = "data/processed/Tokyo_Suginami_clean.csv"

    df_use = prepare_dataset(RAW_PATH, PROCESSED_PATH)

    print("Data types:")
    print(df_use.dtypes)
    print("\nPreview:")
    print(df_use.head())