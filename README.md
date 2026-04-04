# Real Estate AI Lab

---

## Concept

Real Estate AI Lab is an ongoing experimental project that integrates real estate domain expertise with data science and machine learning.

This repository is not a single analysis project, but a structured lab environment to explore how AI can support real-world real estate decision-making.

---

## Vision

The goal of this lab is to develop reproducible and practical AI workflows that enhance:

- Property price analysis  
- Market structure understanding  
- Investment decision support  
- Data-driven strategy in real estate operations  

This project evolves step by step as new models and analytical methods are tested and validated.

---

## Current Stage

**Phase 1 – Foundation**

- Public real estate transaction data acquisition (MLIT)
- Data cleaning and column standardization
- Feature engineering (area, age, station distance)
- Basic regression modeling
- Model evaluation using R² and MAE

---

## Roadmap

**Phase 2 – Model Improvement**

- Cross-validation
- Regularization (Ridge / Lasso)
- Feature importance analysis

**Phase 3 – Advanced Modeling**

- Random Forest regression
- Residual diagnostics
- Multi-ward expansion

**Phase 4 – Practical Decision Support**

- Investment indicator modeling
- Price deviation detection
- Scenario simulation for business use

---

## Data Source

- Ministry of Land, Infrastructure, Transport and Tourism (MLIT)
- Real Estate Transaction Price Information
- Area: Suginami Ward, Tokyo (initial dataset)

Raw data is not included in this repository.  
Please download it from the official MLIT website and place it under:
```
data/raw/
```
Then run:
```
python src/prepare_data.py
```

---

## Project Structure
```
real-estate-ai-lab/
├ data/
│ ├ raw/
│ └ processed/
├ notebooks/
├ src/
└ README.md
```

---

## Tech Stack

- Python
- pandas
- scikit-learn
- matplotlib
- Git / GitHub

---

## Model Performance

Using Suginami Ward transaction data:

- Model: Linear Regression (log-transformed price)
- Features: area_sqm, station_minutes, building_age
- R² (log scale): 0.81
- MAE: ~12.8 million JPY
- MAPE: ~25%

### Missing Value Strategy

- Two-step median imputation (by station → global median)
- Missing flag modeling tested
- Missingness was found to have negligible predictive power

### Text Cleaning (YouTube Transcript Preprocessing)

Remove timestamps like `1:23`, `12:34` from transcript data.

#### Script
`scripts/clean_timestamp.py`

#### Usage
```bash
python scripts/clean_timestamp.py data/raw/input.txt data/processed/output.txt

---

# 不動産AIラボ

---

## コンセプト

Real Estate AI Lab は、不動産実務の専門性とデータサイエンス／機械学習を統合するための継続的な検証プロジェクトです。

単発の分析ではなく、AIを活用した不動産実務の高度化を目指す「実験環境（ラボ）」として設計しています。

---

## ビジョン

本ラボでは、以下を強化することを目的としています。

- 不動産価格分析の高度化  
- 市場構造の理解  
- 投資判断の支援  
- データに基づく業務意思決定  

分析手法やモデルは段階的に拡張していきます。

---

## 現在の段階

**フェーズ1：基礎構築**

- 国土交通省公開データの取得
- データ前処理および列名英語化
- 特徴量設計（面積・築年数・駅距離）
- 回帰モデル構築
- R²・MAEによる評価

---

## 今後の展開

**フェーズ2：モデル改善**

- 交差検証
- 正則化回帰（Ridge / Lasso）
- 重要特徴量の分析

**フェーズ3：高度化**

- ランダムフォレストによる非線形モデル
- 残差分析
- 複数エリアへの拡張

**フェーズ4：実務応用**

- 投資指標モデル
- 割安物件検知
- シナリオシミュレーション

---

## モデル性能

杉並区の不動産取引データを用いた基礎モデルの結果は以下の通りです。

- モデル：線形回帰（価格を対数変換）
- 使用特徴量：area_sqm（面積）、station_minutes（駅徒歩分数）、building_age（築年数）
- R²（対数スケール）：0.81
- MAE（平均絶対誤差）：約1,280万円
- MAPE（平均絶対誤差率）：約25%

### 欠損値処理の検証

- 駅別中央値 → 全体中央値の2段階補完を実施
- 欠損フラグを加えたモデルも比較
- 欠損そのものは価格予測に対して有意な情報を持たないことを確認

本データセットでは、2段階中央値補完を採用しています。

---

## 本プロジェクトの位置づけ

不動産実務者がAI・データ分析を実務レベルへ昇華させるための、構造化された検証プロジェクトです。
