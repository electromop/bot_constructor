from handlers import MessageHandler, CallbackHandler
import os
import re

class BotFile:
    def __init__(self, bot_token):
        self.token = bot_token
        self.bot_path = f"bots/{bot_token}.py"    
        bot_file = True if not os.path.exists(self.bot_path) else False
        if bot_file:
            bot_file = open(self.bot_path, "w+")
            bot_file.write(f'''import telebot
from telebot import types

bot_token = "{bot_token}"
bot = telebot.Bot(bot_token)
#COMMANDS_LIST
#COMMANDS_LIST_END
''')
            bot_file.close()

    def add_simple_handler(self, command, message_text, buttons=False, buttons_list=None, ncol=2):
        handler = MessageHandler(command, message_text, buttons, buttons_list=buttons_list, ncol=ncol)
        bot_file = open(self.bot_path, "a+")
        bot_text = bot_file.read()

        old_commands = bot_text[bot_text.find(f"#COMMANDS_LIST")+14:bot_text.find(f"#COMMANDS_LIST_END") + 14 + 5]
        new_commands = old_commands + f',{command}'

        bot_text.replace(old_commands, new_commands)
        print(new_commands)
        bot_file.write(f"{handler}")
        bot_file.close()
    
    def add_query_handler(self, callback_data, text, buttons=False, buttons_list=None, ncol=2):
        handler = CallbackHandler(callback_data, text, buttons=buttons, buttons_list=buttons_list, ncol=ncol)
        bot_file = open(self.bot_path, "a+")

        bot_text = bot_file.read()

        old_commands = bot_text[bot_text.find(f"#COMMANDS_LIST"):bot_text.find(f"#COMMANDS_LIST_END")]
        print(old_commands)
        new_commands = old_commands + f',{callback_data}'

        bot_text.replace(old_commands, new_commands)
        print(new_commands)

        bot_file.write(f"{handler}")
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

        to_edit = bot_text[bot_text.find(f"#{command}"):bot_text.find(f"#{command}_end") + len(command) + 5]
        new_text = self.add_simple_handler(command, text)

        new_bot_text = bot_text.replace(to_edit, new_text)

        bot_file = open(self.bot_path, "w")
        bot_file.write(new_bot_text)
        bot_file.close()

    def get_code(self):
        bot_file = open(self.bot_path, "r")
        bot_text = bot_file.read()
        bot_file.close()
        return bot_text
    
    def get_commands(self):
        bot_file = open(self.bot_path, "r")
        bot_text = bot_file.read()
        self.commands_list = bot_text[bot_text.find(f"#COMMANDS_LIST")+14:bot_text.find(f"#COMMANDS_LIST_END") + 14 + 5]
        bot_file.close()
        return self.commands_list.split(',')

bot = BotFile("1234567890")
bot.add_simple_handler("start", "Привет! Как дела?", buttons=True, buttons_list=["Хорошо", "Плохо"], ncol=2)
bot.add_query_handler("Хорошо", "Отлично, так держать!")