from bs4 import BeautifulSoup
import requests
import subprocess
import os,sys
import time
from urlparse import urlparse


def pricecheck(url, min_price):
	parsed = urlparse(url)
	parsed_url = "http://"+parsed.netloc+parsed.path
	print (parsed_url)
	r = requests.get(parsed_url)
	data = r.text
	soup = BeautifulSoup(data)
	for price in soup.find_all(itemprop="price"):
		p = price.get('content')
		p = p.replace(',','')
		if int(p) < min_price:
			subprocess.Popen(['notify-send', "It's time to buy. price has droped"])
			exit()
		else:
			print ("checking...", p)
			time.sleep(3600)
			pricecheck()


url = raw_input("paste url here: ")
min_price = int(raw_input("type minimum price: "))


message = "It's time to buy. price has droped below", min_price
pricecheck(url, min_price)
