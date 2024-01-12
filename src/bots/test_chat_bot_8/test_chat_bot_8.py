import telebot
from telebot import types

bot_token = "1234578"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Каталог': {'text': 'Каталог', 'callback': 'Каталог'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Привет! Я бот для продажи очков. Что бы вы хотели сделать?''', reply_markup=markup)
#start_end

#catalog
@bot.message_handler(commands=['catalog'])
def catalog_message(message):
    button_dict = {'Очки солнцезащитные': {'text': 'Очки солнцезащитные', 'callback': 'Очки солнцезащитные'}, 'Очки для чтения': {'text': 'Очки для чтения', 'callback': 'Очки для чтения'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Вот наш каталог очков. Выберите интересующую модель:''', reply_markup=markup)
#catalog_end

#contacts
@bot.message_handler(commands=['contacts'])
def contacts_message(message):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Наши контактные данные:
Телефон: +7*********
Email: example@example.com''', reply_markup=markup)
#contacts_end

#Очки солнцезащитные
@bot.callback_query_handler(func=lambda call: call.data == 'Очки солнцезащитные')
def Ochkisolntsezaschitnye_callback(call):
    button_dict = {'Заказать': {'text': 'Заказать', 'callback': 'Заказать'}, 'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Каталог солнцезащитных очков:
1. Модель 1
2. Модель 2
3. Модель 3''', reply_markup=markup)
#Очки солнцезащитные_end

#Очки для чтения
@bot.callback_query_handler(func=lambda call: call.data == 'Очки для чтения')
def Ochkidljachtenija_callback(call):
    button_dict = {'Заказать': {'text': 'Заказать', 'callback': 'Заказать'}, 'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Каталог очков для чтения:
1. Модель 1
2. Модель 2
3. Модель 3''', reply_markup=markup)
#Очки для чтения_end

#Заказать
@bot.callback_query_handler(func=lambda call: call.data == 'Заказать')
def Zakazat_callback(call):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы выбрали очки. Оставьте свои контактные данные, и наш менеджер свяжется с вами.''', reply_markup=markup)
#Заказать_end

#Назад
@bot.callback_query_handler(func=lambda call: call.data == 'Назад')
def Nazad_callback(call):
    button_dict = {'Очки солнцезащитные': {'text': 'Очки солнцезащитные', 'callback': 'Очки солнцезащитные'}, 'Очки для чтения': {'text': 'Очки для чтения', 'callback': 'Очки для чтения'}, 'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы вернулись в каталог.''', reply_markup=markup)
#Назад_end

#Главное меню
@bot.callback_query_handler(func=lambda call: call.data == 'Главное меню')
def Glavnoemenju_callback(call):
    button_dict = {'Каталог': {'text': 'Каталог', 'callback': 'Каталог'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы вернулись в главное меню. Что бы вы хотели сделать?''', reply_markup=markup)
#Главное меню_end
bot.polling()