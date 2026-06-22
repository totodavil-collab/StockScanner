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

    response = requests.post(
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        json=payload
    )

    print("LINE STATUS =", response.status_code)


data = {}

with open(FILE, encoding="utf-8") as f:

    reader = csv.DictReader(f)

    for row in reader:

        symbol = row["Symbol"]

        if symbol not in data:
            data[symbol] = []

        data[symbol].append(row)

print("\n🚨 SIGNAL CHANGE CHECK\n")

alerts = []

for symbol, history in data.items():

    if len(history) < 2:
        continue

    previous = history[-2]["Signal"]
    current = history[-1]["Signal"]

    if previous != current:

        alerts.append(
            f"{symbol}\n{previous} → {current}"
        )

if alerts:

    alert_text = "🚨 SIGNAL CHANGE\n\n"
    alert_text += "\n\n".join(alerts)

    print(alert_text)

    send_line(alert_text)

scan_text = ""

if os.path.exists("daily_scan.txt"):

    with open(
        "daily_scan.txt",
        encoding="utf-8"
    ) as f:

        scan_text = f.read()

summary = "📈 DAILY PORTFOLIO\n\n"

for symbol, history in data.items():

    latest = history[-1]

    summary += (
        f"{symbol} : "
        f"{latest['Signal']}\n"
    )

final_message = (
    scan_text
    + "\n\n"
    + summary
)

send_line(final_message)
