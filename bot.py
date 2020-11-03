import telebot
import time
import os
import requests
import re
import tracker


try:
  bot_token = "1492010823:AAFjY_4sCYjOmffnKykQU5luZVP1Q0eVDuI"

  bot = telebot.TeleBot(bot_token)

except Exception as pp:
  print("Error block :global 1")
  print(pp)

print("BOT STARTED")

def Find(string): 
  
    # findall() has been used  
    # with valid conditions for urls in string 
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url] 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to price notifier by patiala. 😇 \n This 🤖 will help you find your products at a very reasonable price..")
    bot.reply_to(message, "Click on /help for assitance.")


@bot.message_handler(commands=['restart'])
def restart(message):
    os.system('python "C:/Users/abhik/Desktop/stocks/stocks_analyser/stocks.py"')
    bot.reply_to(message, "Program started again")


# @bot.message_handler(commands=['search'])
# def search(message):
#     try:
#       res = requests.get('http://d.yimg.com/autoc.finance.yahoo.com/autoc?query='+message.text.split(" ", 1)[1]+'&lang=en')
#       bot.reply_to(message, res.json()['ResultSet']['Result'][0]['symbol'])
#     except Exception as ee:
#       print(ee)
#       bot.reply_to(message, "Company da naam is tarah likho /search apple")
#       pass



@bot.message_handler(commands=['help'])
def send_help(message):
  bot.reply_to(message, "1. Select your product from amazon/flipkart website or application \n2. Share product link from application to this bot\n3. Set your desired amount")


@bot.message_handler(func=lambda msg: msg.text is not None)
def at_answer(message):
  s = ""
  try:
    input_value = message.text.strip()
    print("\n \nNEW Link request ")
    # print(input_value)

    url = Find(input_value)[0]
    # print("AFTER PARSING")


    if url.startswith("https://www.amazon.in/"):
      new_obj = tracker.Amazon(url)
      product = new_obj.check_price()

      bot.reply_to(message, product)
      bot.reply_to(message, "Feel free, I will check the product price every hour and then I will notify you when the current price drops down!!!.")

      product = tracker.main(url, "amazon")
      
      bot.reply_to(message, "Your product price drops down, please check")
      bot.reply_to(message, product)

    elif url.startswith("https://dl.flipkart.com/dl/") or url.startswith("https://www.flipkart.com/"):
      new_obj = tracker.Flipkart(url)
      product = new_obj.check_price()

      bot.reply_to(message, product)
      bot.reply_to(message, "Feel free, I will check the product price every hour and then I will notify you when the current price drops down!!!.")

      product = tracker.main(url, "flipkart")
      
      bot.reply_to(message, "Your product price drops down, please check")
      bot.reply_to(message, product)

      
    elif url.startswith("https://www.amazon.com/"):
      bot.reply_to(message, "Please send www.amazon.in link, www.amazon.com not supoorted yet " )

    else:
      print("Not a valid FLIPKART OR AMAZON product link")
      bot.reply_to(message, "Not a valid FLIPKART OR AMAZON product link")

  except Exception as op:
    print(op)
    bot.reply_to(message, "Does not found a valid URL ")


while True:
  try:
    bot.polling()
  except Exception as ee:
    print("POLLING")
    print(ee)
    pass
    # time.sleep(15)

