# import required files and modules

import requests
from bs4 import BeautifulSoup
import smtplib
import time
import random
import sys


class Amazon:
    def __init__(self, url):
        # self.url = "https://www.amazon.in/Bose-SoundLink-Wireless-Around-Ear-Headphones/dp/B0117RGG8E/ref=sr_1_11?qid=1562395272&refinements=p_89%3ABose&s=electronics&sr=1-11"
        self.url = url
        self.old_price = 99999999
        self.count = 0

        randomint = random.randint(0,9)
        user_agents = [
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
            'Mozilla/5.0 (X11; Linux i686; rv:82.0) Gecko/20100101 Firefox/82.0'
        ]

        self.headers = { 'User-Agent' : user_agents[randomint] } 

    def check_price(self):
        print("\n\nNew Amazon request: ")
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        soup.encode('utf-8')

        #print(soup.prettify())
        # f = open("soup.html", "w",encoding= "utf-8")
        # f.write(str(soup))
        # f.close()

        self.title = soup.find(id= "productTitle").get_text().strip()
        print(self.title)

        try:
          self.current_price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
        except:
          self.current_price = soup.find(id = "priceblock_dealprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()

        try:  
          self.current_price = int(self.current_price.split(".")[0])
          self.review_count = soup.find(id="acrCustomerReviewText").get_text().split()[0]
          self.stars = soup.find(id = "acrPopover").get_text().strip()

          try:
            self.product = {'Product Name': self.title, 'price': self.current_price, 'stars':self.stars, 'Number of reviews': self.review_count}
          except NameError as e:
            self.product = {'Product Name': self.title, 'price': self.current_price, 'stars':"Unable to fetch", 'Number of reviews': "Unable to fetch"}

          for key,value in self.product.items():
            print(key , " : ", value)
          # print(json.dumps(jsonObject, indent=2))

          if(self.current_price < self.old_price):
            self.old_price = self.current_price
            if self.count == 0:
              return True
            self.count = 1
            return False
          else:
            return True

        except Exception as pqpq:
          print(pqpq)


    # function that sends an email if the prices fell down
    def send_mail():
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.ehlo()

      server.login('email@gmail.com', 'password')

      subject = 'Price Fell Down'
      body = "Check the amazon link https://www.amazon.in/Bose-SoundLink-Wireless-Around-Ear-Headphones/dp/B0117RGG8E/ref=sr_1_11?qid=1562395272&refinements=p_89%3ABose&s=electronics&sr=1-11 "

      msg = f"Subject: {subject}\n\n{body}"
      
      server.sendmail(
        'sender@gmail.com',
        'receiver@gmail.com',
        msg
      )
      #print a message to check if the email has been sent
      print('Hey Email has been sent')
      # quit the server
      server.quit()

    #loop that allows the program to regularly check for prices
    

class Flipkart:
    def __init__(self, url):
        # self.url = "https://www.amazon.in/Bose-SoundLink-Wireless-Around-Ear-Headphones/dp/B0117RGG8E/ref=sr_1_11?qid=1562395272&refinements=p_89%3ABose&s=electronics&sr=1-11"
        self.url = url
        self.old_price = 999999999
        self.count = 0

        randomint = random.randint(0,9)
        print(randomint)
        user_agents = [
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
            'Mozilla/5.0 (X11; Linux i686; rv:82.0) Gecko/20100101 Firefox/82.0'
        ]

        self.headers = { 'User-Agent' : user_agents[randomint] } 

    def check_price(self):
        print("\n\nNew Flipkart request: ")
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        soup.encode('utf-8')

        #print(soup.prettify())
        f = open("soup.html", "w",encoding= "utf-8")
        f.write(str(soup))
        f.close()
        
        try:

          self.title = soup.find("span", {"class": "_35KyD6"}).text

          try:
            self.current_price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
            print(self.current_price)
          except:
            # self.current_price = soup.find(id = "priceblock_dealprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
            print("self.current_price exception")

          self.current_price = int(self.current_price.split(".")[0])

          self.review_count = soup.find("span", {"class": "_38sUEc"}).get_text()
          self.stars = soup.find("div", {"class": "hGSR34"}).text
          
          try:
            self.product = {'Product Name': self.title, 'price': self.current_price, 'stars':self.stars, 'Number of reviews and ratings': self.review_count}
          except NameError as e:
            self.product = {'Product Name': self.title, 'price': self.current_price, 'stars': "Unable to fetch", 'Number of reviews and ratings': "Unable to fetch"}

          for key,value in self.product.items():
            print(key , " : ", value)
          # # print(json.dumps(jsonObject, indent=2))

          if(self.current_price < self.old_price):
            self.old_price = self.current_price
            if self.count == 0:
              return True
            self.count = 1
            return False
          else:
            return True

        except Exception as ww:
          print(ww)



def main(url, website):
  if website == "amazon":
    obj = Amazon(url)
    check_signal = obj.check_price()
    while(check_signal):
      print("Again checking")
      check_signal = obj.check_price()
      time.sleep(3600)
    print("3600 sec done")
    
  if website == "flipkart":
    obj = Flipkart(url)
    check_signal = obj.check_price()
    print(check_signal)
    while(check_signal):
      print("Again checking")
      check_signal = obj.check_price()
      time.sleep(3600)
    print("3600 sec done")

  return obj.product
