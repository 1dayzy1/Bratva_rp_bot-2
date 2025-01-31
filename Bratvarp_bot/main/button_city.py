import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('7305613783:AAHgY5UJeBwVJqu9WL9U3Ng26Ydz4li4PH8')


#Москва-центр клавиатура

def stret_vernad(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("Магазин одежды")
    btn5 = types.KeyboardButton("Мото салон")

    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Проспект Вернадского",reply_markup=markup)



def stret_mira(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("Риелторское агенство")
    btn5 = types.KeyboardButton("Авто салон")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Проспект Мира",reply_markup=markup)
    

def stret_tversk(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("🎰Казино")
    btn5 = types.KeyboardButton("🗂️Задания")
    btn6 = types.KeyboardButton("🛠️Работы")
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Тверская",reply_markup=markup)
    

def stret_shuhova(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("")
    btn5 = types.KeyboardButton("")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Шухова ",reply_markup=markup)
    

#Королев клавиатура


def street_lenin(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("🏦Банк")
    btn5 = types.KeyboardButton("")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Ленина ",reply_markup=markup)

 
def street_oct(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("Лагерь")
    btn5 = types.KeyboardButton("")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Октябрьская ",reply_markup=markup)
    

def street_rain(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("")
    btn5 = types.KeyboardButton("")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Раина ",reply_markup=markup)
    


#Чертаново клавиатура

def street_sumsk(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("Крайм")
    btn5 = types.KeyboardButton("")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Сумская ",reply_markup=markup)
    
    

def street_varsh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("Авто салон Mercedes ")
    btn5 = types.KeyboardButton("")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Варшвавское шоссе ",reply_markup=markup)
    
    
def street_chertanovskaya(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("")
    btn5 = types.KeyboardButton("")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Чертановская ",reply_markup=markup)
    
    
#Мытищи клавиатура

def street_yubileyn(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("Больница")
    btn5 = types.KeyboardButton("Штрафстоянка")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Юбилейная ",reply_markup=markup)
    

def street_borisovka(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("Шиномонтаж")
    btn5 = types.KeyboardButton("Secrets of happiness")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Борисовка ",reply_markup=markup)
    


def street_letnaya(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("ЖК")
    btn5 = types.KeyboardButton("ЗАГС")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Летная ",reply_markup=markup)
    


#Балашиха клавиатура

def street_razin(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("🏴Черный Рынок")
    btn5 = types.KeyboardButton("--")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Разина ",reply_markup=markup)


def street_victory(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("--")
    btn5 = types.KeyboardButton("--")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Победы ",reply_markup=markup)


def street_crups(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔑Личный кабинет")
    btn2 = types.KeyboardButton("✈️Отправиться в другой город")
    btn3 = types.KeyboardButton("🚍🚏Отправиться на остановку")
    btn4 = types.KeyboardButton("--")
    btn5 = types.KeyboardButton("--")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вы приехали на Ул.Крупской ",reply_markup=markup)
    