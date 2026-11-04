# 旅行プラン相談チャットボット

友達との旅行を想定した、Flask製のシンプルな旅行プラン提案アプリです。
APIキー・外部API・有料サービスは不要です。登録済みの観光スポットとルールに基づいて提案します。

## ファイル構成
- `app.py`：Flaskのルートと旅行プラン生成ロジック
- `requirements.txt`：Flask・Gunicorn
- `templates/index.html`：画面のHTML
- `static/style.css`：デザイン
- `static/app.js`：チャット操作とAPI送信
- `render.yaml`：Renderの設定

## ローカル起動
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
ブラウザで http://127.0.0.1:5000 を開きます。

## Render
Build Command: `pip install -r requirements.txt`
Start Command: `gunicorn app:app`

GitHubにこのフォルダの中身をアップロードし、RenderでNew Web Serviceからリポジトリを選択します。RuntimeはPython。設定欄に上記コマンドを入力し、Deployします。
