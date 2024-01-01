from handlers import Handler
import os

class BotFile:
    def __init__(self, bot_token):
        self.token = bot_token
        self.bot_path = f"bots/{bot_token}.py"    
        bot_file = True if not os.path.exists(self.bot_path) else False
        if bot_file:
            bot_file = open(self.bot_path, "w+")
            bot_file.write(f'''import telebot

bot_token = "{bot_token}"
bot = telebot.Bot(bot_token)
                        ''')
            bot_file.close()

    def add_simple_handler(self, command, message_text):
        handler = Handler(0, command)
        bot_file = open(self.bot_path, "a+")
        bot_file.write(f"{handler.make(message_text)}")
        bot_file.close()

    def delete_simple_handler(self, command):
        bot_file = open(self.bot_path, "r")
        bot_text = bot_file.read()
        bot_file.close()

        to_delete = bot_text[bot_text.find(f"#{command}"):bot_text.find(f"#{command}_end") + len(command) + 5]

        new_bot_text = bot_text.replace(to_delete, "")

        bot_file = open(self.bot_path, "w")
        bot_file.write(new_bot_text)
        bot_file.close()
    
    def edit_simple_handler(self, command, text):
        bot_file = open(self.bot_path, "r")
        bot_text = bot_file.read()
        bot_file.close()

        to_delete = bot_text[bot_text.find(f"#{command}"):bot_text.find(f"#{command}_end") + len(command) + 5]

        new_bot_text = bot_text.replace(to_delete, "")

        bot_file = open(self.bot_path, "w")
        bot_file.write(new_bot_text)
        bot_file.close()

    def get_code(self):
        bot_file = open(self.bot_path, "r")
        bot_text = bot_file.read()
        bot_file.close()
        return bot_text
