# import required files and modules

import requests
from bs4 import BeautifulSoup
import smtplib
import time


class Amazon:
    def __init__(self, url, price):
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        # self.url = "https://www.amazon.in/Bose-SoundLink-Wireless-Around-Ear-Headphones/dp/B0117RGG8E/ref=sr_1_11?qid=1562395272&refinements=p_89%3ABose&s=electronics&sr=1-11"
        self.url = url
        self.price = price

    def check_price(self):
        print("\n\nNew request: ")
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        soup.encode('utf-8')

        #print(soup.prettify())

        title = soup.find(id= "productTitle").get_text()
        price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
        #print(price)

        #converting the string amount to float
        converted_price = float(price[0:5])
        print(converted_price)

        if(converted_price < self.price):
            # send_mail()
            f = open("detail.txt", "a")
            f.write("Price less than\n")
            f.close()

            print("Price less than", self.price)
            print(title.strip())
        else:
            f = open("detail.txt", "a")
            f.write("Price greater than\n")
            f.close()

            print("Price is greater", self.price)
            #using strip to remove extra spaces in the title
            print(title.strip())


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
    

    


url = "https://www.amazon.in/Bose-SoundLink-Wireless-Around-Ear-Headphones/dp/B0117RGG8E/ref=sr_1_11?qid=1562395272&refinements=p_89%3ABose&s=electronics&sr=1-11"
obj = Amazon(url, 100000)
while(True):
    obj.check_price()
    # self.check_price()
    time.sleep(120)
