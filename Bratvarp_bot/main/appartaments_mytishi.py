import sqlite3



db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/econom1.db")
cur = db.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='econom1'")
if not cur.fetchone():
        cur.execute("""CREATE TABLE IF NOT EXISTS econom1 (
        home_num INTEGER DEFAULT 1,
        class_home TEXT DEFAULT 'Эконом',
        price INTEGER DEFAULT 90000,
        owner_name TEXT DEFAULT 'Государство',
        city TEXT DEFAULT 'Мытищи'

        )""")

        cur.execute("""INSERT INTO econom1 (home_num,class_home, price, owner_name, city)
        VALUES (1,'Эконом', 90000, 'Государство', 'Мытищи')""")

        db.commit()


        db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/econom2.db")
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS econom2(
                home_num INTEGER DEFAULT 1,
                class_home TEXT  'Эконом',
                price INTEGER DEFAULT 90000,
                owner_name  TEXT DEFAULT 'Государство',
                city TEXT DEFAULT 'Мытищи'      

        )""")

        cur.execute("""INSERT INTO econom2 (home_num,class_home, price, owner_name, city)
        VALUES (2,'Эконом', 90000, 'Государство', 'Мытищи')""")

        db.commit()





        db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/econom3.db")
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS econom3(
                home_num INTEGER DEFAULT 1,
                class_home TEXT  'Эконом',
                price INTEGER DEFAULT 90000,
                owner_name  TEXT DEFAULT 'Государство',
                city TEXT DEFAULT 'Мытищи'    

        )""")

        cur.execute("""INSERT INTO econom3 (home_num,class_home, price, owner_name, city)
        VALUES (3,'Эконом', 90000, 'Государство', 'Мытищи')""")

        db.commit()




db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/middle1.db")
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS middle1(
        class_home TEXT DEFAULT 'Средний',
        price INTEGER DEFAULT 150000,
        owner_name  TEXT DEFAULT 'Государство',
        city TEXT DEFAULT 'Москва-центр'     

)""")

cur.execute("""INSERT INTO middle1 (class_home, price, owner_name, city)
VALUES ('Средний', 150000, 'Государство', 'Москва-центр')""")

db.commit()

db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/middle2.db")
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS middle2(
        class_home TEXT DEFAULT 'Средний',
        price INTEGER DEFAULT 150000,
        owner_name  TEXT DEFAULT 'Государство',
        city TEXT DEFAULT 'Москва-центр'     

)""")


cur.execute("""INSERT INTO middle2 (class_home, price, owner_name, city)
VALUES ('Средний', 150000, 'Государство', 'Москва-центр')""")

db.commit()


db = sqlite3.connect("C:/Users/dimap/Desktop/Bratvarp_bot/main/Database/middle3.db")
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS middle3(
        class_home TEXT DEFAULT 'Средний',
        price INTEGER DEFAULT 150000,
        owner_name  TEXT DEFAULT 'Государство',
        city TEXT DEFAULT 'Москва-центр'       

)""")

cur.execute("""INSERT INTO middle3 (class_home, price, owner_name, city)
VALUES ('Средний', 150000, 'Государство', 'Москва-центр')""")

db.commit()


