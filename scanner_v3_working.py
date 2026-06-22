import yfinance as yf

stocks = [

    # AI
    "NVDA",
    "AMD",
    "PLTR",
    "MU",
    "AVGO",
    "TSM",
    "SMCI",

    # Space
    "RKLB",
    "ASTS",
    "RDW",

    # Nuclear
    "CCJ",
    "OKLO",
    "NNE",

    # Data Center
    "VRT",
    "HPE",
    "LITE",

    # Quantum
    "IONQ",
    "RGTI",
    "QBTS"
]

results = []

print("\nกำลังสแกนหุ้น...\n")

for symbol in stocks:

    try:

        stock = yf.Ticker(symbol)

        hist = stock.history(period="5d")

        if len(hist) < 2:
            continue

        yesterday = float(hist["Close"].iloc[-2])
        today = float(hist["Close"].iloc[-1])

        pct = ((today - yesterday) / yesterday) * 100

        results.append({
            "symbol": symbol,
            "price": today,
            "pct": pct
        })

    except Exception as e:

        print(f"{symbol} ERROR: {e}")

results = sorted(
    results,
    key=lambda x: x["pct"],
    reverse=True
)

print("\n🔥 TOP MOMENTUM\n")

for i, item in enumerate(results[:10], start=1):

    print(
        f"{i:>2}. "
        f"{item['symbol']:6} "
        f"{item['pct']:>7.2f}% "
        f"${item['price']:.2f}"
    )
