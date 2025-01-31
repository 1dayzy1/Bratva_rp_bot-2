import telebot
import sqlite3
import time
from button_city import *
from telebot import types



bot = telebot.TeleBot('7305613783:AAHgY5UJeBwVJqu9WL9U3Ng26Ydz4li4PH8')



    
    



def street_moscows(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    user_streets = message.text
    user_id = message.from_user.id
    
    cur.execute("SELECT user_street FROM users WHERE user_id = ?",(user_id,))
    users_stret = cur.fetchone()[0]
    

    valid_streets = ["Проспект Вернадского","Проспект Мира","Ул.Тверская","Ул.Шухова"]

    if user_streets == "Проспект Вернадского":
        bot.send_message(message.chat.id,f"<b>Вы отправились на {user_streets}</b>",parse_mode="html")
        time.sleep(3)
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",(user_streets,user_id))
        db.commit()
        stret_vernad(message)
        
    
    elif user_streets == "Проспект Мира":
        bot.send_message(message.chat.id,f"<b>Вы отправились на {user_streets}</b>",parse_mode="html")
        time.sleep(3)
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",(user_streets,user_id))
        db.commit()
        stret_mira(message)
    

    elif user_streets == "Ул.Тверская":
        bot.send_message(message.chat.id,f"<b>Вы отправились на {user_streets}</b>",parse_mode="html")
        time.sleep(3)
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",(user_streets,user_id))
        db.commit()
        stret_tversk(message)
    
    elif user_streets == "Ул.Шухова":
        bot.send_message(message.chat.id,f"<b>Вы отправились на {user_streets}</b>",parse_mode="html")
        time.sleep(3)
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",(user_streets,user_id))
        db.commit()
        stret_shuhova(message)

    elif user_streets == users_stret:
        bot.send_message(message.chat.id,"Ты и так тут!")
    elif user_streets not in valid_streets:
        bot.send_message(message.chat.id,"Такой улицы нет")

        
   
    
