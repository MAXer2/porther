import array # creating array
import telebot
import random
import string
import time
import requests
import json

from telebot import types
from array import *
#from randomsovet import my_list
import re
import mysql.connector
from mysql.connector import MySQLConnection, Error


server.debug = True

server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


bot = telebot.TeleBot('5220624851:AAGYx7fmi8z_32lGeydTm79HbaJc5TKi20E')

mydb = mysql.connector.connect(
  host="a0655204.xsph.ru",
  user="a0655204_castaneda",
  password="castaneda123$$$",
  database="a0655204_castaneda"
)


try:

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, f'''Приветствую тебя на Пути человека знания, {message.from_user.first_name}
Пиши в чат слова:

🕎Знание
⚛️Сила
🔯Практика

И получи свой ответ от К.Кастанеды, пропусти через себя.
🙏 Делай запрос прямо сейчас! ''')



    @bot.message_handler(content_types=['text'])

    def firstmenu(message):
        if (message.text).endswith('е') and 'Знание' or 'знание' in message.text:

            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT Count(ID) FROM `says` ")
            countid = int(mycursor.fetchone()[0])

            knowid = random.randint(1, countid)

            mycursor.execute(f"SELECT `TEXT` FROM `says` WHERE ID = {knowid} ")
            myresult = str(mycursor.fetchone()[0])
            bot.send_message (message.chat.id, myresult)
            mycursor.close()

        if 'Сила' in message.text or 'сила' in message.text and (message.text).endswith('а'):

            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT Count(ID_power) FROM `power` ")
            countid = int(mycursor.fetchone()[0])

            powerid = random.randint(1, countid)

            mycursor.execute(f"SELECT `TEXT_power` FROM `power` WHERE ID_power = {powerid} ")
            myresult = str(mycursor.fetchone()[0])
            bot.send_message (message.chat.id, myresult)
            mycursor.close()

        elif 'Практика'  in message.text or 'практика' in message.text and (message.text).endswith('а'):


            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT Count(ID_practice) FROM `practice` ")
            countid = int(mycursor.fetchone()[0])

            practiceid = random.randint(1, countid)

            mycursor.execute(f"SELECT `TEXT_practice` FROM `practice` WHERE ID_practice = {practiceid} ")
            myresult = str(mycursor.fetchone()[0])
            bot.send_message (message.chat.id, myresult)
            mycursor.close()

except Exception as e:
    print('ошибка')

bot.polling()
