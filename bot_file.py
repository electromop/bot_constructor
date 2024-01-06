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
#COMMANDS_LIST#COMMANDS_LIST_END
''')
            bot_file.close()

    def add_simple_handler(self, command, message_text, buttons=False, buttons_list=None, ncol=2):
        if self.is_command(command):
            return "Already exists"
        else:
            with open(self.bot_path, 'r', encoding="utf-8") as file:
                filedata = file.read()

            handler = MessageHandler(command, message_text, buttons, buttons_list=buttons_list, ncol=ncol)
            old_commands = filedata[filedata.find("#COMMANDS_LIST"):filedata.find("#COMMANDS_LIST_END")+18]
            new_commands = old_commands[:14] + old_commands[14:old_commands.find("#COMMANDS_LIST_END")] + f'{command},' + old_commands[old_commands.find("#COMMANDS_LIST_END"):]
            filedata = filedata.replace(old_commands, new_commands)

            with open(self.bot_path, 'w', encoding="utf-8") as file:
                file.write(filedata)
                file.write(f"{handler}")
            return "Success"
        
    
    def add_query_handler(self, callback_data, text, buttons=False, buttons_list=None, ncol=2):
        if self.is_command(callback_data):
            return "Already exists"
        else:
            with open(self.bot_path, 'r', encoding="utf-8") as file:
                filedata = file.read()

            handler = CallbackHandler(callback_data, text, buttons, buttons_list=buttons_list, ncol=ncol)
            old_commands = filedata[filedata.find("#COMMANDS_LIST"):filedata.find("#COMMANDS_LIST_END")+18]
            new_commands = old_commands[:14] + old_commands[14:old_commands.find("#COMMANDS_LIST_END")] + f'{callback_data},' + old_commands[old_commands.find("#COMMANDS_LIST_END"):]
            filedata = filedata.replace(old_commands, new_commands)

            with open(self.bot_path, 'w', encoding="utf-8") as file:
                file.write(filedata)
                file.write(f"{handler}")
            return "Success"

    def delete_simple_handler(self, command):
        bot_file = open(self.bot_path, "r", encoding="utf-8")
        bot_text = bot_file.read()
        bot_file.close()

        to_delete = bot_text[bot_text.find(f"#{command}"):bot_text.find(f"#{command}_end") + len(command) + 5]

        new_bot_text = bot_text.replace(to_delete, "")

        bot_file = open(self.bot_path, "w", encoding="utf-8")
        bot_file.write(new_bot_text)
        bot_file.close()
    
    def edit_simple_handler(self, command, text):
        bot_file = open(self.bot_path, "r", encoding="utf-8")
        bot_text = bot_file.read()
        bot_file.close()

        to_edit = bot_text[bot_text.find(f"#{command}"):bot_text.find(f"#{command}_end") + len(command) + 5]
        new_text = self.add_simple_handler(command, text)

        new_bot_text = bot_text.replace(to_edit, new_text)

        bot_file = open(self.bot_path, "w", encoding="utf-8")
        bot_file.write(new_bot_text)
        bot_file.close()

    def get_code(self):
        bot_file = open(self.bot_path, "r", encoding="utf-8")
        bot_text = bot_file.read()
        bot_file.close()
        return bot_text
    
    def get_commands(self):
        bot_file = open(self.bot_path, "r", encoding="utf-8")
        bot_text = bot_file.read()
        self.commands_list = bot_text[bot_text.find(f"#COMMANDS_LIST")+14:bot_text.find(f"#COMMANDS_LIST_END") + 14 + 5]
        bot_file.close()
        return self.commands_list.split(',')[:-1]
    
    def is_command(self, command):
        with open(self.bot_path, 'r', encoding="utf-8") as f:
            filedata = f.read()
        return True if f'#{command}' in filedata else False
    

# bot = BotFile("1234567890")
# bot.add_simple_handler("start", "Привет! Как дела?", buttons=True, buttons_list=["Хорошо", "Плохо"], ncol=2)
# bot.add_query_handler("Хорошо", "Отлично, так держать!")
# print(bot.get_commands())