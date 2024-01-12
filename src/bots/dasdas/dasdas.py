import telebot
from telebot import types

bot_token = "dasdasdas"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Коровье': {'text': 'Коровье', 'callback': 'Коровье'}, 'Собачье': {'text': 'Собачье', 'callback': 'Собачье'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Привет! Я бот для продажи какашек. Что бы ты хотел приобрести?''', reply_markup=markup)
#start_end

#buy
@bot.message_handler(commands=['buy'])
def buy_message(message):
    button_dict = {'1 упаковка': {'text': '1 упаковка', 'callback': '1 упаковка'}, '2 упаковки': {'text': '2 упаковки', 'callback': '2 упаковки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Отлично! Сколько упаковок ты хочешь приобрести?''', reply_markup=markup)
#buy_end

#confirm
@bot.message_handler(commands=['confirm'])
def confirm_message(message):
    
    bot.send_message(message.chat.id, '''Ты выбрал 1 упаковку. Теперь введи свои контактные данные для доставки.''')
#confirm_end

#cancel
@bot.message_handler(commands=['cancel'])
def cancel_message(message):
    button_dict = {'Продолжить покупки': {'text': 'Продолжить покупки', 'callback': 'Продолжить покупки'}, 'Связаться с поддержкой': {'text': 'Связаться с поддержкой', 'callback': 'Связаться с поддержкой'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Твой заказ отменен. Что желаешь сделать дальше?''', reply_markup=markup)
#cancel_end

#Коровье
@bot.callback_query_handler(func=lambda call: call.data == 'Коровье')
def Korove_callback(call):
    button_dict = {'1 упаковка': {'text': '1 упаковка', 'callback': '1 упаковка'}, '2 упаковки': {'text': '2 упаковки', 'callback': '2 упаковки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Отличный выбор! Сколько упаковок ты хочешь приобрести?''', reply_markup=markup)
#Коровье_end

#Собачье
@bot.callback_query_handler(func=lambda call: call.data == 'Собачье')
def Sobache_callback(call):
    button_dict = {'1 упаковка': {'text': '1 упаковка', 'callback': '1 упаковка'}, '2 упаковки': {'text': '2 упаковки', 'callback': '2 упаковки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Хороший выбор! Сколько упаковок ты хочешь приобрести?''', reply_markup=markup)
#Собачье_end

#1 упаковка
@bot.callback_query_handler(func=lambda call: call.data == '1 упаковка')
def upakovka_callback(call):
    
    bot.send_message(call.message.chat.id, '''Ты выбрал 1 упаковку. Теперь введи свои контактные данные для доставки.''')
#1 упаковка_end

#2 упаковки
@bot.callback_query_handler(func=lambda call: call.data == '2 упаковки')
def upakovki_callback(call):
    
    bot.send_message(call.message.chat.id, '''Ты выбрал 2 упаковки. Теперь введи свои контактные данные для доставки.''')
#2 упаковки_end

#Продолжить покупки
@bot.callback_query_handler(func=lambda call: call.data == 'Продолжить покупки')
def Prodolzhitpokupki_callback(call):
    button_dict = {'Коровье': {'text': 'Коровье', 'callback': 'Коровье'}, 'Собачье': {'text': 'Собачье', 'callback': 'Собачье'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Что бы ты хотел приобрести?''', reply_markup=markup)
#Продолжить покупки_end

#Связаться с поддержкой
@bot.callback_query_handler(func=lambda call: call.data == 'Связаться с поддержкой')
def Svjazatsjaspodderzhkoj_callback(call):
    
    bot.send_message(call.message.chat.id, '''Ты можешь связаться с нами по номеру 8-800-555-35-35 или отправить письмо на support@poopstore.com.''')
#Связаться с поддержкой_end
bot.polling()