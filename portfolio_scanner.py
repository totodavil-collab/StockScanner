import yfinance as yf

portfolio = {
    "QQQM": 40,
    "SMH": 30,
    "URA": 15,
    "RKLB": 15
}

print("\n🔥 MY PORTFOLIO SCORE\n")

results = []

for symbol, weight in portfolio.items():

    try:

        stock = yf.Ticker(symbol)

        hist = stock.history(period="60d")

        if len(hist) < 50:
            continue

        today = float(hist["Close"].iloc[-1])

        ma20 = float(hist["Close"].tail(20).mean())

        ma50 = float(hist["Close"].tail(50).mean())

        score = 0

        if today > ma20:
            score += 40

        if today > ma50:
            score += 30

        if ma20 > ma50:
            score += 30

        if score >= 90:
            signal = "STRONG BUY"
        elif score >= 70:
            signal = "BUY"
        elif score >= 40:
            signal = "HOLD"
        else:
            signal = "WAIT"

        results.append({
            "symbol": symbol,
            "weight": weight,
            "score": score,
            "signal": signal
        })

    except Exception as e:

        print(f"{symbol} ERROR: {e}")

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

for item in results:

    print(
        f"{item['symbol']:6} "
        f"{item['weight']:>2}% "
        f"Score {item['score']:>3} "
        f"{item['signal']}"
    )

from datetime import datetime
import csv
import os

today = datetime.now().strftime("%Y-%m-%d")

file_exists = os.path.exists(
    "portfolio_history.csv"
)

with open(
    "portfolio_history.csv",
    "a",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    if not file_exists:

        writer.writerow([
            "Date",
            "Symbol",
            "Score",
            "Signal"
        ])

    for item in results:

        writer.writerow([
            today,
            item["symbol"],
            item["score"],
            item["signal"]
        ])
