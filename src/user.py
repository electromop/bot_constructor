import sqlite3

class User:
    def __init__(self, login):
        self.username = login
    
    def get_bots(self):
        conn = sqlite3.connect('DB/users.db')
        cur = conn.cursor()
        cur.execute('''SELECT bots_name_list, bots_token_list FROM users_bots WHERE username = ?
''', (self.username, ))
        bots_dict = cur.fetchall()
        conn.close()

        return dict(bots_dict)
    
    def add_bot(self, bot_name, bot_token):
        conn = sqlite3.connect('DB/users.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO users_bots (username, bots_name_list, bots_token_list) VALUES (?, ?, ?)''', (f"{self.username}", f"{bot_name}", f"{bot_token}", ))
        conn.commit()
        conn.close()

# user = User("root")
# user.get_bots()


# conn = sqlite3.connect('DB/users.db')
# cur = conn.cursor()

# # Создание таблицы
# cur.execute('''CREATE TABLE IF NOT EXISTS users_bots (
#                     username TEXT NOT NULL,
#                     bots_name_list TEXT,
#                     bots_token_list TEXT
#                )''')
# # Сохранение изменений
# conn.commit()
# conn.close()

# user = User("root")
# user.add_bot("test_2_bot", "12345")
# user.get_bots()

# conn = sqlite3.connect('DB/users.db')
# cur = conn.cursor()

# # Создание таблицы
# cur.execute('''INSERT INTO users_bots (username, bots_name_list, bots_token_list) VALUES (?, ?, ?)''', ("root", "test_1_bot", "11234567890", ))
# # Сохранение изменений
# conn.commit()
# conn.close()
