import csv
import os
import requests

FILE = "portfolio_history.csv"
CHANNEL_ACCESS_TOKEN = "ez4FG3Ob8CF/4qMfjlkNWpW30kiMcOM3OwAIK3bt93+Xd0Hd9K6XEy6uBy9QB3YEjh6k9Zh+cCB7ueKCIOeVFMSJqNsgI/SYEgFI98rp7E/IJMvME2XmAB4Fi/GufiDOcK7sbBggHo3v8ExWo4P79wdB04t89/1O/w1cDnyilFU="
USER_ID = "U3ab25f9f85b39d7c610a48264ec2f7bc"

if not os.path.exists(FILE):
    print("ไม่พบ portfolio_history.csv")
    exit()

def send_line(message):

    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

    requests.post(
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        json=payload
    )

data = {}

with open(FILE, encoding="utf-8") as f:

    reader = csv.DictReader(f)

    for row in reader:

        symbol = row["Symbol"]

        if symbol not in data:
            data[symbol] = []

        data[symbol].append(row)

print("\n🚨 SIGNAL CHANGE CHECK\n")
send_line("🚀 STOCK SCANNER TEST")

for symbol, history in data.items():

    if len(history) < 2:
        continue

    previous = history[-2]["Signal"]
    current = history[-1]["Signal"]
    if previous != current:

        msg = (
            f"🚨 STOCK ALERT\n\n"
            f"{symbol}\n"
            f"{previous} → {current}"
        )

        print(msg)

        send_line(msg)

summary = "\n📈 DAILY PORTFOLIO\n\n"

for symbol, history in data.items():

    latest = history[-1]

    summary += (
        f"{symbol} : "
        f"{latest['Signal']}\n"
    )

send_line(summary)

summary = "📈 DAILY PORTFOLIO\n\n"
