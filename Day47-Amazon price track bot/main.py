import requests
from bs4 import BeautifulSoup
import lxml
import json
import smtplib

S_EMAIL = "jingnasong805@gmail.com"
S_PASS = "Sjn18275771142"
URL = "https://www.macys.com/shop/product/lancome-absolue-revitalizing-brightening-soft-cream-with-grand-rose-extracts-2-oz.?ID=7796308&CategoryID=30078"
header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
}


response = requests.get(URL, headers=header)

item_web_page = response.content
soup = BeautifulSoup(item_web_page, "lxml")
# print(soup.prettify())



result = soup.find(name="script", id="productMktData", type="application/ld+json")
# print(result)
item_dict = json.loads(result.contents[0])
price = float(item_dict['offers'][0]['price'])
title = item_dict["name"]
# print(product)
# print(price)


BUY_PRICE = 180

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=S_EMAIL, password=S_PASS)
        connection.sendmail(from_addr=S_EMAIL,
                            to_addrs="queenasong805@gmail.com",
                            msg=f"Subject: Macy's Price Alert!\n\n{message}\n{URL}"
                            )
