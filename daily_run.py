import os

BASE = "/Users/totodavil/StockScanner"

print("\n========================")
print("STOCK SCANNER")
print("========================\n")

os.system(
    f"/Users/totodavil/StockScanner/venv/bin/python3 {BASE}/scanner.py"
)

print("\n========================")
print("PORTFOLIO SCANNER")
print("========================\n")

os.system(
    f"/Users/totodavil/StockScanner/venv/bin/python3 {BASE}/portfolio_scanner.py"
)

print("\n========================")
print("ALERT ENGINE")
print("========================\n")

os.system(
    f"/Users/totodavil/StockScanner/venv/bin/python3 {BASE}/alert_engine.py"
)
