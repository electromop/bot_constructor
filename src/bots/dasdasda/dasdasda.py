import telebot
from telebot import types

bot_token = "dasdasdas"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Каталог товаров': {'text': 'Каталог товаров', 'callback': 'Каталог товаров'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Добро пожаловать в наш магазин игрушек! Выберите действие''', reply_markup=markup)
#start_end

#catalog
@bot.message_handler(commands=['catalog'])
def catalog_message(message):
    button_dict = {'Плюшевые игрушки': {'text': 'Плюшевые игрушки', 'callback': 'Плюшевые игрушки'}, 'Игры и головоломки': {'text': 'Игры и головоломки', 'callback': 'Игры и головоломки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Вот наш каталог товаров. Что вас интересует?''', reply_markup=markup)
#catalog_end

#Плюшевые игрушки
@bot.callback_query_handler(func=lambda call: call.data == 'Плюшевые игрушки')
def Pljushevyeigrushki_callback(call):
    button_dict = {'Купить': {'text': 'Купить', 'callback': 'Купить'}, 'Вернуться в каталог': {'text': 'Вернуться в каталог', 'callback': 'Вернуться в каталог'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Плюшевые игрушки: мишки, котики, зайцы''', reply_markup=markup)
#Плюшевые игрушки_end

#Игры и головоломки
@bot.callback_query_handler(func=lambda call: call.data == 'Игры и головоломки')
def Igryigolovolomki_callback(call):
    button_dict = {'Купить': {'text': 'Купить', 'callback': 'Купить'}, 'Вернуться в каталог': {'text': 'Вернуться в каталог', 'callback': 'Вернуться в каталог'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Игры и головоломки: шахматы, кубики, рубикова кубика''', reply_markup=markup)
#Игры и головоломки_end

#Купить
@bot.callback_query_handler(func=lambda call: call.data == 'Купить')
def Kupit_callback(call):
    button_dict = {'Каталог товаров': {'text': 'Каталог товаров', 'callback': 'Каталог товаров'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Спасибо за покупку! Мы отправим ваш заказ в ближайшее время''', reply_markup=markup)
#Купить_end

#Вернуться в каталог
@bot.callback_query_handler(func=lambda call: call.data == 'Вернуться в каталог')
def Vernutsjavkatalog_callback(call):
    button_dict = {'Плюшевые игрушки': {'text': 'Плюшевые игрушки', 'callback': 'Плюшевые игрушки'}, 'Игры и головоломки': {'text': 'Игры и головоломки', 'callback': 'Игры и головоломки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вот наш каталог товаров. Что вас интересует?''', reply_markup=markup)
#Вернуться в каталог_end
bot.polling()