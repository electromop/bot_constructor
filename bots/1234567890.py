import telebot
from telebot import types

bot_token = "1234567890"
bot = telebot.Bot(bot_token)
                        
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Хорошо': {'text': 'Хорошо', 'callback': 'Хорошо'}, 'Плохо': {'text': 'Плохо', 'callback': 'Плохо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)
#start_end
#Хорошо
@bot.callback_query_handler(func=lambda call: call.data == 'Хорошо')
def Horosho_callback(call):
    
    bot.send_message(call.message.chat.id, "Отлично, так держать!")
#Хорошо_end