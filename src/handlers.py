from keyboard import Keyboard
from transliterate import translit
import re

class MessageHandler:
    def __init__(self, key_word, text, buttons:bool=False, buttons_list=None, ncol=2):
        self.key_word = key_word
        self.buttons = buttons
        self.buttons_list = buttons_list if self.buttons else None
        self.ncol = ncol
        self.text = "'''" + text + "'''"

    def __str__(self):
        keyboard_space, markup = [Keyboard(self.buttons_list, ncol=self.ncol), ", reply_markup=markup"] if self.buttons else ["", ""]
        func_name = translit(self.key_word, language_code='ru', reversed=True)
        func_name = re.sub(r"[^a-zA-Z\s]| ", "", func_name)
        return f'''
#{self.key_word}
@bot.message_handler(commands=['{self.key_word}'])
def {func_name}_message(message):
    {keyboard_space}
    bot.send_message(message.chat.id, {self.text}{markup})
#{self.key_word}_end
bot.polling()'''
#КОСТЫЛЬ!!!!

class CallbackHandler:
    def __init__(self, callback_data, message, buttons:bool=False, buttons_list=None, ncol=2):
        self.callback_data = callback_data
        self.message = "'''" + message + "'''"
        self.buttons = buttons
        self.buttons_list = buttons_list if self.buttons else None
        self.ncol = ncol
    
    def __str__(self):
        keyboard_space, markup = [Keyboard(self.buttons_list, ncol=self.ncol), ", reply_markup=markup"] if self.buttons else ["", ""]
        func_name = translit(self.callback_data, language_code='ru', reversed=True)
        func_name = re.sub(r"[^a-zA-Z\s]| ", "", func_name)
        return f'''
#{self.callback_data}
@bot.callback_query_handler(func=lambda call: call.data == '{self.callback_data}')
def {func_name}_callback(call):
    {keyboard_space}
    bot.send_message(call.message.chat.id, {self.message}{markup})
#{self.callback_data}_end
bot.polling()'''
#КОСТЫЛЬ!!!!