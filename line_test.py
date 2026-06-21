import requests

CHANNEL_ACCESS_TOKEN = "7772b8e5cb40e99d6dc1ae43ce4ccd52ี้"
USER_ID = "2010459323ี้"

headers = {
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "to": USER_ID,
    "messages": [
        {
            "type": "text",
            "text": "🚀 StockScanner พร้อมใช้งานแล้ว"
        }
    ]
}

requests.post(
    "https://api.line.me/v2/bot/message/push",
    headers=headers,
    json=payload
)
