import telebot
from telebot import types

bot_token = "dasdasdasdasd"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Кольца': {'text': 'Кольца', 'callback': 'Кольца'}, 'Браслеты': {'text': 'Браслеты', 'callback': 'Браслеты'}, 'Цепочки': {'text': 'Цепочки', 'callback': 'Цепочки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Привет! Я бот по продаже украшений. Что хочешь приобрести?''', reply_markup=markup)
#start_end

#Кольца
@bot.callback_query_handler(func=lambda call: call.data == 'Кольца')
def Koltsa_callback(call):
    button_dict = {'Размер 16': {'text': 'Размер 16', 'callback': 'Размер 16'}, 'Размер 18': {'text': 'Размер 18', 'callback': 'Размер 18'}, 'Золото': {'text': 'Золото', 'callback': 'Золото'}, 'Серебро': {'text': 'Серебро', 'callback': 'Серебро'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть разнообразные кольца. Какой размер и материал тебя интересует?''', reply_markup=markup)
#Кольца_end

#Браслеты
@bot.callback_query_handler(func=lambda call: call.data == 'Браслеты')
def Braslety_callback(call):
    button_dict = {'Размер S': {'text': 'Размер S', 'callback': 'Размер S'}, 'Размер M': {'text': 'Размер M', 'callback': 'Размер M'}, 'Плетеный': {'text': 'Плетеный', 'callback': 'Плетеный'}, 'Цепочечный': {'text': 'Цепочечный', 'callback': 'Цепочечный'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть стильные браслеты. Какой размер и дизайн тебя интересует?''', reply_markup=markup)
#Браслеты_end

#Цепочки
@bot.callback_query_handler(func=lambda call: call.data == 'Цепочки')
def Tsepochki_callback(call):
    button_dict = {'Длина 40 см': {'text': 'Длина 40 см', 'callback': 'Длина 40 см'}, 'Длина 50 см': {'text': 'Длина 50 см', 'callback': 'Длина 50 см'}, 'Золото': {'text': 'Золото', 'callback': 'Золото'}, 'Серебро': {'text': 'Серебро', 'callback': 'Серебро'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть разнообразные цепочки. Какой размер и материал тебя интересует?''', reply_markup=markup)
#Цепочки_end
bot.polling()