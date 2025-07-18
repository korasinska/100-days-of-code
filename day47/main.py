import requests
from bs4 import BeautifulSoup
import os
import smtplib
from email.message import EmailMessage

PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = os.environ["LIVE_URL"]
FROM_EMAIL = os.environ["FROM_EMAIL_ADDRESS"]
FROM_EMAIL_PASS = os.environ["FROM_EMAIL_PASSWORD"]
TO_EMAIL = os.environ["TO_EMAIL"]

target_price = 100.00
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url=LIVE_URL, headers=header)
html = response.text

soup = BeautifulSoup(html, "html.parser")
price_whole = soup.select_one("span.a-price-whole").getText()
price_fraction = soup.select_one("span.a-price-fraction").getText()
product_title = soup.select_one("span#productTitle").getText()
price = float(price_whole + price_fraction)

msg = EmailMessage()
msg["Subject"] = "Amazon Price Alert!"
msg["From"] = FROM_EMAIL
msg["To"] = TO_EMAIL
content = f"{product_title.strip()} is now below ${target_price} (${price})\n{LIVE_URL}"
msg.set_content(content)


if price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=FROM_EMAIL_PASS)
        connection.send_message(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=msg
        )