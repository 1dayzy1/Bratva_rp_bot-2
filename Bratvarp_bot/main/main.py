import telebot
import sqlite3
from telebot import types
import time
import random
from button_city import *
from street_moscows import street_moscows
from street_korolev import street_korolev
from street_chertanovo import street_chertanovo
from street_mytischi import street_mytischis
from street_balashiha import street_balash
from check_class_home import check_class_homes,home_econom
import appartaments_mytishi



bot = telebot.TeleBot('7305613783:AAHgY5UJeBwVJqu9WL9U3Ng26Ydz4li4PH8')



order_active = False
order_active_bus = False


answer = ""
test_ball = 0

protocols = ""



people_dtp = [
    "Я ехал на велосипеде по тротуару, когда меня сбил автомобиль.  Я упал, у меня ушибы, но, кажется, ничего серьезного...  Водитель остался на месте, он сказал, что позвонит в скорую",
    "Я шла по пешеходному переходу на зеленый свет, но меня сбила машина, которая проехала на красный!  Я получила сильные ушибы, мне нужна помощь.",
    "Я ехал на мотоцикле, когда в меня врезался автомобиль, который не заметил меня. У меня сильные боли в спине и руке, мне нужна срочная госпитализация"   
]





people = [
    {
        "name": "Иванов Иван Иванович",
        "birthdate": "1985-03-15",
        "city": "Москва",
    },
    {
        "name": "Петрова Мария Сергеевна",
        "birthdate": "1992-07-28",
        "city": "Санкт-Петербург",
    },
    {
        "name": "Козлова Елена Владимировна",
        "birthdate": "1989-05-12",
        "city": "Краснодар",
    },
    {
        "name": "Смирнов Дмитрий Алексеевич",
        "birthdate": "1981-09-21",
        "city": "Новосибирск",
    },
    {
        "name": "Кузнецова Анна Павловна",
        "birthdate": "1995-01-18",
        "city": "Челябинск",
    },
    {
        "name": "Соколов Сергей Викторович",
        "birthdate": "1976-06-03",
        "city": "Нижний Новгород",
    },
    {
        "name": "Попова Татьяна Александровна",
        "birthdate": "1990-10-25",
        "city": "Красноярск",
    },
    {
        "name": "Васильева Ирина Николаевна",
        "birthdate": "1997-08-08",
        "city": "Воронеж",
    },
    {
        "name": "Сидоров Александр Николаевич",
        "birthdate": "1978-11-04",
        "city": "Екатеринбург",
    },
]

wanted_people = [
    {
        "name": "Сидоров Александр Николаевич",
        "birthdate": "1978-11-04",
        "city": "Екатеринбург",
    },
    {
        "name": "Борисов Михаил Дмитриевич",
        "birthdate": "1983-02-10",
        "city": "Пермь",
    }
]





car_ugon = [
    {
        "photo" :"/Users/dayzy/Desktop/Bratva_mac/main/cars/clsblack.jpg ",
        "Marka":"Mercedes",
        "Color":"Black",
        "Number":"м710ут82"
    },
{
        "photo" :"/Users/dayzy/Desktop/Bratva_mac/main/cars/m5f90.jpg ",
        "Marka":"Bmw",
        "Color":"Black",
        "Number":"м400oх82"
    },
{
        "photo" :"/Users/dayzy/Desktop/Bratva_mac/main/cars/z4.jpg ",
        "Marka":"BMW",
        "Color":"Black",
        "Number":"м666ну124"
    }
]
car_def = [
    "/Users/dayzy/Desktop/Bratva_mac/main/cars/m5f90.jpg",
    "/Users/dayzy/Desktop/Bratva_mac/main/cars/z4.jpg",
    "/Users/dayzy/Desktop/Bratva_mac/main/cars/clsblack.jpg",
    "/Users/dayzy/Desktop/Bratva_mac/main/cars/alfa.jpg",
    "/Users/dayzy/Desktop/Bratva_mac/main/cars/porshe.jpg",
    "/Users/dayzy/Desktop/Bratva_mac/main/cars/toyta.jpg"
    ]

def send_city_photo(message, city):
    # Замените эти пути на реальные пути к вашим фотографиям
    photo_paths = {
        "Moscow-center": "main/photo/moscow_center.jpeg",

        # Добавьте пути к фотографиям других городов
    }

    if city in photo_paths:
        with open(photo_paths[city], 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat,id, f"Фото для города {city} не найдено попробуйте позже(")






