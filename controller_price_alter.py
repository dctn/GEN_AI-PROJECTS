import requests
from bs4 import BeautifulSoup
import resend
import os

# ================= CONFIG =================
url = "https://www.amazon.in/dp/B0D8HY8CT8"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "en-IN,en;q=0.9"
}

TO_EMAIL = "thanipadai10@gmail.com"
LAST_PRICE_FILE = "/root/last_price.txt"

# Set your Resend API key as environment variable
resend.api_key = 're_CpLi5NhD_7fTvSDVA2t1SV1hcJ94b5rus'

# =========================================

def get_price():
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, "lxml")

        selectors = [
            ".a-price .a-offscreen",
            "#priceblock_ourprice",
            "#priceblock_dealprice",
            "#priceblock_saleprice"
        ]

        for sel in selectors:
            tag = soup.select_one(sel)
            if tag:
                return tag.get_text(strip=True)

        return None

    except Exception as e:
        print("Error fetching price:", e)
        return None


def get_last_price():
    if os.path.exists(LAST_PRICE_FILE):
        with open(LAST_PRICE_FILE, "r") as f:
            return f.read().strip()
    return None


def save_price(price):
    with open(LAST_PRICE_FILE, "w") as f:
        f.write(price)


def send_email(price):
    try:
        resend.Emails.send({
            "from": "maheswara@critictech.com",  # default test sender
            "to": [TO_EMAIL],
            "subject": "🎮 Cosmic Byte Blitz Price Alert",
            "html": f"""
                    <div style="font-family: Arial, sans-serif; line-height:1.5;">
                        <h2>Cosmic Byte Blitz</h2>

                        <p>Hello,</p>

                        <p>The current price is <strong>{price}</strong>.</p>

                        <p>You can check it here:</p>
                        <p><a href="{url}">View Product on Amazon</a></p>

                        <br>
                        <p style="font-size:12px;color:gray;">
                            You are receiving this because you subscribed to price alerts.
                        </p>
                    </div>
                    """
        })
        print("Email sent via Resend ✅")

    except Exception as e:
        print("Email failed:", e)


# ================= MAIN =================

price = get_price()

if price:
    print("Current Price:", price)

    last_price = get_last_price()

    send_email(price)
    if price != last_price:
        print("Price changed! Sending email...")
        # save_price(price)
    else:
        print("No change in price. No email sent.")

else:
    print("Price not found (maybe blocked or HTML changed)")