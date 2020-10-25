# -*- coding: utf-8 -*-
# import _thread
# import time

# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while count < 4:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# # Create two threads as follows
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-3", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-4", 2, ) )
#    _thread.start_new_thread( print_time, ("--------", 2, ) )
#    _thread.start_new_thread( print_time, ("--------", 2, ) )


# except Exception as ss:
#    print (ss)

# print("DONE")

# while 1:
#   pass

import telebot
import time
import os
import requests

setup_name = "default"

try:
  bot_token = "#"

  bot = telebot.TeleBot(bot_token)

except Exception as pp:
  print("Error block :global 1")
  print(pp)

print("BOT STARTED")

def get_stock_name(message,msg):
  # for text in msg:
    if msg.startswith("@"):
      bot.reply_to(message, "Stock name {}".format(msg))
      return msg[1:]

def get_interval(message,msg):
  for text in msg:
    if text[0].isdigit() or text:
      bot.reply_to(message, "Interval {}".format(text))
      return text

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to price notifier by patiala. 😇 \n This 🤖 will help you find your products at a very reasonable price..")


@bot.message_handler(commands=['restart'])
def restart(message):
    os.system('python "C:/Users/abhik/Desktop/stocks/stocks_analyser/stocks.py"')
    bot.reply_to(message, "Mubaarka, Server dobara chal peya.")


@bot.message_handler(commands=['search'])
def search(message):
    try:
      res = requests.get('http://d.yimg.com/autoc.finance.yahoo.com/autoc?query='+message.text.split(" ", 1)[1]+'&lang=en')
      bot.reply_to(message, res.json()['ResultSet']['Result'][0]['symbol'])
    except Exception as ee:
      print(ee)
      bot.reply_to(message, "Company da naam is tarah likho /search apple")
      pass



@bot.message_handler(commands=['help'])
def send_welcome(message):
  bot.reply_to(message, "1. To use this bot, send stock name like this '@SBI.NS 1d' or '@SBIN.NS 1m' or '@SBI.NS 1mo' etc.\n2. search - Search stocks symbol (/search apple) \n3. restart - In case of failure (/restart) \n4. setup - Two setups - Default (for latest date) and Date \n5. help - How to use bot? (/help)")


@bot.message_handler(func=lambda msg: msg.text is not None)
def at_answer(message):
  global setup_name
  ohlc = []
  ohlc.clear()

  input_value = message.text.split(" ")
  bot.reply_to(message, input_value)
  # Eg. input_value = ['stock name', 'interval', 'date']
  

while True:
  try:
    bot.polling()
  except Exception as ee:
    print("POLLING")
    print(ee)
    pass
    # time.sleep(15)

