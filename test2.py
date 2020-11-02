import requests
from bs4 import BeautifulSoup
import smtplib
import time
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
url = 'https://www.amazon.in/Stone-170-Bluetooth-Resistant-Mysterious/dp/B084GPDTVR'
response = requests.get(url, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.content, 'html.parser')
soup.encode('utf-8')

# title = soup.select("#productTitle")[0].get_text().strip()
title = soup.find(id= "productTitle").get_text().strip()

f = open("soup.html", "w",encoding= "utf-8")
f.write(str(soup))
f.close()

# time.sleep(5)
# priceblock_dealprice

try:
    try:
    	price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
    except:
    	price = soup.find(id = "priceblock_dealprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()

    review_count = soup.find(id="acrCustomerReviewText").get_text().split()[0]
    stars = soup.find(id = "acrPopover").get_text().strip()

    product = {'Product Name': title, 'price': price, 'stars':stars, 'Number of reviews': review_count}
    for key,value in product.items():
    	print(key , " : ", value)
    # print(json.dumps(jsonObject, indent=2))
except Exception as ee:
	print(ee)

