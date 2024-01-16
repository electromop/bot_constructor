import os
from handlers import MessageHandler, CallbackHandler, CatalogHandler
from structure import JsonFileProcessor

class BotFile:
    def __init__(self, bot_name, bot_token):
        self.token = bot_token
        self.bot_path = f"bots/{bot_name}/{bot_name}.py"
        self.dir_path = f"bots/{bot_name}"

        if not os.path.exists(self.bot_path):
            os.makedirs(f"bots/{bot_name}", exist_ok=True)
            with open(self.dir_path +"/structure.json", 'w', encoding="utf-8") as f:
                f.write("[]")
            with open(self.bot_path, "w+", encoding="utf-8") as bot_file:
                bot_file.write(f'''import telebot
from telebot import types

bot_token = "{bot_token}"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END

bot.polling()
''')

    def _read_file(self):
        with open(self.bot_path, 'r', encoding="utf-8") as file:
            return file.read()

    def _write_file(self, content):
        with open(self.bot_path, 'w', encoding="utf-8") as file:
            file.write(content)

    def _update_handlers(self, handler):
        file_data = self._read_file()
        file_data = file_data.replace("bot.polling()", "")
        self._write_file(file_data + handler)

    def add_handler(self, handler_type, command, message_text, buttons=False, buttons_list=None, ncol=2):
        if self.is_command(command):
            return "Already exists"

        handler_class = MessageHandler if handler_type == 'simple' else CallbackHandler
        handler = handler_class(command, message_text, buttons, buttons_list=buttons_list, ncol=ncol)
        self._update_handlers(str(handler))

        structure_processor = JsonFileProcessor(self.dir_path)
        structure_processor.add_entry(handler_type, command, message_text, buttons, buttons_list)
        structure_processor.save_data()

        return "Success"

    def delete_handler(self, command):
        file_data = self._read_file()
        to_delete = file_data[file_data.find(f"#{command}"):file_data.find(f"#{command}_end") + len(command) + 5]
        new_bot_text = file_data.replace(to_delete, "")
        self._write_file(new_bot_text)

        structure_processor = JsonFileProcessor(self.dir_path)
        structure_processor.remove_entry_by_command_action(command)
        structure_processor.save_data()

    def edit_handler(self, command, text):
        file_data = self._read_file()
        to_edit = file_data[file_data.find(f"#{command}"):file_data.find(f"#{command}_end") + len(command) + 5]
        new_text = self.add_handler('simple', command, text)
        new_bot_text = file_data.replace(to_edit, new_text)
        self._write_file(new_bot_text)

        structure_processor = JsonFileProcessor(self.dir_path)
        structure_processor.update_command(command, text)
        structure_processor.save_data()

    def get_code(self):
        return self._read_file()
    
    def get_structure(self):
        structure = JsonFileProcessor(self.dir_path)
        return structure.get_data()

    def get_commands(self):
        structure_processor = JsonFileProcessor(self.dir_path)
        return structure_processor.get_command_names()

    def get_buttons(self):
        structure_processor = JsonFileProcessor(self.dir_path)
        return structure_processor.get_all_buttons()

    def is_command(self, command):
        with open(self.bot_path, 'r', encoding="utf-8") as f:
            filedata = f.read()
        return f'#{command}' in filedata

    def add_catalog(self, command, handler_type):
        if self.is_command(command):
            return "Already exists"
        
        handler_class = CatalogHandler
        handler = handler_class(handler_type)
        print(str(handler))
        self._update_handlers(str(handler))

        structure_processor = JsonFileProcessor(self.dir_path)
        structure_processor.add_entry(handler_type, command, '', '', [])
        structure_processor.save_data()

# bot = BotFile("bot_4_gpt", '')
# bot.add_catalog("simple", "catalog")
