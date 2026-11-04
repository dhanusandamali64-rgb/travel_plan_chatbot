from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# APIキー不要のルールベース旅行プラン提案
DESTINATIONS = {
    "東京": ["浅草", "上野公園", "東京スカイツリー", "渋谷"],
    "京都": ["清水寺", "伏見稲荷大社", "嵐山", "祇園"],
    "大阪": ["大阪城", "道頓堀", "海遊館", "通天閣"],
    "沖縄": ["美ら海水族館", "古宇利島", "首里城", "ビーチ"],
    "北海道": ["小樽運河", "札幌時計台", "大通公園", "市場"],
    "福岡": ["太宰府天満宮", "中洲", "大濠公園", "博多"]
}

def make_plan(destination, budget, days):
    spots = DESTINATIONS.get(destination, ["人気スポット", "街歩き", "カフェ", "景色のよい場所"])
    per_day = max(1, len(spots) // min(days, 4))
    itinerary = []
    for day in range(1, days + 1):
        a = spots[(day - 1) % len(spots)]
        b = spots[day % len(spots)]
        itinerary.append(f"**{day}日目**：{a}を観光 → {b}周辺でランチ・散策")
    if budget < 10000:
        tip = "節約ポイント：公共交通機関を使い、無料スポットやリーズナブルな食事を中心にしましょう。"
    elif budget < 30000:
        tip = "予算の目安：交通費・食事・入場料をバランスよく組み合わせると楽しめます。"
    else:
        tip = "予算に余裕あり：体験ツアーや少し特別な食事も候補に入れられます。"
    return "\n".join(itinerary) + "\n\n" + tip

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    destination = str(data.get("destination", "東京")).strip()
    try:
        budget = int(data.get("budget", 20000))
        days = int(data.get("days", 2))
    except (TypeError, ValueError):
        return jsonify({"reply": "予算と日数は数字で入力してください。"}), 400
    budget = max(0, min(budget, 10000000))
    days = max(1, min(days, 14))
    if not destination:
        destination = "東京"
    plan = make_plan(destination, budget, days)
    reply = f"🎒 {destination}の旅行プラン案です！（{days}日間・予算{budget:,}円）\n\n{plan}\n\n※これはサンプル提案です。営業時間・交通・料金は旅行前に確認してください。"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
