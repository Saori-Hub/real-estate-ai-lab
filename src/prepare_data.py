import os
import pandas as pd

RAW_PATH = "data/raw/Tokyo_Suginami_Ward_20234_20253.csv"
OUT_PATH = "data/processed/Tokyo_Suginami_renamed.csv"

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

def main():
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    df = pd.read_csv(RAW_PATH, encoding="utf-8")
    df = df.rename(columns=RENAME_MAP)

    df.to_csv(OUT_PATH, index=False)
    print("Saved:", OUT_PATH, "shape=", df.shape)

if __name__ == "__main__":
    main()