@bot.message_handler(commands=['start'])
def start(message):
    global us
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    message_code = message.text.split()

    appartaments_mytishi
    db = sqlite3.connect('C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db')
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        user_name TEXT,
        user_city TEXT,
        user_money INTEGER DEFAULT 0,
        work_lvl INTEGER DEFAULT 0,
        work_lvl_bus INTEGER DEFAULT 0,
        check_sub  DEFAULT 0,
        check_channel  DEFAULT 0,
        referrals INTEGER DEFAULT 0,
        refer_by INTEGER DEFAULT 0,
        work TEXT DEFAULT 'Без работы',
        work_police INTEGER DEFAULT 0,
        work_police_check INTEGER DEFAULT 0,
        user_street TEXT,
        bank_score INTEGER DEFAULT 0
        

    )""")
    db.commit()
    cur.execute("SELECT user_city FROM users WHERE user_id = ?",(user_id,))
    user_city_work = cur.fetchone()
    # Проверяем, есть ли уже пользователь в базе данных
    cur.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
    user_exists = cur.fetchone()
    
    
    
    if user_exists:
        check_city(message)


   


    else:
        if len(message_code)>1:
            ref_code = message_code[1]
            if ref_code.isdigit():
                ref_code = int(ref_code)
                cur.execute("SELECT * FROM users")
                users = cur.fetchall()
                user_ids = users[0] if users else None 
                if ref_code in user_ids:
                    
                    cur.execute("UPDATE users SET user_money = user_money + 10000 WHERE user_id = ?",(ref_code,))
                    db.commit() 


                    cur.execute("UPDATE users SET refer_by = refer_by + 1 WHERE user_id = ? ",(user_id,))
                    db.commit()


                    cur.execute("UPDATE users SET referrals = referrals + 1 WHERE user_id = ?",(ref_code,))
                    db.commit()
                    
                    cur.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
                    db.commit()

                    markup = types.InlineKeyboardMarkup(row_width=3)
                    btn1 = types.InlineKeyboardButton(text="Москва-центр", callback_data="Москва-центр")
                    btn2 = types.InlineKeyboardButton(text="Королёв", callback_data="Королёв")
                    btn3 = types.InlineKeyboardButton(text="Чертаново", callback_data="Чертаново")
                    btn4 = types.InlineKeyboardButton(text="Мытищи", callback_data="Мытищи")
                    btn5 = types.InlineKeyboardButton(text="Балашиха", callback_data="Балашиха")
                    btn6 = types.InlineKeyboardButton(text="Люберцы", callback_data="Люберцы")
                    btn7 = types.InlineKeyboardButton(text="Видное", callback_data="Видное")
                    btn8 = types.InlineKeyboardButton(text="Химки", callback_data="Химки")
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
                    bot.send_message(ref_code,"По вашей ссылке зарегистрировался человек:)\n Бонус уже вам зачислен")
                    bot.send_message(chat_id, f"*Приветствую тебя {message.from_user.first_name} {message.from_user.last_name} ты стал рефералом и можешь получить свой бонус в личном кабинете!\n\nЭто игра про реальную Москву и ее областные города.\nЗдесь ты можешь быть как на стороне закона, так и на стороне бандитизма.\nВыбор за тобой:)\n\nА сейчас выбери город, в котором ты хочешь начать развиваться*", reply_markup=markup,parse_mode='Markdown')
                    
                else:
                    bot.send_message(message.chat.id,"Вас нет в базе")
            else:
    

                bot.send_message(message.chat.id,"Неверный код")
        else:
            cur.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
            db.commit()
            markup = types.InlineKeyboardMarkup(row_width=3)
            btn1 = types.InlineKeyboardButton(text="Москва-центр", callback_data="Москва-центр")
            btn2 = types.InlineKeyboardButton(text="Королёв", callback_data="Королёв")
            btn3 = types.InlineKeyboardButton(text="Чертаново", callback_data="Чертаново")
            btn4 = types.InlineKeyboardButton(text="Мытищи", callback_data="Мытищи")
            btn5 = types.InlineKeyboardButton(text="Балашиха", callback_data="Балашиха")
            btn6 = types.InlineKeyboardButton(text="Люберцы", callback_data="Люберцы")
            btn7 = types.InlineKeyboardButton(text="Видное", callback_data="Видное")
            btn8 = types.InlineKeyboardButton(text="Химки", callback_data="Химки")
            markup.add(btn1, btn2, btn3, btn4, btn5,)

            bot.send_message(chat_id, f"*Приветствую тебя {message.from_user.first_name} {message.from_user.last_name}!\n\nЭто игра про реальную Москву и ее областные города.\nЗдесь ты можешь быть как на стороне закона, так и на стороне бандитизма.\nВыбор за тобой:)\n\nА сейчас выбери город, в котором ты хочешь начать развиваться*", reply_markup=markup,parse_mode='Markdown')
        
        db.close()





@bot.callback_query_handler(func=lambda call:True)
def city(call):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    global city
    city = call.data
    user_id = call.from_user.id


    cur.execute(f"UPDATE users SET user_city = ? WHERE user_id = ?", (city, user_id))
    db.commit()

    bot.send_message(call.message.chat.id, "Введите ваше имя")
    bot.register_next_step_handler(call.message, get_name)
    
    db.close()



def get_name(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()

    name = message.text
    user_id = message.from_user.id

    cur.execute("UPDATE users SET user_name = ? WHERE user_id = ?",(name,user_id))
    db.commit()
    cur.execute("SELECT user_city FROM users WHERE user_id = ?",(user_id,))
    user_city = cur.fetchone()
    bot.send_message(message.chat.id, "⏳")
    bot.send_message(message.chat.id,"*Происходит регистрация....*",parse_mode='Markdown')
    #send_city_photo(message,user_city)
    time.sleep(3)
    
    if city == "Москва-центр":
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",("Ул.Тверская",user_id,))
        db.commit()

    elif city == "Королёв":
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",("Ул.Ленина",user_id,))
        db.commit()

    elif city == "Чертаново":
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",("Ул.Чертановская",user_id,))
        db.commit()

    elif city == "Мытищи":
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",("Ул.Летная",user_id,))
        db.commit()


    check_city(message)
  






@bot.message_handler(content_types=['text'])
def reaction_on_message(message):
    global order_active
    global order_active_bus
    user_id = message.from_user.id
    admin_id = 1205083192
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    taxi_phrase = [
        "Новый заказ!",
        "Появился заказ!",
        "Отлично! Новый заказ!",
        "Поехали! Новый заказ ждет!",
        "Отличная возможность заработать! Новый заказ! "
    ]
    random_taxi_phrase = random.choice(taxi_phrase)
    money_phrase = [
        "Оплата за заказ получена!",
        "Деньги за заказ на вашем счету!",
        "Заказ оплачен!",
        "Оплата поступила!",
        "Поздравляем! Заработок за поездку  доступен!",
        "Спасибо за поездку! Оплата за заказ  уже на вашем счету."
    ]
    random_phrase_money = random.choice(money_phrase)
    bus_phrase = [
        "В путь! Маршрут начался!",
        "Двери закрываются, отправляемся!",
        "Поехали! Добро пожаловать на борт!",
        "Пристегните ремни, мы отправляемся!",
        ""
    ]
    random_bus_phrase = random.choice(bus_phrase)
    money_phrase_bus = [
        "Оплата за маршрут  начислена!",
        "Поздравляем! Заработок за маршрут  доступен!",
        "Вы успешно получили оплату за маршрут !",
        "Деньги за маршрут получены!",
        "Ваши деньги за маршрут на вашем счету! "

    ]
    random_bus_money = random.choice(money_phrase_bus)
    cur.execute("SELECT refer_by FROM users WHERE user_id = ?",(user_id,))
    ref_by = cur.fetchone()[0]

    cur.execute("SELECT work_police FROM users WHERE user_id = ?",(user_id,))
    work_police = cur.fetchone()[0]

    cur.execute("SELECT work_police_check FROM users WHERE user_id = ?",(user_id,))
    work_check = cur.fetchone()[0]
    
    
    cur.execute("SELECT user_city FROM users WHERE user_id = ?",(user_id,))
    user_city_work = cur.fetchone()[0]

    cur.execute("SELECT check_sub FROM users WHERE user_id = ?",(user_id,))
    check_sub = cur.fetchone()[0]

    cur.execute("SELECT work_lvl FROM users WHERE user_id = ?",(user_id,))
    taxi = cur.fetchone()[0]

    cur.execute("SELECT work_lvl_bus FROM users WHERE user_id = ?",(user_id,))
    bus = cur.fetchone()[0]

    cur.execute("SELECT user_city FROM users WHERE user_id = ?",(user_id,))
    user_city = cur.fetchone()[0]

    cur.execute("SELECT referrals FROM users WHERE user_id = ?",(user_id,))
    referals = cur.fetchone()[0]

    cur.execute("SELECT user_city FROM users WHERE user_id = ?",(user_id,))
    users_ciity = cur.fetchone()[0]

    cur.execute("SELECT check_channel FROM users WHERE user_id = ?",(user_id,))
    check_channel = cur.fetchone()[0]

    cur.execute("SELECT user_street FROM users WHERE user_id = ?",(user_id,))
    users_stret = cur.fetchone()[0]

    cur.execute("SELECT bank_score FROM users WHERE user_id = ?",(user_id,))
    bank_score = cur.fetchone()[0]

    if message.text == "🛠️Работы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Такси🚕")
        btn2 = types.KeyboardButton("Водитель автобуса🚌")
        btn3 = types.KeyboardButton("Полиция👮‍♀️")
        btn4 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id, "Выберите кем вы хотите работать",reply_markup=markup)

    

    elif message.text == "Такси🚕":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать работу🚕")
        btn2 = types.KeyboardButton("О работе🚕")
        btn3 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id, "Ты выбрал работу таксиста",reply_markup=markup)


    elif message.text == "🔙Назад":
        check_city(message)


    elif message.text == "О работе🚕" and user_city_work == "Москва-центр":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Ты выбрал работу таксиста🚕\nЗаработок за одну поездку в твоем городе:650р\nОписаие работы:Придумать описание")


    elif message.text == "О работе🚕" and user_city_work == "Королёв":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Ты выбрал работу таксиста🚕\nЗаработок за одну поездку в твоем городе:250р\nОписаие работы:Придумать описание")


    elif message.text == "О работе🚕" and user_city_work == "Химки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Ты выбрал работу таксиста🚕\nЗаработок за одну поездку в твоем городе:350р\nОписаие работы:Придумать описание")


    elif message.text == "О работе🚕" and user_city_work == "Чертаново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Ты выбрал работу таксиста🚕\nЗаработок за одну поездку в твоем городе:400р\nОписаие работы:Придумать описание")


    elif message.text == "О работе🚕" and user_city_work == "Мытищи":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Ты выбрал работу таксиста🚕\nЗаработок за одну поездку в твоем городе:450р\nОписаие работы:Придумать описание")


    elif message.text == "О работе🚕" and user_city_work == "Балашиха":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Ты выбрал работу таксиста🚕\nЗаработок за одну поездку в твоем городе:200р\nОписаие работы:Придумать описание")


    elif message.text == "О работе🚕" and user_city_work == "Видное":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Ты выбрал работу таксиста🚕\nЗаработок за одну поездку в твоем городе:325р\nОписаие работы:Придумать описание")


    elif message.text == "О работе🚕" and user_city_work == "Люберцы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Ты выбрал работу таксиста🚕\nЗаработок за одну поездку в твоем городе:150р\nОписаие работы:Придумать описание")








    elif message.text == "Начать работу🚕" and user_city_work == "Химки":

        if order_active:
            bot.send_message(message.chat.id,"У вас есть заказ!")
        else:
            order_active = True
            bot.send_message(message.chat.id, f"{random_taxi_phrase}")
            time.sleep(10)
            order_active = False
            cur.execute("UPDATE users SET user_money = user_money + 350 WHERE user_id = ?", (user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl = work_lvl + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id,f"{random_phrase_money}\nНа вашем счету:{money:,}")












    elif message.text == "Начать работу🚕" and user_city_work == "Москва-центр":
        if order_active:
            bot.send_message(message.chat.id,"У вас есть заказ!")
        else:
            order_active = True
            bot.send_message(message.chat.id, f"{random_taxi_phrase}")
            time.sleep(5)
            order_active = False
            cur.execute("UPDATE users SET user_money = user_money + 650 WHERE user_id = ?", (user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl = work_lvl + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id,f"{random_phrase_money}\nНа вашем счету:{money:,}")







    elif message.text == "Начать работу🚕" and user_city_work == "Королёв":
        if order_active:
            bot.send_message(message.chat.id,"У вас есть заказ!")
        else:
            order_active = True
            bot.send_message(message.chat.id, f"{random_taxi_phrase}")
            time.sleep(10)
            order_active = False
            cur.execute("UPDATE users SET user_money = user_money + 250 WHERE user_id = ?", (user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl = work_lvl + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id,f"{random_phrase_money}\nНа вашем счету:{money:,}")



    elif message.text == "Начать работу🚕" and user_city_work == "Чертаново":
        if order_active:
            bot.send_message(message.chat.id,"У вас есть заказ!")
        else:
            order_active = True
            bot.send_message(message.chat.id, f"{random_taxi_phrase}")
            time.sleep(10)
            order_active = False
            cur.execute("UPDATE users SET user_money = user_money + 400 WHERE user_id = ?", (user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl = work_lvl + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id,f"{random_phrase_money}\nНа вашем счету:{money:,}")





    elif message.text == "Начать работу🚕" and user_city_work == "Мытищи":
        if order_active:
            bot.send_message(message.chat.id,"У вас есть заказ!")
        else:
            order_active = True
            bot.send_message(message.chat.id, f"{random_taxi_phrase}")
            time.sleep(10)
            order_active = False
            cur.execute("UPDATE users SET user_money = user_money + 450 WHERE user_id = ?", (user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl = work_lvl + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id,f"{random_phrase_money}\nНа вашем счету:{money:,}")


    elif message.text == "Начать работу🚕" and user_city_work == "Балашиха":
        if order_active:
            bot.send_message(message.chat.id,"У вас есть заказ!")
        else:
            order_active = True
            bot.send_message(message.chat.id, f"{random_taxi_phrase}")
            time.sleep(10)
            order_active = False
            cur.execute("UPDATE users SET user_money = user_money + 220 WHERE user_id = ?", (user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl = work_lvl + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id,f"{random_phrase_money}\nНа вашем счету:{money:,}")



    elif message.text == "Начать работу🚕" and user_city_work == "Видное":
        if order_active:
            bot.send_message(message.chat.id,"У вас есть заказ!")
        else:
            order_active = True
            bot.send_message(message.chat.id, f"{random_taxi_phrase}")
            time.sleep(10)
            order_active = False
            cur.execute("UPDATE users SET user_money = user_money + 325 WHERE user_id = ?", (user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl = work_lvl + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id,f"{random_phrase_money}\nНа вашем счету:{money:,}")




    elif message.text == "Начать работу🚕" and user_city_work == "Люберцы":
        if order_active:
            bot.send_message(message.chat.id,"У вас есть заказ!")
        else:
            order_active = True
            bot.send_message(message.chat.id, f"{random_taxi_phrase}")
            time.sleep(10)
            order_active = False
            cur.execute("UPDATE users SET user_money = user_money + 150 WHERE user_id = ?", (user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl = work_lvl + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id,f"{random_phrase_money}\nНа вашем счету:{money:,}")





    elif message.text == "Водитель автобуса🚌":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать работу🚌")
        btn2 = types.KeyboardButton("О работе🚌")
        btn3 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,"Ты выбрал работу водителя автобуса",reply_markup=markup)


    elif message.text == "О работе🚌" and user_city_work == "Москва-центр":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, f"Ты выбрал работу водителя автобуса\nОплата за маршут в твоем городе составляет:1000р",reply_markup=markup)



    elif message.text == "О работе🚌" and user_city_work == "Королёв":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, f"Ты выбрал работу водителя автобуса\nОплата за маршут в твоем городе составляет:500р",reply_markup=markup)


    elif message.text == "О работе🚌" and user_city_work == "Чертаново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, f"Ты выбрал работу водителя автобуса\nОплата за маршут в твоем городе составляет:750р",reply_markup=markup)


    elif message.text == "О работе🚌" and user_city_work == "Мытищи":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, f"Ты выбрал работу водителя автобуса\nОплата за маршут в твоем городе составляет:550р",reply_markup=markup)


    elif message.text == "О работе🚌" and user_city_work == "Балашиха":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, f"Ты выбрал работу водителя автобуса\nОплата за маршут в твоем городе составляет:300р",reply_markup=markup)


    elif message.text == "О работе🚌" and user_city_work == "Люберцы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, f"Ты выбрал работу водителя автобуса\nОплата за маршут в твоем городе составляет:150р",reply_markup=markup)


    elif message.text == "О работе🚌" and user_city_work == "Видное":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, f"Ты выбрал работу водителя автобуса\nОплата за маршут в твоем городе составляет:250р",reply_markup=markup)


    elif message.text == "О работе🚌" and user_city_work == "Химки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id, f"Ты выбрал работу водителя автобуса\nОплата за маршут в твоем городе составляет:50р",reply_markup=markup)




    elif message.text == "Начать работу🚌" and user_city_work == "Москва-центр":
        if order_active_bus:
            bot.send_message(message.chat.id, "Вы уже начали маршрут!")
        else:
            order_active_bus = True

            bot.send_message(message.chat.id, f"Ты начал маршрут по городу {user_city_work}\nОплата в этом городе составляет:1000р")
            time.sleep(5)
            order_active_bus = False
            cur.execute("UPDATE users SET user_money = user_money + 1000 WHERE user_id = ? ",(user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl_bus = work_lvl_bus + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id, f"{random_bus_money}\nНа вашем счету: {money:,}")


    elif message.text == "Начать работу🚌" and user_city_work == "Королёв":
        if order_active_bus:
            bot.send_message(message.chat.id, "Вы уже начали маршрут!")
        else:
            order_active_bus = True

            bot.send_message(message.chat.id, f"Ты начал маршрут по городу {user_city_work}\nОплата в этом городе составляет:1000р")
            time.sleep(5)
            order_active_bus = False
            cur.execute("UPDATE users SET user_money = user_money + 500 WHERE user_id = ? ",(user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl_bus = work_lvl_bus + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id, f"{random_bus_money}\nНа вашем счету: {money:,}")


    elif message.text == "Начать работу🚌" and user_city_work == "Чертаново":
        if order_active_bus:
            bot.send_message(message.chat.id, "Вы уже начали маршрут!")
        else:
            order_active_bus = True

            bot.send_message(message.chat.id, f"Ты начал маршрут по городу {user_city_work}\nОплата в этом городе составляет:1000р")
            time.sleep(5)
            order_active_bus = False
            cur.execute("UPDATE users SET user_money = user_money + 750 WHERE user_id = ? ",(user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl_bus = work_lvl_bus + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id, f"{random_bus_money}\nНа вашем счету: {money:,}")


    elif message.text == "Начать работу🚌" and user_city_work == "Мытищи":
        if order_active_bus:
            bot.send_message(message.chat.id, "Вы уже начали маршрут!")
        else:
            order_active_bus = True

            bot.send_message(message.chat.id, f"Ты начал маршрут по городу {user_city_work}\nОплата в этом городе составляет:1000р")
            time.sleep(5)
            order_active_bus = False
            cur.execute("UPDATE users SET user_money = user_money + 550 WHERE user_id = ? ",(user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl_bus = work_lvl_bus + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id, f"{random_bus_money}\nНа вашем счету: {money:,}")


    elif message.text == "Начать работу🚌" and user_city_work == "Балашиха":
        if order_active_bus:
            bot.send_message(message.chat.id, "Вы уже начали маршрут!")
        else:
            order_active_bus = True

            bot.send_message(message.chat.id, f"Ты начал маршрут по городу {user_city_work}\nОплата в этом городе составляет:1000р")
            time.sleep(5)
            order_active_bus = False
            cur.execute("UPDATE users SET user_money = user_money + 300 WHERE user_id = ? ",(user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl_bus = work_lvl_bus + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id, f"{random_bus_money}\nНа вашем счету: {money:,}")


    elif message.text == "Начать работу🚌" and user_city_work == "Люберцы":
        if order_active_bus:
            bot.send_message(message.chat.id, "Вы уже начали маршрут!")
        else:
            order_active_bus = True

            bot.send_message(message.chat.id, f"Ты начал маршрут по городу {user_city_work}\nОплата в этом городе составляет:1000р")
            time.sleep(5)
            order_active_bus = False
            cur.execute("UPDATE users SET user_money = user_money + 150 WHERE user_id = ? ",(user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl_bus = work_lvl_bus + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id, f"{random_bus_money}\nНа вашем счету: {money:,}")


    elif message.text == "Начать работу🚌" and user_city_work == "Видное":
        if order_active_bus:
            bot.send_message(message.chat.id, "Вы уже начали маршрут!")
        else:
            order_active_bus = True

            bot.send_message(message.chat.id, f"Ты начал маршрут по городу {user_city_work}\nОплата в этом городе составляет:1000р")
            time.sleep(5)
            order_active_bus = False
            cur.execute("UPDATE users SET user_money = user_money + 250 WHERE user_id = ? ",(user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl_bus = work_lvl_bus + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id, f"{random_bus_money}\nНа вашем счету: {money:,}")


    elif message.text == "Начать работу🚌" and user_city_work == "Химки":
        if order_active_bus:
            bot.send_message(message.chat.id, "Вы уже начали маршрут!")
        else:
            order_active_bus = True

            bot.send_message(message.chat.id, f"Ты начал маршрут по городу {user_city_work}\nОплата в этом городе составляет:1000р")
            time.sleep(5)
            order_active_bus = False
            cur.execute("UPDATE users SET user_money = user_money + 50 WHERE user_id = ? ",(user_id,))
            db.commit()
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            money = cur.fetchone()[0]
            cur.execute("UPDATE users SET work_lvl_bus = work_lvl_bus + 1 WHERE user_id = ?",(user_id,))
            db.commit()
            bot.send_message(message.chat.id, f"{random_bus_money}\nНа вашем счету: {money:,}")



    elif message.text == '/menu' :
        check_city(message)


    



    elif message.text == "🔑Личный кабинет" or message.text == "/account":
        cur.execute("SELECT user_money,user_name,user_city,work FROM users WHERE user_id = ?",(user_id,))
        user_data = cur.fetchone()
        cur.execute("SELECT user_street FROM users WHERE user_id = ?",(user_id,))
        user_street = cur.fetchone()[0]
        user_money,user_name,user_city,work = user_data
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Реферальная ссылка")
        btn3 = types.KeyboardButton("🎁Получить бонус")
        btn4 = types.KeyboardButton("🔄Сменить имя")
        btn2 = types.KeyboardButton("🔙Назад")
        btn5 = types.KeyboardButton("🏘️Имущество")
        markup.add(btn1,btn3,btn4,btn5,btn2)
        bot.send_message(message.chat.id, f"🔐Личный кабинет:\n 👤Твой ник:{user_name}\n 🆔Твой ID:{user_id}\n 💵На руках:{user_money:,}₽\n🏦В банке:{bank_score:,}₽\n🏙️Ты в: {user_city}, На {user_street} \n 🚕Заказов на такси: {taxi}\n 🚌Рейсов на автобусе: {bus}\nМесто работы: {work}",reply_markup=markup)

    elif message.text == "🔄Сменить имя":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id,"Смена имени стоит 15.000р если вы согласны введите имя:",reply_markup=markup)
        bot.register_next_step_handler(message,new_name)
        
    elif message.text == "🗂️Задания" and check_sub < 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton(text="Проверить✅")
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn2,btn1)
        bot.send_message(message.chat.id,"📚*Твое задание*:\n\nПодпишись на наш телеграмм канал\n\n🏆 *награда:\n\n 💲20.000₽*\nhttps://t.me/Bratvarpchannel",reply_markup=markup,parse_mode='Markdown')
        
    elif message.text == "🗂️Задания" and check_sub == 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Проверить🚕")
        btn2 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,"📚*Твое задание*:\n\n Выполните 20 заказов на такси\n\n🏆 *награда:\n\n 💲20.000₽* ",reply_markup=markup,parse_mode='Markdown')
    
    elif message.text == "🎁Получить бонус" and ref_by == 1 :
        
        cur.execute("UPDATE users SET user_money = user_money + 10000 WHERE user_id = ?",(user_id,))
        db.commit()

        cur.execute("UPDATE users SET refer_by = refer_by - 1 WHERE user_id = ? ",(user_id,))
        db.commit()


        bot.send_message(user_id,"Вы получили бонус за то что стали чьим-то рефералом")
        check_city(message)
    elif message.text == "🎁Получить бонус" and ref_by != 1:
        bot.send_message(user_id,"У вас нет бонусов(")
    
    elif message.text == "Реферальная ссылка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        ref_link = f"https://t.me/BratvaRPbot?start={user_id}"
        bot.send_message(message.chat.id,f"За каждого приглашенного пользователя вы и пришлашенный человек получат 10.000₽\nТвоя реферальная ссылка: {ref_link}\nТвои рефералы:{referals:,}",reply_markup=markup)

    






    elif message.text == "Проверить🚕" and taxi >= 20 :
        cur.execute("UPDATE users SET user_money = user_money + 20000 WHERE user_id = ?",(user_id,))
        db.commit()
        cur.execute("UPDATE users SET check_sub = check_sub + 1 WHERE user_id = ?",(user_id,))
        db.commit()
        bot.send_message(message.chat.id,"Поздрвляю вас!")
        check_city(message)


    elif message.text == "Проверить🚕" and taxi < 20:
        bot.send_message(message.chat.id,"Вы не сделали 20 заказов!")

    elif message.text == "🗂️Задания" and check_sub == 2 :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Проверить🚌")
        btn2 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,"📚*Твое задание*:\n\nВыполните 25 рейсов на автобусе🏆 *награда:\n\n 💲15.000₽* ",reply_markup=markup,parse_mode='Markdown')
    
    elif message.text == "Проверить🚌" and bus >= 25:
        cur.execute("UPDATE users SET user_money = user_money + 20000 WHERE user_id = ?",(user_id,))
        db.commit()
        cur.execute("UPDATE users SET check_sub = check_sub + 1 WHERE user_id = ?",(user_id,))
        db.commit()
        bot.send_message(message.chat.id,"Поздрвляю вас!")
        check_city(message)

    elif message.text == "Проверить🚌" and bus < 25:
        bot.send_message(message.chat.id,"Вы не сделали 25 рейсов!")

    elif message.text == "🗂️Задания" and check_sub > 2 :
        bot.send_message(message.chat.id,"На данный момент вы выполнили все задания!)")


    elif message.text == '/menu':
        cur.execute("SELECT user_city, user_name FROM users WHERE user_id = ?",(user_id,))
        user_data = cur.fetchone()
        user_city, user_name = user_data
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔑Личный кабинет")
        btn2 = types.KeyboardButton("🛠️Работы")
        btn3 = types.KeyboardButton("🗂️Задания")
        btn4 = types.KeyboardButton("✈️Отправиться в другой город")
        markup.add(btn1,btn2,btn3,btn4)

        bot.send_message(message.chat.id, f"И снова привет {user_name}\nТы находишься в {user_city}\nКак тебе наша игра?",reply_markup=markup)

    elif message.text == "🔙Назад":
        check_city(message)

    elif message.text == "✈️Отправиться в другой город":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text="Москва-центр")
        btn2 = types.KeyboardButton(text="Королёв")
        btn3 = types.KeyboardButton(text="Чертаново")
        btn4 = types.KeyboardButton(text="Мытищи")
        btn5 = types.KeyboardButton(text="Балашиха")
        btn6 = types.KeyboardButton(text="Люберцы")
        btn7 = types.KeyboardButton(text="Видное")
        btn8 = types.KeyboardButton(text="Химки")
        btn9 = types.KeyboardButton("🔙Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn9)
        bot.send_message(message.chat.id,"Стоимость отправления стоит 💲1.000₽ если вы согласны выберите город в который вы хотите отправится",reply_markup=markup)
        bot.register_next_step_handler(message,to_new_city)



    elif message.text == "Проверить✅" and check_channel == 0:
        status = ['creator','administrator','member']
       
        for stat in status:
            if stat == bot.get_chat_member(chat_id="@Bratvarpchannel",user_id=message.from_user.id).status:
                cur.execute("UPDATE users SET user_money = user_money + 20000 WHERE user_id = ?",(user_id,))
                db.commit()
                cur.execute("UPDATE users SET check_sub = check_sub + 1 WHERE user_id = ?",(user_id,))
                db.commit()
                cur.execute("UPDATE users SET check_channel = check_channel + 1 WHERE user_id = ?",(user_id,))
                db.commit()
                bot.send_message(message.chat.id,"Спасибо за подписку!")
                check_city(message)
                break
        else:
            bot.send_message(message.chat.id,"Вы не подписаны!")
        
    elif message.text == "Проверить✅" and check_channel !=0:
        bot.send_message(message.chat.id,"Вы уже подписались")


    elif message.text == "🎰Казино" and users_ciity == "Москва-центр" :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎡Рулетка")
        btn2 = types.KeyboardButton("Блек джек")
        btn3 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn3)
        bot.send_message(message.chat.id,"Добро пожаловть в казино!",reply_markup=markup)

    elif message.text == "🎰Казино" and users_ciity != "Москва-центр" :
        bot.send_message(message.chat.id,"Отправляйтесь в Москву чтоб сыграть в казино")


    elif message.text == "🎡Рулетка":
       # photo = open("/Users/dayzy/Desktop/Bratva_mac/main/photo/roulette.jpeg",'rb')
       # bot.send_photo(message.chat.id, photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Поставить на число")
        btn2 = types.KeyboardButton("Поставить на сектор")
        btn3 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,f"Выберите на что вы хотите поставить",reply_markup=markup)



    elif message.text == "Поставить на число":
        photo = open("/Users/dayzy/Desktop/Bratva_mac/main/photo/roulette.jpeg",'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,"Выберите число от 0 до 36")
        bot.register_next_step_handler(message,sum_casino)




    elif message.text == "Поставить на сектор":
        cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
        us_money = cur.fetchone()[0]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        photo = open("/Users/dayzy/Desktop/Bratva_mac/main/photo/roulette.jpeg",'rb')
        btn1 = types.KeyboardButton("1")
        btn2 = types.KeyboardButton("2")
        btn3 = types.KeyboardButton("3")
        markup.add(btn1,btn2,btn3)
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,f"Выберите на какой сектор вы хотите поставить\nУ вас на счету:{us_money:,}",reply_markup=markup)
        bot.register_next_step_handler(message,casino_rows)
                

    elif message.text == "/admins" and user_id == admin_id:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Все пользователи")
        btn2 = types.KeyboardButton("Отправить деньги")
        btn3 = types.KeyboardButton("Рассылка")
        btn4 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id,"Приветствутю тебя админ!",reply_markup=markup)
        
    

    elif message.text == "/admins" and user_id != admin_id:
        bot.send_message(message.chat.id,"Вы не админ")
    
    elif message.text == "Рассылка" and user_id == admin_id:
        bot.send_message(user_id,'Введите текст который хотите отправить')
        bot.register_next_step_handler(message,send_all)

    elif message.text == "Отправить деньги" and user_id ==  admin_id:
        bot.send_message(message.chat.id,"Напишите id кому хотите отправить деньги")
        bot.register_next_step_handler(message,id_user)

    elif message.text == "Отправить деньги" and user_id !=  admin_id:
        bot.send_message(message.chat.id,"Вы не админ")

    elif message.text == "Все пользователи" and user_id == admin_id:
        cur.execute("SELECT user_name,user_id,user_money,bank_score FROM users ")
        users = cur.fetchall()
        for user_ids,username,moneys,bank_score in users:
            bot.send_message(message.chat.id,f"🆔ID:{username}\n👤Имя:{user_ids}\n💵На руках: {moneys:,}\n🏦В банке:{bank_score:,}")

    elif message.text == "Все пользователи" and user_id != admin_id:
        bot.send_message(message.chat.id,"Даже не пытайся)")

    elif message.text == "Блек джек":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать игру")
        btn2 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,"Нажмите начать игру",reply_markup=markup)
    

    elif message.text == "Начать игру":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("В игру")
        markup.add(btn1)
        bot.send_message(message.chat.id,"Игра начата",reply_markup=markup)
        # bot.register_next_step_handler(message,casino_blackjeck)

    elif message.text == "Полиция👮‍♀️" and work_police != 1:
        
        global police
        police = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Пройти тест")
        btn2 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2)

        bot.send_message(message.chat.id,"Приветствую тебя в отделе полиции\nЕсли ты хочешь начать служить нашей стране и бороться с приступностью тебе придется пройти тест ",reply_markup=markup)
        


    elif message.text == "Полиция👮‍♀️" and work_police == 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать патруль")
        btn2 = types.KeyboardButton("Увольнение")
        btn3 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,"Приветствую тебя кадет!",reply_markup=markup)


    elif message.text == "Начать патруль":
        cur.execute("UPDATE users SET work_police_check = work_police_check + 1 WHERE user_id = ?",(user_id,))
        db.commit()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Проверить район")
        markup.add(btn1)
        bot.send_message(message.chat.id,f"Вы начали патруль по городу {user_city_work}",reply_markup=markup)
        time.sleep(2)
        bot.register_next_step_handler(message,random_police_patrul)



    elif message.text == "Пройти тест":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("а")
        btn2 = types.KeyboardButton("б")
        btn3 = types.KeyboardButton("в")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,"🚨 Ты видишь подозрительную сумку, оставленную на вокзале. Что ты делаешь?\nА)Используешь сирену\nБ)Пытаешься его блокировать\nВ)Звонишь за подкреплением ",reply_markup=markup)
        bot.register_next_step_handler(message,police_test2)


    elif message.text == "Проверить" and work_check == True:
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Продолжить")
        btn2 = types.KeyboardButton("Вернуться")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,"Подойдите к машине медленно, чтобы не спугнуть угонщика. Используйте радио, чтобы вызвать подкрепление, если ситуация станет опасной",reply_markup=markup)

    elif message.text == "Продолжить"and work_check == True:
        
        random_car = random.choice(car_def)
        with open(random_car,'rb') as photo:
            orient = ["Будьте внимательны! Перед вами автомобиль, соответствующая описанию угнанной.  Проведите тщательную проверку, не подходите близко, если подозреваете водителя в опасности. Вызовите эвакуатор только при полном совпадении с ориентировкой"]
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Ориентировка")
            btn2 = types.KeyboardButton("Отправить машину на стоянку")
            btn3 = types.KeyboardButton("Продолжить патруль")
            markup.add(btn1,btn2,btn3)
            bot.send_message(message.chat.id,orient,reply_markup=markup)
            bot.send_photo(message.chat.id,photo)

    elif message.text == "Отправить машину на стоянку" and work_check == True :
       

        cur.execute("UPDATE users SET user_money = user_money + 1500 WHERE user_id = ?",(user_id,))
        db.commit()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Продолжить патруль")
        markup.add(btn1)
        bot.send_message(message.chat.id,"Хорошая работа\nМожешь вернуться к патрулю",reply_markup=markup)



    elif message.text == "Закончить работу" and work_check == True:
        cur.execute("UPDATE users SET work_police_check = work_police_check - 1 WHERE user_id = ?",(user_id,))
        db.commit()

        bot.send_message(message.chat.id,f"Вы хорошо поработали\nПропишите /menu чтоб вернуться в меню")
        


    elif message.text == "Продолжить патруль" and work_check == True:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Проверить район")
        markup.add(btn1)
        bot.send_message(message.chat.id,f"Вы продолжили патруль патруль по городу {user_city_work}",reply_markup=markup)
        time.sleep(2)
        bot.register_next_step_handler(message,random_police_patrul)



    elif message.text == "Ориентировка" and work_check == True:
        car = random.choice(car_ugon)
        with open(car["photo"],'rb') as photo:
            
            bot.send_message(message.chat.id,f"Марка: {car["Marka"]}\nЦвет: {car["Color"]}\nНомер: {car["Number"]}")
            bot.send_photo(message.chat.id,photo)
    
    elif message.text == "Вернуться" and work_check == 1:
        bot.register_next_step_handler(message,random_police_patrul)


    elif message.text == "Вернуться" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")



    elif message.text == "Продолжить"and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")

    elif message.text == "Проверить"and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")

    elif message.text == "Продолжить патруль" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")
    
    elif message.text == "Ориентировка" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")
    
    elif message.text == "Закончить работу" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")


    elif message.text == "Продолжить патруль" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")


    elif message.text == "Отправиться" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")
    
    
    elif message.text == "Разобраться" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")


    elif message.text == "Проверить документы" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")


    elif message.text == "Розыск" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")


    elif message.text == "Отправить в участок" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")


    elif message.text == "Выехать" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")


    elif message.text == "Вызвать скорую" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")


    elif message.text == "Опросить" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")


    elif message.text == "Составить протокол" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")


    elif message.text == "Отвезти в отдел" and work_check == 0:
        bot.send_message(message.chat.id,"Ты не в патруле")

    elif message.text == "Отправиться" :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Разобраться")
        btn2 = types.KeyboardButton("Продолжить патруль")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,"Вы приехали на место вызова, перед вами шумная компания подростков не поделившая что-либо между собой\nПодойдите разберитесь в ситуации помогите если это необоходимо, проверьте документы.",reply_markup=markup)

    elif message.text == "Разобраться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Проверить документы")
        btn2 = types.KeyboardButton("Отправить в участок")
        btn3 = types.KeyboardButton("Розыск")
        btn4 = types.KeyboardButton("Продолжить патруль")
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id,"Вы подошли к компании.")
        time.sleep(3)
        bot.send_message(message.chat.id,"Теперь проверьте документы и если вы посчитаете что то подозрительным отправьте подозреваемого в участок.\nЗнайте что в нашем городе есть люди которые розыскиваются если документы человека совпадают с ориентировкой немедленно задержите его и отправьте в участок.\nЕсли же все хорошо можете продолжить патруль.",reply_markup=markup)

    
    elif message.text == "Проверить документы":
        global name1,name2,name3
        
        random_dock = random.choice(people)
        random_dock2 = random.choice(people)
        random_dock3 = random.choice(people)

        name1 = random_dock["name"]
        name2 = random_dock2["name"]
        name3 = random_dock3["name"]

        bot.send_message(message.chat.id,f"Документы первого человека\nФИО:{random_dock["name"]}\nДата рождения: {random_dock["birthdate"]}\nГород: {random_dock["city"]}")
        time.sleep(5)
        bot.send_message(message.chat.id,f"Документы второго человека\nФИО:{random_dock2["name"]}\nДата рождения: {random_dock2["birthdate"]}\nГород: {random_dock2["city"]}")
        time.sleep(5)
        bot.send_message(message.chat.id,f"Документы третьего человека\nФИО:{random_dock3["name"]}\nДата рождения: {random_dock3["birthdate"]}\nГород: {random_dock3["city"]}")

    elif message.text == "Розыск":
        random_wanted = random.choice(wanted_people)
        bot.send_message(message.chat.id,f"Люди которые розыскиваются\nФИО:{random_wanted["name"]}\nДата рождения: {random_wanted["birthdate"]}\nГород: {random_wanted["city"]}")


    elif message.text == "Отправить в участок":
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('1')
        btn2 = types.KeyboardButton('2')
        btn3 = types.KeyboardButton('3')
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,"Выберите кого хотите отправить в участок",reply_markup=markup)
        bot.register_next_step_handler(message,wanted_police)



 
    elif message.text == "Выехать":
        bot.send_message(message.chat.id,"Вы в срочном порядке выехали на место проишествия")
        time.sleep(2)
        dtp = "Мытищи"
        cur.execute("UPDATE users SET user_city = ? WHERE user_id = ?",(dtp,user_id,))
        db.commit()
        cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",("Ул.Летная",user_id,))
        db.commit()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вызвать скорую")
        btn2 = types.KeyboardButton("Опросить")
        
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,"Вы прибыли на место проишествия\nВы видите пострадавшего человека вызовите скорую и узнайте что произошло ",reply_markup=markup)

    elif message.text == "Вызвать скорую":
        bot.send_message(message.chat.id,"Скорая была вызвана и уже направляется на место происшествия.")

    elif message.text == "Опросить":
        ramdom_people_dtp = random.choice(people_dtp)
        random_docks = random.choice(people)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Составить протокол")
        markup.add(btn1)
        bot.send_message(message.chat.id,"Выслушайте пострадавшего и составьте протокол.",reply_markup=markup)
        time.sleep(3)
        bot.send_message(message.chat.id,f"Мои паспортные данные\nФИО:{random_docks["name"]}\nДата рождения: {random_docks["birthdate"]}\nГород: {random_docks["city"]}")
        time.sleep(3)
        bot.send_message(message.chat.id,ramdom_people_dtp)



    elif message.text == "Составить протокол":
        bot.send_message(message.chat.id,"Запишите ФИО пострадавшего")
        bot.register_next_step_handler(message,protocol)




    elif message.text == "Отвезти в отдел":
        bot.send_message(message.chat.id,"Вы отправились в отдел это займет 30 секунд")
        time.sleep(3)
        protocols = ""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Продолжить патруль")
        btn2 = types.KeyboardButton("Закончить работу")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,"Отлично протокол был отдан дежурному вы можете продолжить патруль!",reply_markup=markup)


    elif message.text == "🚍🚏Отправиться на остановку":
        check_ostanovka(message)

    elif message.text == "Риелторское агенство" and user_city == "Москва-центр" and users_stret == "Проспект Мира":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Эконом")
        btn2 = types.KeyboardButton("Средний")
        btn3 = types.KeyboardButton("Высокий")
        btn4 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id,"Выберете какой класс вас интересует",reply_markup=markup)
        bot.register_next_step_handler(message,check_class_homes)


    elif message.text == "ЖК" and user_city == "Мытищи":
        home_econom(message)
    
    elif message.text == "/phone":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Перевести деньги")
        btn2 = types.KeyboardButton("Отправить сообещние")
        btn3 = types.KeyboardButton("еще что-то")
        btn4 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id,"Что хотите сделать?",reply_markup=markup)
        bot.register_next_step_handler(message,check_phone)


    elif message.text == "🏦Банк" and user_city == "Королёв":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Пополнить счет")
        btn2 = types.KeyboardButton("Снять деньги")
        btn3 = types.KeyboardButton("Перевести деньги")
        btn4 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id,"Добро пожаловать в Банк\nВыберите что хотите сделать",reply_markup=markup)
        bot.register_next_step_handler(message,check_bank_operation)



        

def sum_casino(message):
    global bet
    try:
        db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
        cur = db.cursor()
        bet = int(message.text)
        user_id = message.from_user.id
        if bet > 36:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🎰Казино")
            btn2 = types.KeyboardButton("🔙Назад")
            markup.add(btn1,btn2)
            bot.send_message(message.chat.id,"Такого числа нет!\nПопробуйте заново",reply_markup=markup)
        else:
            cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
            us_money = cur.fetchone()[0]
            bot.send_message(message.chat.id,f"Выберите сумму ставки\nУ вас на счету: {us_money:,}")
            bot.register_next_step_handler(message,casino_bet)
    except Exception:
                bot.send_message(message.chat.id,"Введите число!")
                check_city(message)




def casino_bet(message):
                global bet
                try:
                    lose_casino = [
                        "Брат, не фартило... Но не кисни, ещё зацепим хату! 🎲",
                        "Ну, кинули тебя кубики, как подельников на стреле...",
                        "Не повезло сегодня, братан. Но главное - не терять хватку, щас отыграем по полной! 👊",
                        "Эх, сегодня козыри в чужих руках... Но ты не сдавайся, пацан, у тебя ещё все впереди! 💪"
                    ]
                    random_lose = random.choice(lose_casino)
                    win_casino = [
                        "Ха-ха, брат! Забрал банк💰",
                        "Удача тебе улыбается, братан! 🥳  Продолжай в том же духе, и все бабки будут твои!",
                        "Ты круче всех, братан! 🎉  Сегодня ты король",
                        "Поздравляю, братан! Кубики оказались на твоей стороне! 🎲"
                    ]
                    random_win = random.choice(win_casino)
                    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
                    cur = db.cursor()

                    user_id = message.from_user.id

                    cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
                    money = cur.fetchone()[0]
                    sum = int(message.text)
                    
                    if sum > money or sum <=0:
                        bot.send_message(message.chat.id,"У вас столько нет!")
                        time.sleep(0.5)
                        return sum_casino(message)
                    elif bet > 36:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        btn1 = types.KeyboardButton("🎰Казино")
                        btn2 = types.KeyboardButton("🔙Назад")
                        markup.add(btn1,btn2)
                        bot.send_message(message.chat.id,"Такого числа нет!\nПопробуйте заново",reply_markup=markup)
                        
                    

                    result = random.randint(0, 36)
                    win_balance = money + sum *36
                    cash = sum *36
                    lose_balance = money - sum
                    cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
                    user_money = cur.fetchone()[0]


                    if bet ==  result :
                        bot.send_message(message.chat.id,"*Генерируем случайное число...*",parse_mode="Markdown")
                        time.sleep(3)
                        cur.execute("UPDATE users SET user_money =  ? WHERE user_id = ?",(win_balance,user_id,))
                        db.commit()
                        cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
                        user_money = cur.fetchone()[0]
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        btn1 = types.KeyboardButton("🎡Рулетка")
                        btn2 = types.KeyboardButton("🔙Назад")
                        markup.add(btn1,btn2)
                        bot.send_message(message.chat.id,f"*{random_win} \n\nВыпало число: {result}🎲\n\nВы выйграли: {cash:,}💲\nЕсли хотите продолжить игру нажмите 🎡Рулетка\nОставшийся баланс: {user_money:,}*",reply_markup=markup,parse_mode="Markdown")




                    



                    else:
                        bot.send_message(message.chat.id,"*Генерируем случайное число...*",parse_mode="Markdown")
                        time.sleep(3)
                        cur.execute("UPDATE users SET user_money =  ? WHERE user_id = ?",(lose_balance,user_id,))
                        db.commit()
                        cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
                        user_money = cur.fetchone()[0]
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        btn1 = types.KeyboardButton("🎡Рулетка")
                        btn2 = types.KeyboardButton("🔙Назад")
                        markup.add(btn1,btn2)
                        bot.send_message(message.chat.id,f"*{random_lose} \nВыпало число: {result}🎲\nЕсли хотите продолжить игру нажмите 🎡Рулетка\nОставшийся баланс: {user_money:,}*",reply_markup=markup,parse_mode="Markdown")
                        
                except Exception:
                    bot.send_message(message.chat.id,"Введите число!")
                    check_city(message)






def to_new_city(message):

    user_id = message.from_user.id
    new_city = message.text

    valid_cities = ["Москва-центр", "Королёв", "Чертаново", "Мытищи", "Балашиха", "Люберцы", "Видное", "Химки"]


    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
    us_money = cur.fetchone()[0]
    cur.execute("SELECT user_city FROM users WHERE user_id = ?",(user_id,))
    us_city = cur.fetchone()[0]

    if us_money < 1000 and us_city == "Москва-центр":
        bot.send_message(message.chat.id,"К сожалению у вас недостаточно средств")
        return check_city(message)
    
    elif us_money < 1000 and us_city != "Москва-центр":
        bot.send_message(message.chat.id,"К сожалению у вас недостаточно средств")
        return check_city(message)
     
    elif us_city == new_city:
        bot.send_message(message.chat.id,"Ты и так в этом городе!")
        check_city(message)
    
    elif new_city == "🔙Назад":
        check_city(message)
    
    elif new_city not in valid_cities:
        bot.send_message(message.chat.id,"Такого города нет!")
        check_city(message)
    
    
    elif new_city == "Москва-центр":
            cur.execute("UPDATE users SET user_money = user_money - 1000 WHERE user_id = ?",(user_id,))
            db.commit()
            
            cur.execute("UPDATE users SET user_city = ? WHERE user_id = ?",(new_city, user_id,))
            db.commit()

            cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",("Ул.Тверская",user_id))
            db.commit()
            bot.send_message(message.chat.id,f"<b>Вы отправились в {new_city}</b>",parse_mode="html")
            time.sleep(5)
            bot.send_message(message.chat.id,f"Ты теперь в {new_city}")
            check_city(message)
            

    elif new_city == "Королёв":
            cur.execute("UPDATE users SET user_money = user_money - 1000 WHERE user_id = ?",(user_id,))
            db.commit()
            
            cur.execute("UPDATE users SET user_city = ? WHERE user_id = ?",(new_city, user_id,))
            db.commit()

            cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",("Ул.Ленина",user_id))
            db.commit()
            bot.send_message(message.chat.id,f"<b>Вы отправились в {new_city}</b>",parse_mode="html")
            time.sleep(5)
            bot.send_message(message.chat.id,f"Ты теперь в {new_city}")
            check_city(message)

    elif new_city == "Чертаново":
            cur.execute("UPDATE users SET user_money = user_money - 1000 WHERE user_id = ?",(user_id,))
            db.commit()
            
            cur.execute("UPDATE users SET user_city = ? WHERE user_id = ?",(new_city, user_id,))
            db.commit()

            cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",("Ул.Чертановская",user_id))
            db.commit()
            bot.send_message(message.chat.id,f"<b>Вы отправились в {new_city}</b>",parse_mode="html")
            time.sleep(5)
            bot.send_message(message.chat.id,f"Ты теперь в {new_city}")
            check_city(message)

    elif new_city == "Мытищи":
            cur.execute("UPDATE users SET user_money = user_money - 1000 WHERE user_id = ?",(user_id,))
            db.commit()
            
            cur.execute("UPDATE users SET user_city = ? WHERE user_id = ?",(new_city, user_id,))
            db.commit()

            cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",("Ул.Летная",user_id))
            db.commit()
            bot.send_message(message.chat.id,f"<b>Вы отправились в {new_city}</b>",parse_mode="html")
            time.sleep(5)
            bot.send_message(message.chat.id,f"Ты теперь в {new_city}")
            check_city(message)
    
    elif new_city == "Балашиха":
            cur.execute("UPDATE users SET user_money = user_money - 1000 WHERE user_id = ?",(user_id,))
            db.commit()
            
            cur.execute("UPDATE users SET user_city = ? WHERE user_id = ?",(new_city, user_id,))
            db.commit()

            cur.execute("UPDATE users SET user_street = ? WHERE user_id = ?",("Ул.Победы",user_id))
            db.commit()
            bot.send_message(message.chat.id,f"<b>Вы отправились в {new_city}</b>",parse_mode="html")
            time.sleep(5)
            bot.send_message(message.chat.id,f"Ты теперь в {new_city}")
            check_city(message)
    
    
    









def id_user(message):
    global id
    id = message.text
    bot.send_message(message.chat.id,"Введите сумму:")
    bot.register_next_step_handler(message,send_money)

def send_money(message):
    global id
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    try:
        money = int(message.text)
        user_id = message.from_user.id
        cur.execute("SELECT user_money FROM users WHERE user_id = ?",(id,))
        user_money = cur.fetchone()
        user_balance = user_money[0]
        total = user_balance + money
        cur.execute(f"UPDATE users SET user_money = ?  WHERE user_id = ?",(total,id,))
        db.commit()
        bot.send_message(message.chat.id,"Деньги отправлены)")
        bot.send_message(id,f"Вам перевели: {money:,}")
    except Exception:
        bot.send_message(message.chat.id,"Произошла ошибка попробуйте позже")
        check_city(message)






def casino_rows(message):
    global row
    
    
    
    try:
        row = int(message.text)
        if row == 1:
            user_sector = 1
        elif row == 2:
            user_sector = 2
        elif row == 3:
            user_sector = 3
        global sector
        sector = user_sector
        if row > 3:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🎰Казино")
            btn2 = types.KeyboardButton("🔙Назад")
            markup.add(btn1,btn2)
            bot.send_message(message.chat.id,"Такого числа нет!\nПопробуйте заново",reply_markup=markup)
        else:
            bot.send_message(message.chat.id,"Выберите сумму ставки")
            bot.register_next_step_handler(message,casino_row)
    except Exception:
        bot.send_message(message.chat.id,"Произошла ошибка")
        check_city(message)
                    


def get_sector(number):
    if 1 <= number <= 12:
        return 1
    elif 13 <= number <= 24:
        return 2
    elif 25 <= number <= 36:
        return 3
    else:
        return None



def casino_row(message):
    global row
    global sector
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    try:
        lose_casino = [
                        "Брат, не фартило... Но не кисни, ещё зацепим хату! 🎲",
                        "Ну, кинули тебя кубики, как подельников на стреле...",
                        "Не повезло сегодня, братан. Но главное - не терять хватку, щас отыграем по полной! 👊",
                        "Эх, сегодня козыри в чужих руках... Но ты не сдавайся, пацан, у тебя ещё все впереди! 💪"
                    ]
        random_lose = random.choice(lose_casino)
        win_casino = [
                        "Ха-ха, брат! Забрал банк💰",
                        "Удача тебе улыбается, братан! 🥳  Продолжай в том же духе, и все бабки будут твои!",
                        "Ты круче всех, братан! 🎉  Сегодня ты король",
                        "Поздравляю, братан! Кубики оказались на твоей стороне! 🎲"
                    ]
        random_win = random.choice(win_casino)
        user_id = message.from_user.id

        bid  = int(message.text)

        random_number1  = random.randint(1,36)
        cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
        user_money = cur.fetchone()[0]
        
        if bid > user_money or bid <= 0 :
            bot.send_message(message.chat.id,"У вас столько нет!")
            time.sleep(0.5)
            return sum_casino(message) 
        
        win = user_money + bid * 3
        loose = user_money - bid
        cash = bid * 3
        result_sector = get_sector(random_number1)

        
        if sector == result_sector :
                bot.send_message(message.chat.id,"*Генерируем случайное число...*",parse_mode="Markdown")
                time.sleep(3)
                cur.execute("UPDATE users SET user_money =  ? WHERE user_id = ?",(win,user_id,))
                db.commit()
                cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
                user_money = cur.fetchone()[0]
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("🎡Рулетка")
                btn2 = types.KeyboardButton("🔙Назад")
                markup.add(btn1,btn2)
                bot.send_message(message.chat.id,f"*{random_win}\nВыпало число {random_number1}🎲\nВы выйграли: {cash:,}💲\nЕсли хотите продолжить игру нажмите 🎡Рулетка\nОставшийся баланс: {user_money:,}*",reply_markup=markup,parse_mode="Markdown")




                        



        else:
                bot.send_message(message.chat.id,"*Генерируем случайное число...*",parse_mode="Markdown")
                time.sleep(3)
                cur.execute("UPDATE users SET user_money =  ? WHERE user_id = ?",(loose,user_id,))
                db.commit()
                cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
                user_money = cur.fetchone()[0]
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("🎡Рулетка")
                btn2 = types.KeyboardButton("🔙Назад")
                markup.add(btn1,btn2)
                bot.send_message(message.chat.id,f"*{random_lose}\nВыпало число {random_number1}🎲\nЕсли хотите продолжить игру нажмите 🎡Рулетка\nОставшийся баланс: {user_money:,}*",reply_markup=markup,parse_mode="Markdown")
    except Exception:
        bot.send_message(message.chat.id,"Произошла ошибка")
        check_city(message)   
                        

# def casino_blackjeck(message):
#     global diler
#     if message.text == "В игру":
#         random_ochk = random.randint(1,11)
#         random_ochk2 = random.randint(1,11)
#         diler = random_ochk
#         user = random_ochk2
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("Взять")
#         btn2 = types.KeyboardButton('Оставить')
#         markup.add(btn1,btn2)
#         bot.send_message(message.chat.id,f"У дилера: {diler}\nУ вас: {user} ",reply_markup=markup)
        






def police_test2(message):
    
    
    global test_ball
    if message.text == "а":
        test_ball +=1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("а")
        btn2 = types.KeyboardButton("б")
        btn3 = types.KeyboardButton("в")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,"Ты видишь драку на улице.  Что ты делаешь?\nа) Разнимаешь дерущихся\nа)Звонишь в полицию\nб)Ждешь, пока они сами успокоятся",reply_markup=markup)
        bot.register_next_step_handler(message,police_test3)    
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("а")
        btn2 = types.KeyboardButton("б")
        btn3 = types.KeyboardButton("в")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,"Ты видишь драку на улице.  Что ты делаешь?\nа) Разнимаешь дерущихся\nа)Звонишь в полицию\nб)Ждешь, пока они сами успокоятся",reply_markup=markup)
        bot.register_next_step_handler(message,police_test3)  



def police_test3(message):
    
    global test_ball
    if message.text == "а":
        test_ball +=1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("а")
        btn2 = types.KeyboardButton("б")
        btn3 = types.KeyboardButton("в")
        markup.add(btn1,btn2,btn3)
        
        bot.send_message(message.chat.id,"Ты  узнал  от  информатора,  что  в  определенном  месте  собирается  банда.  Как  ты  планируешь  провести  операцию  по  задержанию?\nа)Разрабатываешь  план  и  собираешь  необходимые  ресурсы \nб)Врываешься  в  место  сбора  банды  и  арестовываешь  их  👊\nв) Рискуешь  не  вмешиваться  и  не  ставить  под  угрозу  свою  безопасность")
        bot.register_next_step_handler(message,police_test4)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("а")
        btn2 = types.KeyboardButton("б")
        btn3 = types.KeyboardButton("в")
        markup.add(btn1,btn2,btn3)
        
        bot.send_message(message.chat.id,"Ты  узнал  от  информатора,  что  в  определенном  месте  собирается  банда.  Как  ты  планируешь  провести  операцию  по  задержанию?\nа)Разрабатываешь  план  и  собираешь  необходимые  ресурсы \nб)Врываешься  в  место  сбора  банды  и  арестовываешь  их  👊\nв) Рискуешь  не  вмешиваться  и  не  ставить  под  угрозу  свою  безопасность")
        bot.register_next_step_handler(message,police_test4)

def police_test4(message):
    
    global test_ball
    if message.text == "а":
        test_ball +=1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("а")
        btn2 = types.KeyboardButton("б")
        btn3 = types.KeyboardButton("в")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,"🔒  Ты  работаешь  над  делом  о  бандитизме.  Тебе  предлагают  взятку,  чтобы  ты  закрыл  глаза  на  преступления  банды.  Что  ты  делаешь?\nа)Берешь  взятку  и  прекращаешь  расследование  💰\nб)Сообщаешь  о  предложении  взятки  своим  начальникам  \nв)Отказываешься  от  взятки  и  продолжаешь  расследование  👮‍♀️",reply_markup=markup)
        bot.register_next_step_handler(message,police_test5)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("а")
        btn2 = types.KeyboardButton("б")
        btn3 = types.KeyboardButton("в")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,"🔒  Ты  работаешь  над  делом  о  бандитизме.  Тебе  предлагают  взятку,  чтобы  ты  закрыл  глаза  на  преступления  банды.  Что  ты  делаешь?\nа)Берешь  взятку  и  прекращаешь  расследование  💰\nб)Сообщаешь  о  предложении  взятки  своим  начальникам  \nв)Отказываешься  от  взятки  и  продолжаешь  расследование  👮‍♀️",reply_markup=markup)
        bot.register_next_step_handler(message,police_test5)



def police_test5(message):
    global test_ball

    if message.text == "б":
        test_ball +=1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("а")
        btn2 = types.KeyboardButton("б")
        btn3 = types.KeyboardButton("в")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,"💰 Ты  знаешь,  что  у  местного  бизнесмена  есть  нелегальный  бизнес,  связанный  с  бандитами. Что  ты  делаешь?\nа)Шантажируешь  бизнесмена,  требуя  от него  деньги \nб)Считаешь  это  не  твоим  делом  и  не  вмешиваешься\nв)Собираешь  доказательства  и  передаешь  их  в  полицию 🕵️‍♀️",reply_markup=markup)
        bot.register_next_step_handler(message,police_test6)

    else:
        test_ball +=1


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("а")
        btn2 = types.KeyboardButton("б")
        btn3 = types.KeyboardButton("в")
        markup.add(btn1,btn2,btn3)


        bot.send_message(message.chat.id,"💰 Ты  знаешь,  что  у  местного  бизнесмена  есть  нелегальный  бизнес,  связанный  с  бандитами. Что  ты  делаешь?\nа)Шантажируешь  бизнесмена,  требуя  от него  деньги \nб)Считаешь  это  не  твоим  делом  и  не  вмешиваешься\nв)Собираешь  доказательства  и  передаешь  их  в  полицию 🕵️‍♀️",reply_markup=markup)
        bot.register_next_step_handler(message,police_test6)



def police_test6(message):
    global test_ball

    if message.text == "в":
        test_ball +=1


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("а")
        btn2 = types.KeyboardButton("б")
        btn3 = types.KeyboardButton("в")
        markup.add(btn1,btn2,btn3)

    
    
        bot.send_message(message.chat.id,f" Ты  в  патруле  и  замечаешь  подозрительную  машину  с  группой  людей  внутри.  Что  ты  делаешь?\nа)Скрываешься  и  вызываешь  подкрепление\nб)Останавливаешь  машину  и  проверяешь  документы \nв)Проезжаешь  мимо  и  не  обращаешь  внимания",reply_markup=markup)
        bot.register_next_step_handler(message,police_finish_test)
    

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("а")
        btn2 = types.KeyboardButton("б")
        btn3 = types.KeyboardButton("в")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,"а)Скрываешься  и  вызываешь  подкрепление\nб)Останавливаешь  машину  и  проверяешь  документы \nв)Проезжаешь  мимо  и  не  обращаешь  внимания",reply_markup=markup)
        bot.register_next_step_handler(message,police_finish_test)


def police_finish_test(message):
    global test_ball
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    if test_ball > 4 and message.text == "б" :
        user_id = message.from_user.id
        cur.execute("UPDATE users SET work_police = work_police + 1 WHERE user_id = ?",(user_id,))
        db.commit()
        cur.execute("UPDATE users SET work = ? WHERE user_id = ?",(police,user_id,))
        db.commit()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать патруль")
        btn2 = types.KeyboardButton("🔙Назад")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,f"Поздрваляем ты теперь в рядах полиции!\nТы набрал: {test_ball} баллов!",reply_markup=markup)
        
    else:
        bot.send_message(message.chat.id,"Тебе пока рано служить")


def random_police_patrul(message):
    patrul = {
        1:police_patrul1,
        2:police_patrul2,
        3:police_patrul3
    }
    random_index = random.choice(list(patrul.keys()))
    patrul[random_index](message)





def police_patrul1(message):
    
    pat = ["В районе замечена подозрительная машина, возможно, угнанная. Проверьте номер и документы"]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Проверить")
    btn2 = types.KeyboardButton("Продолжить патруль")
    btn3 = types.KeyboardButton("Закончить работу")
    markup.add(btn1,btn2,btn3)
    bot.send_message(message.chat.id,pat,reply_markup=markup)
    

def police_patrul2(message):
    situtaion = [
        "В дежурную часть поступило сообщение о хулиганстве в вашем районе\nВыдвигайтесь и разберитесь в этом"
    ]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Отправиться")
    btn2 = types.KeyboardButton("Продолжить патруль")
    btn3 = types.KeyboardButton("Закончить работу")
    markup.add(btn1,btn2,btn3)
    bot.send_message(message.chat.id,situtaion,reply_markup=markup)

    
def police_patrul3(message):
    situtaion = [
        "Поступила информация о ДТП в Мытищах. Прибыть на место и оказать помощь пострадавшим, обеспечить безопасность."
    ]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выехать")
    btn2 = types.KeyboardButton("Продолжить патруль")
    btn3 = types.KeyboardButton("Закончить работу")
    markup.add(btn1,btn2,btn3)
    bot.send_message(message.chat.id,situtaion,reply_markup=markup)







def wanted_police(message):
    if message.text == "1":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Продолжить патруль")
        btn2 = types.KeyboardButton("Закончить работу")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,f"Хорошо\n{name1},будет отправлен до выяснения обстоятельств",reply_markup=markup)

    elif message.text == "2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Продолжить патруль")
        btn2 = types.KeyboardButton("Закончить работу")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,f"Хорошо\n{name2},будет отправлен до выяснения обстоятельств",reply_markup=markup)

    elif message.text == "3":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Продолжить патруль")
        btn2 = types.KeyboardButton("Закончить работу")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,f"Хорошо\n{name3},будет отправлен до выяснения обстоятельств",reply_markup=markup)




def protocol(message):
    global protocols
    protocols = f"ФИО:{message.text}\n"

    bot.send_message(message.chat.id,"Запишите дату рождения пострадавшего")
    bot.register_next_step_handler(message,protocol2)

def protocol2(message):
    global protocols
    protocols += f"Дата рождения:{message.text}\n"

    bot.send_message(message.chat.id,"Опишите в кратце ситацию.")
    bot.register_next_step_handler(message,protocol3)


def protocol3(message):
    global protocols
    protocols += f"Описание ситуации:{message.text}"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Отвезти в отдел")
    btn2 = types.KeyboardButton("Продолжить патруль")
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id,f"Отлично протокол составлен вы можете отвезти его в отдел и продолжить патруль.\n\n\nВаш протокол\n{protocols}",reply_markup=markup)
    

def new_name(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    user_id = message.from_user.id
    new_name = message.text
    cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
    user_money = cur.fetchone()[0]
    
    try: 
        if new_name == "🔙Назад":
            check_city(message)
            
        elif user_money >= 15000:

            bot.send_message(message.chat.id,"*Происходит смена имени...🔄*",parse_mode="Markdown")
            time.sleep(3)
            cur.execute("UPDATE users SET user_money = user_money - 15000 WHERE user_id = ?",(user_id,))
            db.commit()
            cur.execute("UPDATE users SET user_name = ? WHERE user_id = ?",(new_name,user_id,))
            db.commit()
            bot.send_message(message.chat.id,f"Вы сменили имя на:{new_name} ")
            check_city(message)
        
      
        else:
            bot.send_message(message.chat.id,"Недостаточно средств")
            check_city(message)
    except Exception:
        bot.send_message(message.chat.id,"Ошибка")


def check_city(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    user_id = message.from_user.id
    cur.execute("SELECT user_street FROM users WHERE user_id = ?",(user_id,))
    user_street = cur.fetchone()[0]
    cur.execute("SELECT user_city FROM users WHERE user_id = ?",(user_id,))
    user_city = cur.fetchone()[0]

    if user_city == "Москва-центр" and user_street == "Ул.Тверская":
        stret_tversk(message)

    elif user_city == "Москва-центр" and user_street == "Ул.Шухова":
        stret_shuhova(message)

    elif user_city == "Москва-центр" and user_street == "Проспект Мира":
        stret_mira(message)

    elif user_city == "Москва-центр" and user_street == "Проспект Вернадского":
        stret_vernad(message)
    
    elif user_city == "Королёв" and user_street == "Ул.Ленина":
        street_lenin(message)

    elif user_city == "Королёв" and user_street == "Ул.Октябрьская":
        street_oct(message)

    elif user_city == "Королёв" and user_street == "Ул.Раина":
        street_rain(message)

    elif user_city == "Чертаново" and user_street == "Варшавское шоссе":
        street_varsh(message)
        
    elif user_city == "Чертаново" and user_street == "Ул.Сумская":
        street_sumsk(message)

    elif user_city == "Чертаново" and user_street == "Ул.Чертановская":
        street_chertanovskaya(message)
    

    elif user_city == "Мытищи" and user_street == "Ул.Летная":
        street_letnaya(message)

    elif user_city == "Мытищи" and user_street == "Ул.Борисовка":
        street_borisovka(message)
    
    elif user_city == "Мытищи" and user_street == "Ул.Юбилейная":
        street_yubileyn(message)
    
    elif user_city == "Балашиха" and user_street == "Ул.Разина":
        street_razin(message)
    
    elif user_city == "Балашиха" and user_street == "Ул.Победы":
        street_victory(message)
    
    elif user_city == "Балашиха" and user_street == "Ул.Крупская":
        street_crups(message)
    


        
        

    
    
        


def check_ostanovka(message):
    db = sqlite3.connect('C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db')
    cur = db.cursor()
    user_id = message.from_user.id
    cur.execute("SELECT user_city FROM users WHERE user_id = ?",(user_id,))
    user_city = cur.fetchone()[0]
    if user_city == "Москва-центр":
        bot.send_message(message.chat.id,"*Вы идете до остановки...*",parse_mode="Markdown")
        time.sleep(3)
        
        ostanovka_msk(message)


    elif user_city == "Королёв":
        bot.send_message(message.chat.id,"*Вы идете до остановки...*",parse_mode="Markdown")
        time.sleep(3)
        ostanovka_korolev(message)

    elif user_city == "Чертаново":
        bot.send_message(message.chat.id,"*Вы идете до остановки...*",parse_mode="Markdown")
        time.sleep(3)
        ostanovka_chertanovo(message)

    elif user_city == "Мытищи":
        bot.send_message(message.chat.id,"*Вы идете до остановки...*",parse_mode="Markdown")
        time.sleep(3)
        ostanovka_mytischi(message)
    
    elif user_city == "Балашиха":
        bot.send_message(message.chat.id,"*Вы идете до остановки...*",parse_mode="Markdown")
        time.sleep(3)
        ostanovka_balashiha(message)

    




def ostanovka_msk(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Проспект Вернадского")
    btn2 = types.KeyboardButton("Проспект Мира")
    btn3 = types.KeyboardButton("Ул.Тверская")
    btn4 = types.KeyboardButton("Ул.Шухова")
    markup.add(btn1,btn2,btn3,btn4)
    bot.send_message(message.chat.id,"На какую улицу хотите отправиться",reply_markup=markup)
    bot.register_next_step_handler(message,street_moscows)



def ostanovka_korolev(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ул.Ленина")
    btn2 = types.KeyboardButton("Ул.Октябрьская")
    btn3 = types.KeyboardButton("Ул.Раина")
    markup.add(btn1,btn2,btn3,)
    bot.send_message(message.chat.id,"На какую улицу хотите отправиться",reply_markup=markup)
    bot.register_next_step_handler(message,street_korolev)




def ostanovka_chertanovo(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ул.Сумская")
    btn2 = types.KeyboardButton("Варшавское шоссе")
    btn3 = types.KeyboardButton("Ул.Чертановская")
    markup.add(btn1,btn2,btn3,)
    bot.send_message(message.chat.id,"На какую улицу хотите отправиться",reply_markup=markup)
    bot.register_next_step_handler(message,street_chertanovo)

def ostanovka_mytischi(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ул.Летная")
    btn2 = types.KeyboardButton("Ул.Борисовка")
    btn3 = types.KeyboardButton("Ул.Юбилейная")
    markup.add(btn1,btn2,btn3,)
    bot.send_message(message.chat.id,"На какую улицу хотите отправиться",reply_markup=markup)
    bot.register_next_step_handler(message,street_mytischis)


def ostanovka_balashiha(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ул.Разина")
    btn2 = types.KeyboardButton("Ул.Победы")
    btn3 = types.KeyboardButton("Ул.Крупская")
    markup.add(btn1,btn2,btn3,)
    bot.send_message(message.chat.id,"На какую улицу хотите отправиться",reply_markup=markup)
    bot.register_next_step_handler(message,street_balash)




def check_phone(message):
    if message.text == "Отправить сообещние":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id,"Введите ID кому хотите отправить сообщение",reply_markup=markup)
        bot.register_next_step_handler(message,user_send_message)



    elif message.text == "Перевести деньги":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙Назад")
        markup.add(btn1)
        bot.send_message(message.chat.id,"Введите ID кому хотите отправить деньги",reply_markup=markup)
        bot.register_next_step_handler(message,money_id)


def user_send_message(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    user_id = message.from_user.id

    
    try:
        global send_id,username
        cur.execute("SELECT user_name FROM users WHERE user_id = ?",(user_id,))
        username = cur.fetchone()[0]
        cur.execute("SELECT user_id FROM users WHERE user_id = ?",(user_id,))
        userids = cur.fetchone()[0]
        send_id =  int(message.text)
        if send_id == userids:
            bot.send_message(message.chat.id,"Вы не можете написать самому себе")
        else:
            bot.send_message(message.chat.id,"Введите текст сообещения")
            bot.register_next_step_handler(message,user_send_text)
    except Exception:
        bot.send_message(message.chat.id,'Введите ID,а не текст')
        bot.register_next_step_handler(message,user_send_message)



def user_send_text(message):
   
    user_id = message.from_user.id
    user_text = message.text

    bot.send_message(send_id,f"Сообщение от {username}:\n{user_text}")
    bot.send_message(message.chat.id,"Сообщение отправлено")


def money_id(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    user_id = message.from_user.id
    global send_ids,usernames
    send_ids = int(message.text)
    cur.execute("SELECT user_id FROM users WHERE user_id = ?",(user_id,))
    userid = cur.fetchone()[0]
    cur.execute("SELECT user_name FROM users WHERE user_id = ?",(user_id,))
    usernames = cur.fetchone()[0]
    if send_ids == userid:
        bot.send_message(message.chat.id,"Вы не можете перевести самому себе")
    else:
        bot.send_message(message.chat.id,"Введите сумму")
        bot.register_next_step_handler(message,user_send_money)


def user_send_money(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    user_id = message.from_user.id
    summa = int(message.text)
    cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
    money = cur.fetchone()[0]
    if summa > money or summa <= 0:
        bot.send_message(message.chat.id,"У вас столько нет")
        
    else:
        cur.execute("UPDATE users SET user_money = user_money - ? WHERE user_id = ?",(summa,user_id,))
        db.commit()
        cur.execute("UPDATE users SET user_money = user_money + ? WHERE user_id = ?",(summa,send_ids,))
        db.commit()
        bot.send_message(send_ids,f"{usernames},перевёл вам:{summa:,}")
        bot.send_message(user_id,"Деньги отправлены")




def check_bank_operation(message):
    user_id = message.from_user.id
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    cur.execute("SELECT bank_score FROM users WHERE user_id = ?",(user_id,))
    money = cur.fetchone()[0]

    if message.text == "Пополнить счет":
        bot.send_message(message.chat.id,"Выберите сумму для пополнения")
        bot.register_next_step_handler(message,top_money)

    elif message.text == "Снять деньги":
        bot.send_message(message.chat.id,f"Какую сумму хотите снять?\nНа счету:{money:,}")
        bot.register_next_step_handler(message,down_money)

    elif message.text == "Перевести деньги":
        bot.send_message(message.chat.id,"Введите ID кому хотите отправить деньги")
        bot.register_next_step_handler(message,money_id)




def top_money(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    user_id = message.from_user.id
    
    cur.execute("SELECT user_money FROM users WHERE user_id = ?",(user_id,))
    money = cur.fetchone()[0]
    top_summ = int(message.text)
    if top_summ > money or top_summ == 0:
        bot.send_message(message.chat.id,'К сожалению у вас столько нет')
    else:
        cur.execute("UPDATE users SET bank_score = bank_score + ? WHERE user_id = ?",(top_summ,user_id,))
        cur.execute("UPDATE users SET user_money = user_money - ? WHERE user_id = ?",(top_summ,user_id,))
        db.commit()
        bot.send_message(user_id,'Банковский счет пополнен)')




def down_money(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    user_id = message.from_user.id
    
    cur.execute("SELECT bank_score FROM users WHERE user_id = ?",(user_id,))
    money = cur.fetchone()[0]
    down_summ = int(message.text)

    if down_summ > money or down_summ <= 0:
        bot.send_message(message.chat.id,'К сожалению у вас столько нет')
    else:
        cur.execute("UPDATE users SET bank_score = bank_score - ? WHERE user_id = ?",(down_summ,user_id,))
        cur.execute("UPDATE users SET user_money = user_money + ? WHERE user_id = ?",(down_summ,user_id,))
        db.commit()
        bot.send_message(user_id,'Деньги сняты)')




def send_all(message):
    db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/users.db")
    cur = db.cursor()
    user_id = message.from_user.id
    user_text = message.text
    cur.execute("SELECT user_id FROM users")
    all_users = cur.fetchall()
    user_ids = [row[0] for row in all_users]

    # Отправка сообщения каждому пользователю
    for user_id in user_ids:
        bot.send_message(user_id, user_text)

bot.polling(none_stop=True)


