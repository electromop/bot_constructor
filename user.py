import sqlite3

class User:
    def __init__(self, login):
        self.login = login
    
    def botsList(self):
        conn = sqlite3.connect('DB/users')
        
