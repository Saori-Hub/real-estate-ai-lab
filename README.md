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

# 不動産AIラボ（日本語版）

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

## 本プロジェクトの位置づけ

不動産実務者がAI・データ分析を実務レベルへ昇華させるための、構造化された検証プロジェクトです。
