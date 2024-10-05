# Streamlitポートフォリオアプリケーション（自己学習用）

## 使用技術一覧

<p style="display: inline">
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
  <img src="https://img.shields.io/badge/-Streamlit-FF4B4B.svg?logo=streamlit&style=for-the-badge">
  <img src="https://img.shields.io/badge/-Pandas-150458.svg?logo=pandas&style=for-the-badge">
  <img src="https://img.shields.io/badge/-Plotly-3F4F75.svg?logo=plotly&style=for-the-badge">
</p>

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [環境](#環境)
3. [ディレクトリ構成](#ディレクトリ構成)
4. [開発環境構築](#開発環境構築)
5. [使用方法](#使用方法)

## プロジェクトについて

このプロジェクトは、Streamlitを使用したデータ分析と可視化のポートフォリオアプリケーションです。CSVやExcelファイルのアップロード、データの表示、グラフの生成などの機能を提供します。

デプロイされたアプリケーションは以下のURLで確認できます：
[appportfolio-yurune111.streamlit.app](https://appportfolio-yurune111.streamlit.app)

## 環境

| 言語・フレームワーク   | バージョン  |
| -------------------- | ---------- |
| Python               | 3.12.7     |
| Streamlit            | 1.37.1     |
| Pandas               | 2.2.2      |
| Plotly               | 5.24.0     |
| openpyxl             | 3.1.2      |

その他のパッケージのバージョンは `requirements.txt` を参照してください。

## ディレクトリ構成

```
.
├── data
│   ├── sample_data.csv
│   └── sample_data.xlsx
├── .gitignore
├── README.md
├── app.py
└── requirements.txt
```

## 開発環境構築

1. リポジトリをクローンします：
   ```
   git clone https://github.com/yourusername/streamlit-portfolio.git
   cd streamlit-portfolio
   ```

2. 仮想環境を作成し、有効化します：
   ```
   python -m venv venv
   source venv/bin/activate  # Linuxの場合
   venv\Scripts\activate  # Windowsの場合
   ```

3. 必要なパッケージをインストールします：
   ```
   pip install -r requirements.txt
   ```

4. アプリケーションを実行します：
   ```
   streamlit run app.py
   ```

5. ブラウザで `http://localhost:8501` を開いてアプリケーションにアクセスします。

## 使用方法

1. アプリケーションを起動すると、サイドバーにさまざまな操作オプションが表示されます。
2. CSVまたはExcelファイルをアップロードして、データを表示および分析します。
3. グラフの種類や表示するデータを選択して、視覚化を行います。
4. アプリケーション内の各セクションの説明に従って、機能を探索してください。

このREADME.mdテンプレートは、プロジェクトの概要、使用技術、環境設定、ディレクトリ構造、開発環境の構築手順、そして基本的な使用方法を含んでいます。これにより、第三者（面接官や未経験者を含む）が容易にプロジェクトを理解し、環境を構築できるようになります。

## アプリケーションの更新とメンテナンス

1. VSCodeでアプリケーションのコードを変更します。
2. 「ソース管理」パネルで、変更したファイルをステージングします。
3. 適切なコミットメッセージを入力します。
4. 「コミット」ボタンをクリックしてコミットします。
5. 「変更の同期」ボタンをクリックして変更をGitHubにプッシュします。

Streamlit Cloudは自動的にGitHubの変更を検知し、新しいバージョンのアプリケーションを自動的にデプロイします。

## セキュリティ更新

VSCodeのターミナルで以下のコマンドを実行して、依存関係を更新します：

```
pip install -U -r requirements.txt
```

更新後、ローカルでアプリケーションをテストし、問題がなければGitHubにプッシュします。

## パフォーマンスの最適化

- データの効率的な読み込み：必要な部分のみを読み込む
- 計算結果のキャッシュ：重複計算を避ける
- 画像や動画の最適化：適切なサイズと形式を使用
- 不要なデータの削除：使用しないデータを削除
- ページ分割：大量の情報を複数ページに分ける
