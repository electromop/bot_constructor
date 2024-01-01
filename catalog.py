import sqlite3

class Catalog:

    def __init__(self, botToken):
        self.catalogTable = sqlite3.connect("bots/botToken/database/")

    def get_item(self):
        pass