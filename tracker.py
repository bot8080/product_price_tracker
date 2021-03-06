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
    self.product_details = ""

  def request_with_ua(self):
    self.error = ""
    lines = open("user_agents.txt").read().splitlines()
    user_agent =  random.choice(lines)

    self.headers = { 'User-Agent' : user_agent } 
    print("New Amazon request with : ", user_agent)
    
    response = requests.get(self.url)
    # response = requests.get(self.url, headers=self.headers)

    self.soup = BeautifulSoup(response.content, 'html.parser')
    self.soup.encode('utf-8')

    try:
      #check whether browser version is supported or not
      self.error = self.soup.find("div", {"class": "popup-header"}).text.strip()
      print("Browser is no longer supported")

    except Exception as bb:
      try:
        # when browser is supported then check captcha page
        self.error = self.soup.find("div", {"class": "a-box a-alert a-alert-info a-spacing-base"}).text.strip()
        print("Browser Captcha error")
        print("Self.error:",self.error)
        # print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(bb).__name__, bb)
      except Exception as bc:
        print("Browser is supported")
        # print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(bc).__name__, bc)
        pass
      # print(be)
    
    f = open("soup.html", "w",encoding= "utf-8")
    f.write(str(self.soup))
    f.close()

  def check_price(self):
    try:

      self.request_with_ua()
      while(self.error=="Your browser is no longer supported" or self.error.startswith("Enter the characters you see below")):
        print("User agent switching\n")
        self.request_with_ua()

      try:
        # print("current price block")
        self.title = self.soup.find(id= "productTitle").get_text().strip()
        self.current_price = self.soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
      except:
        print("Its a special deal price")
        self.current_price = self.soup.find(id = "priceblock_dealprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()

      try:  
        self.current_price = int(self.current_price.split(".")[0])
        self.review_count = self.soup.find(id="acrCustomerReviewText").get_text().split()[0]
        self.stars = self.soup.find(id = "acrPopover").get_text().strip()

        try:
          self.product_dict = {'Product Name': self.title, 'price': self.current_price, 'stars':self.stars, 'Number of reviews': self.review_count}
        except NameError as e:
          self.product_dict = {'Product Name': self.title, 'price': self.current_price, 'stars':"Unable to fetch", 'Number of reviews': "Unable to fetch"}

        for key,value in self.product_dict.items():
          self.product_details = self.product_details + str(key) + " : "+ str(value) + "\n"
        # print(json.dumps(jsonObject, indent=2))

        if(self.current_price < self.old_price):
          self.old_price = self.current_price
          if self.count == 0:
            return self.product_details
          self.count = 1
          return False
        else:
          return self.product_details

      except Exception as pqpq:
        print("second end block")
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(pqpq).__name__, pqpq)

    except Exception as qq:
        print("end block")
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(qq).__name__, qq)


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
    self.old_price = 99999999
    self.count = 0
    self.product_details = ""

  def request_with_ua(self):
    self.error = ""
    lines = open("user_agents.txt").read().splitlines()
    user_agent =  random.choice(lines)

    self.headers = { 'User-Agent' : user_agent } 
    print("New Flipkart request with : ", user_agent)
    response = requests.get(self.url, headers=self.headers)

    self.soup = BeautifulSoup(response.content, 'html.parser')
    self.soup.encode('utf-8')

    try:
      #check whether browser version is supported or not
      self.error = self.soup.find("div", {"class": "popup-header"}).text.strip()
      print("Browser is no longer supported")

    except Exception as be:
      print("Browser is supported")
      # print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(be).__name__, be)
      pass
      # print(be)

    # f = open("soup.html", "w",encoding= "utf-8")
    # f.write(str(self.soup))
    # f.close()
  
  def check_price(self):    
    try:
      
      self.request_with_ua()

      while(self.error=="Your browser is no longer supported"):
        print("User agent switching\n")
        self.request_with_ua()

      try:
        # print("current price block")
        self.title = self.soup.find("span", {"class": "_35KyD6"}).text
        self.current_price = self.soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
        # print(self.current_price)
      except:
        # self.current_price = soup.find(id = "priceblock_dealprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
        print("self.current_price exception")

      try:
        self.current_price = int(self.current_price.split(".")[0])
        self.review_count = self.soup.find("span", {"class": "_38sUEc"}).get_text()
        self.stars = self.soup.find("div", {"class": "hGSR34"}).text
        
        try:
          self.product_dict = {'Product Name': self.title, 'price': self.current_price, 'stars':self.stars, 'Number of reviews and ratings': self.review_count}
        except NameError as e:
          self.product_dict = {'Product Name': self.title, 'price': self.current_price, 'stars': "Unable to fetch", 'Number of reviews and ratings': "Unable to fetch"}

        for key,value in self.product_dict.items():
          self.product_details = self.product_details + str(key) + " : "+ str(value) + "\n"
        # # print(json.dumps(jsonObject, indent=2))

        if(self.current_price < self.old_price):
          self.old_price = self.current_price
          if self.count == 0:
            return self.product_details
          self.count = 1
          return False
        else:
          return self.product_details

      except Exception as qq:
        print("second end block")
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(qq).__name__, qq)

    except Exception as ww:
      print("end block")
      print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(ww).__name__, ww)



def main(url, website):
  try:
    if website == "amazon":
      obj = Amazon(url)
      check_signal = obj.check_price()
      while(check_signal):
        print("\nAgain checking")
        print(check_signal)
        check_signal = obj.check_price()
        time.sleep(10)
      print("3600 sec done")
      
    if website == "flipkart":
      obj = Flipkart(url)
      check_signal = obj.check_price()
      while(check_signal):
        print("Again checking")
        print(check_signal)
        check_signal = obj.check_price()
        time.sleep(10)
      print("3600 sec done")

    return obj.product_details
  except Exception as E:
    print(E)
