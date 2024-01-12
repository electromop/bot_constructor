import telebot
from telebot import types

bot_token = "hg"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Курс 1': {'text': 'Курс 1', 'callback': 'Курс 1'}, 'Курс 2': {'text': 'Курс 2', 'callback': 'Курс 2'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Добро пожаловать в наш бот! Выберите курс, который вас интересует''', reply_markup=markup)
#start_end

#Курс 1
@bot.callback_query_handler(func=lambda call: call.data == 'Курс 1')
def Kurs_callback(call):
    button_dict = {'Написать в чат': {'text': 'Написать в чат', 'callback': 'Написать в чат'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы выбрали Курс 1. Для получения подробной информации о курсе напишите нам в чат''', reply_markup=markup)
#Курс 1_end

#Курс 2
@bot.callback_query_handler(func=lambda call: call.data == 'Курс 2')
def Kurs_callback(call):
    button_dict = {'Написать в чат': {'text': 'Написать в чат', 'callback': 'Написать в чат'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы выбрали Курс 2. Для получения подробной информации о курсе напишите нам в чат''', reply_markup=markup)
#Курс 2_end

#Написать в чат
@bot.callback_query_handler(func=lambda call: call.data == 'Написать в чат')
def Napisatvchat_callback(call):
    button_dict = {'Курс 1': {'text': 'Курс 1', 'callback': 'Курс 1'}, 'Курс 2': {'text': 'Курс 2', 'callback': 'Курс 2'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время''', reply_markup=markup)
#Написать в чат_end
bot.polling()