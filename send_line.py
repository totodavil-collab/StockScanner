import requests

CHANNEL_ACCESS_TOKEN = "c9P9Z1+wgxQsh3UpELBqJ3NwMCDUa+8WUzPyCq7a5uU9abC2w88IErSr1v/V8E53jh6k9Zh+cCB7ueKCIOeVFMSJqNsgI/SYEgFI98rp7E8couf+KjQQl+p7QLKfds0KGMG17hdF7ltEIuf9NAI2XgdB04t89/1O/w1cDnyilFU="
USER_ID = "U3ab25f9f85b39d7c610a48264ec2f7bc"

headers = {
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "to": USER_ID,
    "messages": [
        {
            "type": "text",
            "text": "🚀 StockScanner เชื่อมต่อ LINE สำเร็จ"
        }
    ]
}

response = requests.post(
    "https://api.line.me/v2/bot/message/push",
    headers=headers,
    json=payload
)

print(response.status_code)
print(response.text)
