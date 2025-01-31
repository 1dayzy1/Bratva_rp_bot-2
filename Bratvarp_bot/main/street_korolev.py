import telebot
import sqlite3
import time
from button_city import street_lenin,street_oct,street_rain




bot = telebot.TeleBot('7305613783:AAHgY5UJeBwVJqu9WL9U3Ng26Ydz4li4PH8')

def street_korolev(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    user_street = message.text
    user_id = message.from_user.id
    cur.execute("SELECT user_street FROM users WHERE user_id = ?",(user_id,))
    users_stret = cur.fetchone()[0]
    valid_street = ["Ул.Ленина","Ул.Октябрьская","Ул.Раина"]

    if user_street == "Ул.Ленина":
        bot.send_message(message.chat.id,f"<b>Вы отправились на {user_street}</b>",parse_mode="html")
        time.sleep(4)
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",(user_street,user_id))
        db.commit()
        
        street_lenin(message)
        
    
    elif user_street == "Ул.Октябрьская":
        bot.send_message(message.chat.id,f"<b>Вы отправились на {user_street}</b>",parse_mode="html")
        time.sleep(4)
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",(user_street,user_id))
        db.commit()
        
        street_oct(message)
        
    

    elif user_street == "Ул.Раина":
        bot.send_message(message.chat.id,f"<b>Вы отправились на {user_street}</b>",parse_mode="html")
        time.sleep(4)
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",(user_street,user_id))
        db.commit()
        
        street_rain(message)
        
    
    elif user_street not in valid_street:
        bot.send_message(message.chat.id,"Такой улицы нет!")
        
    
    
    elif user_street == users_stret:
        bot.send_message(message.chat.id,"Вы и так здесь!)")
    
