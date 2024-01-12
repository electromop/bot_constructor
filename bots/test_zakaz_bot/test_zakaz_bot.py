import telebot
from telebot import types

bot_token = "6788944411:AAFJDlLmpjvocCtNkgtTqsfSoYjU5UNWDc4"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Заказать сайт': {'text': 'Заказать сайт', 'callback': 'Заказать сайт'}, 'Узнать цены': {'text': 'Узнать цены', 'callback': 'Узнать цены'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Привет! Я бот-помощник для заказа разработки сайтов. Чем могу помочь?''', reply_markup=markup)
#start_end

#Заказать сайт
@bot.callback_query_handler(func=lambda call: call.data == 'Заказать сайт')
def Zakazatsajt_callback(call):
    button_dict = {'Готово': {'text': 'Готово', 'callback': 'Готово'}, 'Отмена': {'text': 'Отмена', 'callback': 'Отмена'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Оставьте свои контактные данные и мы свяжемся с вами для уточнения деталей заказа.''', reply_markup=markup)
#Заказать сайт_end

#Узнать цены
@bot.callback_query_handler(func=lambda call: call.data == 'Узнать цены')
def Uznattseny_callback(call):
    button_dict = {'Базовый пакет': {'text': 'Базовый пакет', 'callback': 'Базовый пакет'}, 'Продвинутый пакет': {'text': 'Продвинутый пакет', 'callback': 'Продвинутый пакет'}, 'Премиум пакет': {'text': 'Премиум пакет', 'callback': 'Премиум пакет'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть несколько пакетов разработки сайтов. Выберите интересующий вас:''', reply_markup=markup)
#Узнать цены_end

#Базовый пакет
@bot.callback_query_handler(func=lambda call: call.data == 'Базовый пакет')
def Bazovyjpaket_callback(call):
    button_dict = {'Заказать': {'text': 'Заказать', 'callback': 'Заказать'}, 'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Цена базового пакета: 10 000 рублей. Включает в себя установку и настройку CMS, адаптивную верстку и основные функциональные возможности.''', reply_markup=markup)
#Базовый пакет_end

#Продвинутый пакет
@bot.callback_query_handler(func=lambda call: call.data == 'Продвинутый пакет')
def Prodvinutyjpaket_callback(call):
    button_dict = {'Заказать': {'text': 'Заказать', 'callback': 'Заказать'}, 'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Цена продвинутого пакета: 20 000 рублей. Включает в себя все функции базового пакета, а также дополнительные возможности для расширения функциональности сайта.''', reply_markup=markup)
#Продвинутый пакет_end

#Премиум пакет
@bot.callback_query_handler(func=lambda call: call.data == 'Премиум пакет')
def Premiumpaket_callback(call):
    button_dict = {'Заказать': {'text': 'Заказать', 'callback': 'Заказать'}, 'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Цена премиум пакета: 30 000 рублей. Включает в себя все функции продвинутого пакета, а также дизайн сайта по вашим требованиям.''', reply_markup=markup)
#Премиум пакет_end

#Готово
@bot.callback_query_handler(func=lambda call: call.data == 'Готово')
def Gotovo_callback(call):
    button_dict = {'Отмена': {'text': 'Отмена', 'callback': 'Отмена'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Пожалуйста, отправьте ваше имя, номер телефона и электронную почту для связи.''', reply_markup=markup)
#Готово_end

#Отмена
@bot.callback_query_handler(func=lambda call: call.data == 'Отмена')
def Otmena_callback(call):
    
    bot.send_message(call.message.chat.id, '''Заказ отменен. Если у вас возникнут вопросы, вы всегда можете связаться с нами по телефону или электронной почте.''')
#Отмена_end

#Назад
@bot.callback_query_handler(func=lambda call: call.data == 'Назад')
def Nazad_callback(call):
    button_dict = {'Базовый пакет': {'text': 'Базовый пакет', 'callback': 'Базовый пакет'}, 'Продвинутый пакет': {'text': 'Продвинутый пакет', 'callback': 'Продвинутый пакет'}, 'Премиум пакет': {'text': 'Премиум пакет', 'callback': 'Премиум пакет'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Выберите интересующий вас пакет разработки сайта:''', reply_markup=markup)
#Назад_end
bot.polling()