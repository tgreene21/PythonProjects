from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

#Load env variables
load_dotenv()

#This should be the link to the Amazon page of the item
URL = "https://www.amazon.com/COTTON-CRAFT-Round-Pouf-Ottoman/dp/B00TIO07YS?pf_rd_p=2b7b98a6-ae90-4248-a5e1-2321618b5b1a&pf_rd_r=PP9VGBHA7R7ZAJKCNFVG&ref_=OTC24_dormlife_compct_dt_B00TIO07YS&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
amazon_web = response.text
soup = BeautifulSoup(amazon_web, "html.parser")

# Get the price of the item
dollar_text = soup.find(name = "span", class_ = "a-price-whole")
cent_text = soup.find(name = "span", class_ = "a-price-fraction")

# print(dollar_text.getText())
# print(cent_text.getText())

current_price = float(dollar_text.getText() + cent_text.getText())

# Price you want to pay equal to or less than
target_price = 100

if current_price <= target_price:
    
    sender_email = os.getenv("SENDER_EMAIL", "sender email")
    sender_password = os.getenv("PASSWORD", "password here")
    receiver_email = os.getenv("RECEIVER_EMAIL", "receiver email here")

    product_name = soup.find(name = "span", id="productTitle").getText()
    product_name_revised = " ".join(product_name.split())
    print(product_name_revised)


    #If there's a UnicodeEncoding error like there's a special character then encode in utf-8

    with smtplib.SMTP(os.getenv("SMTP_ADDRESS")) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        try:
            connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=f"Subject:Amazon Price Alert\n\n Product Name: {product_name_revised}\nCurrent Price: {current_price}\n{URL}")
        except UnicodeEncodeError:
            product_name_revised = product_name.strip().encode("UTF-8")
            connection.sendmail(from_addr=sender_email,
                                to_addrs=receiver_email,
                                msg=f"Subject:Amazon Price Alert\n\nProduct Name: {product_name_revised}\nCurrent Price: {current_price}\n{URL}")
