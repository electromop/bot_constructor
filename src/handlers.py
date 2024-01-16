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
    
class CatalogHandler:
    def __init__(self, command, handler_type="simple"):
        self.command = command
        self.handler_type = handler_type

    def __str__(self):
        route = f'@bot.callback_query_handler(func= lambda call: call.data == "{self.command}")\n' if self.handler_type != 'simple' else f"@bot.message_handler(commands=['{self.command}'])\n"
        return route + '''
def browse_cat(call):
    bot.answer_callback_query(call.id, "")
    catalog = Catalog()
    button_dict = {'Вперед': {'text': 'Вперед', 'callback': 'Вперед1'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    product_info = catalog.get_product_info(1)
    bot.send_message(call.message.chat.id, str(product_info), reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data[:6] == "Вперед")
def next(call):
    bot.answer_callback_query(call.id, "")
    catalog = Catalog()
    product_id = int(call.data[6:]) + 1
    
    button_dict = {'Вперед': {'text': 'Вперед', 'callback': f'Вперед{product_id}'}, 'Назад': {'text': 'Назад', 'callback': f'Назад{product_id}'}}
    if product_id == len(catalog):
        del button_dict['Вперед']
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)

    product_info = catalog.get_product_info(product_id)
    bot.edit_message_text(text=product_info, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data[:5] == "Назад")
def previous(call):
    bot.answer_callback_query(call.id, "")
    catalog = Catalog()
    product_id = int(call.data[5:]) - 1

    button_dict = {'Вперед': {'text': 'Вперед', 'callback': f'Вперед{product_id}'}, 'Назад': {'text': 'Назад', 'callback': f'Назад{product_id}'}}
    if product_id == 1:
        del button_dict['Назад']
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)

    product_info = catalog.get_product_info(product_id)
    bot.edit_message_text(text=product_info, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=markup)

bot.polling()'''