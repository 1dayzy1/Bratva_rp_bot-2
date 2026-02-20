import telebot
import sqlite3
import time

from button_city import *

bot = telebot.TeleBot('')

def street_mytischis(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database//users.db")
    cur = db.cursor()
    user_street = message.text
    user_id = message.from_user.id
    cur.execute("SELECT user_street FROM users WHERE user_id = ?",(user_id,))
    users_stret = cur.fetchone()[0]

    valid_street = ["Ул.Юбилейная","Ул.Борисовка","Ул.Летная"]

    if user_street == "Ул.Юбилейная":
        bot.send_message(message.chat.id,f"<b>Вы отправились на {user_street}</b>",parse_mode="html")
        time.sleep(4)
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",(user_street,user_id))
        db.commit()
        
        street_yubileyn(message)
        
    
    elif user_street == "Ул.Борисовка":
        bot.send_message(message.chat.id,f"<b>Вы отправились на {user_street}</b>",parse_mode="html")
        time.sleep(4)
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",(user_street,user_id))
        db.commit()
        
        street_borisovka(message)
        
    

    elif user_street == "Ул.Летная":
        bot.send_message(message.chat.id,f"<b>Вы отправились на {user_street}</b>",parse_mode="html")
        time.sleep(4)
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",(user_street,user_id))
        db.commit()
       
        street_letnaya(message)
        
    
    elif user_street not in valid_street:
        bot.send_message(message.chat.id,"Такой улицы нет!")
        
    
    
    elif user_street == users_stret:
        bot.send_message(message.chat.id,"Вы и так здесь!)")
    
