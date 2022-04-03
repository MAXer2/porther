import telebot
import random
import string
import requests
import json
import sqlite3
from telebot import types
from array import *
import re
import mysql.connector
from mysql.connector import MySQLConnection, Error


bot = telebot.TeleBot('5220512547:AAECT9QpvjemKadgn-ftJhnyefOymD2IF8I')


mydb = mysql.connector.connect(
  host="a0655204.xsph.ru",
  user="a0655204_castaneda",
  password="castaneda123$$$",
  database="a0655204_castaneda"
)


def main():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('Добавить фразу')
    key2 = types.KeyboardButton('Удалить фразу')
    markup.add(key1, key2)
    return markup

def sec():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('Отмена')
    markup.add(key1)
    return markup




def lea():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('Знание')
    key2 = types.KeyboardButton('Практика')
    key3 = types.KeyboardButton('Сила')
    markup.add(key1, key2, key3)
    return markup


def delete():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('/Знание')
    key2 = types.KeyboardButton('/Практика')
    key3 = types.KeyboardButton('/Сила')
    markup.add(key1, key2, key3)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == 967453280 or message.from_user.id == 341548875:
        bot.send_message(message.chat.id, f'''✨ Привет, {message.from_user.first_name}
Я bot-updater castaneda''', reply_markup=main())
    else:
    return


@bot.message_handler(content_types=['text'])

def firstmenu(message):
    if message.text == 'Добавить фразу':
        bot.send_message (message.chat.id, 'Выберите таблицу', reply_markup= lea())
        bot.register_next_step_handler(message, secondmenu)

    if message.text == 'Удалить фразу':
        bot.send_message (message.chat.id, 'Выберите таблицу', reply_markup= delete())
        bot.register_next_step_handler(message, secondmenu)



def secondmenu(message):

    if message.text == 'Знание':
        bot.send_message (message.chat.id, 'Введите текст', reply_markup= sec())
        bot.register_next_step_handler(message, knowlege)

    if message.text == 'Практика':
        bot.send_message (message.chat.id, 'Введите текст', reply_markup= sec())
        bot.register_next_step_handler(message, practice)


    if message.text == 'Сила':
        bot.send_message (message.chat.id, 'Введите текст', reply_markup= sec())
        bot.register_next_step_handler(message, power)


    if message.text == '/Знание':
        bot.send_message (message.chat.id, 'Введите ID', reply_markup= sec())
        bot.register_next_step_handler(message, knowlegedel)

    if message.text == '/Практика':
        bot.send_message (message.chat.id, 'Введите ID', reply_markup= sec())
        bot.register_next_step_handler(message, practicedel)


    if message.text == '/Сила':
        bot.send_message (message.chat.id, 'Введите ID', reply_markup= sec())
        bot.register_next_step_handler(message, powerdel)

    if message.text == 'Отмена':
        bot.send_message (message.chat.id, 'Отмена', reply_markup= main())


def knowlege(message):

    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT Count(ID) FROM `says` ")
    currentid = int(mycursor.fetchone()[0]) + 1

    sql = "INSERT INTO says (ID, TEXT) VALUES (%s, %s)"
    val = (currentid, message.text)
    mycursor.execute(sql, val)
    mydb.commit()
    bot.send_message (message.chat.id, f'''Добавил в базу, ID записи = {currentid}''', reply_markup= main())
    mycursor.close()


def practice(message):

    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT Count(ID_practice) FROM `practice` ")
    currentid = int(mycursor.fetchone()[0]) + 1

    sql = "INSERT INTO power (ID_practice, TEXT_practice) VALUES (%s, %s)"
    val = (currentid, message.text)

    mycursor.execute(sql, val)
    mydb.commit()

    bot.send_message (message.chat.id, f'''Добавил в базу, ID записи = {currentid}''', reply_markup= main())
    mycursor.close()


def power(message):

    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT Count(ID_power) FROM `power` ")
    currentid = int(mycursor.fetchone()[0]) + 1

    sql = "INSERT INTO power (ID_power, TEXT_power) VALUES (%s, %s)"
    val = (currentid, message.text)

    mycursor.execute(sql, val)
    mydb.commit()

    bot.send_message (message.chat.id, f'''Добавил в базу, ID записи = {currentid}''', reply_markup= main())
    mycursor.close()



def knowlegedel(message):
    mycursor = mydb.cursor()
    deleteid = int(message.text)
    mycursor.execute(f'''DELETE FROM says WHERE ID = {deleteid}''')
    bot.send_message (message.chat.id, f'''Удалил ID {deleteid} из базы''', reply_markup= main())
    mycursor.close()
    mydb.commit()


def practicedel(message):

    mycursor = mydb.cursor()
    deleteid = int(message.text)
    mycursor.execute(f'''DELETE FROM practice WHERE ID_practice = {deleteid}''')
    bot.send_message (message.chat.id, f'''Удалил ID {deleteid} из базы''', reply_markup= main())
    mycursor.close()
    mydb.commit()



def powerdel(message):

    mycursor = mydb.cursor()
    deleteid = int(message.text)
    mycursor.execute(f'''DELETE FROM power WHERE ID_power = {deleteid}''')
    bot.send_message (message.chat.id, f'''Удалил ID {deleteid} из базы''', reply_markup= main())
    mycursor.close()
    mydb.commit()




bot.polling()
