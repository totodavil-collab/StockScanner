import yfinance as yf
import os
import csv
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

groups = {
    "AI": ["NVDA", "AMD", "PLTR", "MU", "AVGO", "TSM", "SMCI", "ARM"],
    "SPACE": ["RKLB", "ASTS", "RDW", "PL"],
    "NUCLEAR": ["CCJ", "OKLO", "NNE", "LEU"],
    "QUANTUM": ["IONQ", "RGTI", "QBTS"],
    "DATACENTER": ["VRT", "EQIX", "DLR"],
    "COPPER": ["FCX", "SCCO"],
    "CYBERSECURITY": ["CRWD", "PANW", "FTNT"],
    "SOFTWARE": ["SNOW", "DDOG", "MDB"],
    "ROBOTICS": ["SYM", "SERV", "PATH"]
}

def analyze_stock(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="20d")

        if len(hist) < 10:
            return None

        yesterday = float(hist["Close"].iloc[-2])
        today = float(hist["Close"].iloc[-1])

        ma20 = float(hist["Close"].tail(20).mean())

        if today < ma20:
            return None

        pct = ((today - yesterday) / yesterday) * 100

        if pct <= 0:
            return None

        volume_today = float(hist["Volume"].iloc[-1])
        avg_volume = float(hist["Volume"].tail(10).mean())

        relative_volume = volume_today / avg_volume

        score = min(100, pct * 8 + relative_volume * 20)

        return {
            "symbol": symbol,
            "pct": pct,
            "score": score
        }

    except Exception:
        return None

hot_stocks = []

print("\n🔥 AI STOCK SCANNER V5\n")

for group_name, symbols in groups.items():

    results = []

    for symbol in symbols:

        data = analyze_stock(symbol)

        if data:

            results.append(data)

            if data["score"] >= 70 and data["pct"] >= 3:
                hot_stocks.append(data)

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print(f"\n=== {group_name} ===")

    for item in results[:3]:

        print(
            f"{item['symbol']:6} "
            f"Score {item['score']:>5.0f} "
            f"({item['pct']:.2f}%)"
        )

hot_stocks.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\n🔥 หุ้นซิ่งคืนนี้\n")

for stock in hot_stocks[:5]:

    print(
        f"{stock['symbol']:6} "
        f"Score {stock['score']:.0f} "
        f"({stock['pct']:.2f}%)"
    )

history_dir = os.path.join(BASE_DIR, "history")
os.makedirs(history_dir, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")

filename = os.path.join(
    history_dir,
    f"{today}.csv"
)

with open(
    filename,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Symbol",
        "Score",
        "Percent"
    ])

    for stock in hot_stocks[:5]:

        writer.writerow([
            stock["symbol"],
            round(stock["score"], 0),
            round(stock["pct"], 2)
        ])

print(f"\n💾 Saved: {filename}")
