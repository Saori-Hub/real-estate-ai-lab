import pandas as pd

PATH = "data/processed/Tokyo_Suginami_clean.csv"

df = pd.read_csv(PATH, encoding="utf-8-sig")

print("shape:", df.shape)
print("\nNaN counts:")
print(df[["station_minutes", "building_age"]].isna().sum())

print("\nNaN rate (%):")
print((df[["station_minutes", "building_age"]].isna().mean() * 100).round(3))

print("\nstation_minutes missing by nearest_station (top 10):")
print(df[df["station_minutes"].isna()]["nearest_station"].value_counts().head(10))

print("\nbuilding_age missing by nearest_station (top 10):")
print(df[df["building_age"].isna()]["nearest_station"].value_counts().head(10))

print("\n--- Imputation (2-step) ---")

df2 = df.copy()

# 1段階：駅別中央値
df2["station_minutes"] = df2["station_minutes"].fillna(
    df2.groupby("nearest_station")["station_minutes"].transform("median")
)

df2["building_age"] = df2["building_age"].fillna(
    df2.groupby("nearest_station")["building_age"].transform("median")
)

# 2段階：全体中央値
df2["station_minutes"] = df2["station_minutes"].fillna(
    df2["station_minutes"].median()
)

df2["building_age"] = df2["building_age"].fillna(
    df2["building_age"].median()
)

print("\nAfter imputation - NaN counts:")
print(df2[["station_minutes","building_age"]].isna().sum())

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

def run_model(data):
    X = data[["area_sqm","station_minutes","building_age"]]
    y = np.log1p(data["price"])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    pred_log = model.predict(X_test)
    pred = np.expm1(pred_log)
    y_true = np.expm1(y_test)

    return (
        r2_score(y_test, pred_log),
        mean_absolute_error(y_true, pred),
        np.mean(np.abs((y_true - pred)/y_true))*100
    )

# dropna版
df_drop = df[["price","area_sqm","station_minutes","building_age"]].dropna()

print("Dropna:", run_model(df_drop))

# 補完版
print("Imputed:", run_model(df2))

print("\n--- Missing Flag Model ---")

df3 = df.copy()

# 欠損フラグ
df3["station_minutes_missing"] = df3["station_minutes"].isna().astype(int)
df3["building_age_missing"] = df3["building_age"].isna().astype(int)

# 2段階補完
df3["station_minutes"] = df3["station_minutes"].fillna(
    df3.groupby("nearest_station")["station_minutes"].transform("median")
).fillna(df3["station_minutes"].median())

df3["building_age"] = df3["building_age"].fillna(
    df3.groupby("nearest_station")["building_age"].transform("median")
).fillna(df3["building_age"].median())

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

X = df3[[
    "area_sqm",
    "station_minutes",
    "building_age",
    "station_minutes_missing",
    "building_age_missing"
]]

y = np.log1p(df3["price"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

pred_log = model.predict(X_test)
pred = np.expm1(pred_log)
y_true = np.expm1(y_test)

print("R2 (log):", r2_score(y_test, pred_log))
print("MAE:", mean_absolute_error(y_true, pred))
print("MAPE:", np.mean(np.abs((y_true - pred)/y_true))*100)