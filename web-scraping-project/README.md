# Web Scraping Project

Python 初心者向けのシンプルな Web スクレイピングのデモプロジェクトです。
Python の公式サイトから基本的な情報（タイトル、見出し、段落数）を取得し、JSON 形式で保存します。

## プロジェクト構成

```
web-scraping-project
├── src
│   ├── main.py          # メインプログラム（実行するファイル）
│   └── scraper.py       # スクレイピング機能を実装したファイル
├── data
│   └── output.json      # 取得したデータの保存先
├── requirements.txt      # 必要なライブラリのリスト
└── README.md             # このファイル
```

## 必要な環境

- Python 3.7 以上
- pip（Python のパッケージ管理ツール）

## セットアップ手順

### 1. 必要なライブラリをインストール

ターミナルで以下のコマンドを実行してください：

```bash
pip install requests beautifulsoup4
```

または、requirements.txt を使用する場合：

```bash
pip install -r requirements.txt
```

### 2. data フォルダの作成

プロジェクトのルートディレクトリで以下を実行：

```bash
mkdir -p data
```

## 実行方法

### src フォルダに移動して実行

```bash
cd src
python main.py
```

または、プロジェクトのルートから実行：

```bash
python src/main.py
```

## 実行結果

成功すると以下のような出力が表示されます：

```
==================================================
スクレイピング開始
==================================================
アクセス中: https://www.python.org/
✓ アクセス成功！
✓ データ取得完了！

【取得したデータ】
タイトル: Welcome to Python.org
H1タグの数: 1
H1タグの内容: ['Welcome to Python.org']
段落(p)の数: 25

✓ データを ../data/output.json に保存しました！
```

取得したデータは`data/output.json`に保存されます。

## 取得するデータ

このプログラムは以下の情報を取得します：

- **title**: ページのタイトル（`<title>`タグの内容）
- **h1_tags**: すべての見出し（`<h1>`タグ）のリスト
- **p_count**: 段落（`<p>`タグ）の数

## コードの説明

### main.py

- プログラムのエントリーポイント
- スクレイピングの実行と結果の表示・保存を担当

### scraper.py

- `scrape_data(url)` 関数を提供
- 指定した URL にアクセスし、HTML を解析してデータを取得
- エラーハンドリングも実装

## カスタマイズ方法

### 別のサイトをスクレイピングする

`main.py`の`url`変数を変更してください：

```python
url = "https://example.com/"  # ここを変更
```

### 取得するデータを変更する

`scraper.py`の`data`辞書を編集してください：

```python
data = {
    'title': soup.title.string if soup.title else 'タイトルなし',
    'h1_tags': [h1.text.strip() for h1 in soup.find_all('h1')],
    'p_count': len(soup.find_all('p')),
    # 新しいデータを追加できます
}
```

## 注意事項

⚠️ **重要：スクレイピングを行う際の注意点**

1. **利用規約の確認**: 対象サイトの利用規約でスクレイピングが禁止されていないか確認してください
2. **robots.txt の確認**: サイトの`/robots.txt`でクローリングのルールを確認してください
3. **アクセス頻度**: 短時間に大量のリクエストを送らないようにしてください（サーバーに負荷がかかります）
4. **個人情報**: 個人情報を含むデータの取得・保存には十分注意してください
5. **著作権**: 取得したデータの著作権に注意してください

## トラブルシューティング

### `ModuleNotFoundError: No module named 'requests'`

→ ライブラリがインストールされていません。セットアップ手順 1 を実行してください。

### `FileNotFoundError: [Errno 2] No such file or directory: '../data/output.json'`

→ data フォルダが存在しません。セットアップ手順 2 を実行してください。

### `✗ エラー: ステータスコード 403`

→ サイトがアクセスをブロックしています。別のサイトを試すか、アクセス方法を変更してください。

## 学習のポイント

このプロジェクトを通じて学べること：

- Python の基本的な文法（関数、変数、if 文、try-except）
- 外部ライブラリの使い方（requests, BeautifulSoup）
- HTML の構造とタグの理解
- JSON データの扱い方
- ファイル入出力の基本

## 次のステップ

このプロジェクトをマスターしたら、以下に挑戦してみましょう：

1. 複数のページを連続してスクレイピング
2. 画像のダウンロード
3. CSV ファイルへの保存
4. より複雑な HTML 構造からのデータ取得
5. スクレイピング結果の可視化

## ライセンス

このプロジェクトは学習目的で作成されています。自由に改変・使用してください。
