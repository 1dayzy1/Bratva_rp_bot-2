import telebot 
import sqlite3



bot = telebot.TeleBot('')



def home_econom(message):
    db_eco1 = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/econom1.db")
    cur_eco1 = db_eco1.cursor()

    db_eco2 = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/econom2.db")
    cur_eco2 = db_eco2.cursor()

    db_eco3 = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/econom3.db")
    cur_eco3 = db_eco3.cursor()

    cur_eco1.execute("SELECT home_num,price,owner_name,class_home FROM econom1")
    home_num,price,owner_name,class_home = cur_eco1.fetchone()
    cur_eco1.execute("SELECT city FROM econom1  ")
    city = cur_eco1.fetchone()[0]

    # Преобразование результата запроса в читаемый формат
        
    bot.send_message(message.chat.id, f"Номер дома:{home_num}\nДома класса:\n{class_home}\nЦена:{price}\nВладелец:{owner_name}\nГород:{city}")


    cur_eco2.execute("SELECT home_num,price,owner_name,class_home FROM econom2  ")
    home_num,price,owner_name,class_home = cur_eco2.fetchone()
    cur_eco2.execute("SELECT city FROM econom2 ")
    city = cur_eco2.fetchone()[0]

    # Преобразование результата запроса в читаемый формат
        
    bot.send_message(message.chat.id, f"Номер дома:{home_num}\nДома класса:\n{class_home}\nЦена:{price}\nВладелец:{owner_name}\nГород:{city}")


    cur_eco3.execute("SELECT home_num,price,owner_name,class_home FROM econom3  ")
    home_num,price,owner_name,class_home = cur_eco3.fetchone()
    cur_eco3.execute("SELECT city FROM econom3 ")
    city = cur_eco3.fetchone()[0]

    # Преобразование результата запроса в читаемый формат
        
    bot.send_message(message.chat.id, f"Номер дома:{home_num}\nДома класса:\n{class_home}\nЦена:{price}\nВладелец:{owner_name}\nГород:{city}")





def check_class_homes(message):
    db_eco1 = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/econom1.db")
    cur_eco1 = db_eco1.cursor()

   

    db_mid1 = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/middle1.db")
    cur_mid1 = db_mid1.cursor()
    

    class_home = message.text

    if class_home == "Эконом":
       home_econom(message)

    elif class_home == "Средний":
        cur_mid1.execute("SELECT price,owner_name,class_home FROM middle1")
        price,owner_name,class_home = cur_mid1.fetchone()
        cur_mid1.execute("SELECT city FROM middle1 ")
        city = cur_mid1.fetchone()[0]

    # Преобразование результата запроса в читаемый формат
        
        bot.send_message(message.chat.id, f"Дома класса :\n{class_home}\nЦена:{price}\nВладелец:{owner_name}\nГород:{city}")
        


    else:
        bot.send_message(message.chat.id,"Тильт")
