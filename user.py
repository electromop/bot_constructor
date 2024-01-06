import sqlite3

class User:
    def __init__(self, login):
        self.username = login
    
    def get_bots(self):
        conn = sqlite3.connect('DB/users.db')
        cur = conn.cursor()
        cur.execute('''SELECT bots_list FROM users_bots WHERE username = ?
''', (self.username, ))
        bots_list = cur.fetchall()
        conn.close()
        print(type(bots_list[0]), bots_list[0])

        return bots_list[0][0].split(',') if bots_list[0][0] != None else []
    
    def add_bot(self, bot_token):
        bots_list = self.get_bots()
        bots_list.append(bot_token)

        conn = sqlite3.connect('DB/users.db')
        cur = conn.cursor()
        cur.execute("UPDATE users_bots SET bots_list = ? WHERE username = ?", (",".join(bots_list), self.username))
        conn.commit()
        conn.close()



# conn = sqlite3.connect('DB/users.db')
# cur = conn.cursor()

# # Создание таблицы
# cur.execute('''CREATE TABLE IF NOT EXISTS users_bots (
#                     username TEXT NOT NULL,
#                     bots_list TEXT
#                )''')
# # Сохранение изменений
# conn.commit()
# conn.close()

# user = User("root")
# user.add_bot("12345")
# user.add_bot("678910")
# print(user.get_bots())

# conn = sqlite3.connect('DB/users.db')
# cur = conn.cursor()

# # Создание таблицы
# cur.execute('''INSERT INTO users_bots (username, bots_list) VALUES (?, ?)''', ("root", "123456789"))
# # Сохранение изменений
# conn.commit()
# conn.close()
