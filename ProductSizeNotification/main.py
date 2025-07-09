import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

MY_EMAIL = email
PASSWORD = password
product_url = url

response = requests.get(product_url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

not_available_alert = soup.select_one("div.alert")

msg = EmailMessage()
msg["Subject"] = "Produkt znów dostępny!"
msg["From"] = MY_EMAIL
msg["To"] = email
msg.set_content(f"Produkt na który czekasz znów jest dostępny w sprzedaży!<3\nLINK: {product_url}")

if not not_available_alert:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.send_message(
            from_addr=MY_EMAIL,
            to_addrs=email
            msg=msg)





