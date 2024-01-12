import telebot
from telebot import types

bot_token = "dadasdasdasd"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'О нас': {'text': 'О нас', 'callback': 'О нас'}, 'Курсы': {'text': 'Курсы', 'callback': 'Курсы'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Добро пожаловать в наш бот! Выберите одну из команд ниже:''', reply_markup=markup)
#start_end

#about
@bot.message_handler(commands=['about'])
def about_message(message):
    button_dict = {'Курсы': {'text': 'Курсы', 'callback': 'Курсы'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Мы предлагаем широкий выбор курсов по разным тематикам. Наши преподаватели являются экспертами в своей области и помогут вам получить необходимые знания и навыки.''', reply_markup=markup)
#about_end

#courses
@bot.message_handler(commands=['courses'])
def courses_message(message):
    button_dict = {'Курс 1': {'text': 'Курс 1', 'callback': 'Курс 1'}, 'Курс 2': {'text': 'Курс 2', 'callback': 'Курс 2'}, 'Курс 3': {'text': 'Курс 3', 'callback': 'Курс 3'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Выберите интересующий вас курс из списка ниже:''', reply_markup=markup)
#courses_end

#course_1
@bot.message_handler(commands=['course_1'])
def course_message(message):
    button_dict = {'Записаться': {'text': 'Записаться', 'callback': 'Записаться'}, 'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Курс 1

Длительность: 10 занятий
Стоимость: 5000 рублей

Описание курса 1''', reply_markup=markup)
#course_1_end

#course_2
@bot.message_handler(commands=['course_2'])
def course_message(message):
    button_dict = {'Записаться': {'text': 'Записаться', 'callback': 'Записаться'}, 'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Курс 2

Длительность: 8 занятий
Стоимость: 4000 рублей

Описание курса 2''', reply_markup=markup)
#course_2_end

#course_3
@bot.message_handler(commands=['course_3'])
def course_message(message):
    button_dict = {'Записаться': {'text': 'Записаться', 'callback': 'Записаться'}, 'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Курс 3

Длительность: 12 занятий
Стоимость: 6000 рублей

Описание курса 3''', reply_markup=markup)
#course_3_end

#О нас
@bot.callback_query_handler(func=lambda call: call.data == 'О нас')
def Onas_callback(call):
    button_dict = {'Курсы': {'text': 'Курсы', 'callback': 'Курсы'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Мы предлагаем широкий выбор курсов по разным тематикам. Наши преподаватели являются экспертами в своей области и помогут вам получить необходимые знания и навыки.''', reply_markup=markup)
#О нас_end

#Курсы
@bot.callback_query_handler(func=lambda call: call.data == 'Курсы')
def Kursy_callback(call):
    button_dict = {'Курс 1': {'text': 'Курс 1', 'callback': 'Курс 1'}, 'Курс 2': {'text': 'Курс 2', 'callback': 'Курс 2'}, 'Курс 3': {'text': 'Курс 3', 'callback': 'Курс 3'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Выберите интересующий вас курс из списка ниже:''', reply_markup=markup)
#Курсы_end

#Контакты
@bot.callback_query_handler(func=lambda call: call.data == 'Контакты')
def Kontakty_callback(call):
    button_dict = {'О нас': {'text': 'О нас', 'callback': 'О нас'}, 'Курсы': {'text': 'Курсы', 'callback': 'Курсы'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Наши контактные данные:
Телефон: 8-800-123-45-67
Email: info@example.com''', reply_markup=markup)
#Контакты_end

#Курс 1
@bot.callback_query_handler(func=lambda call: call.data == 'Курс 1')
def Kurs_callback(call):
    button_dict = {'Записаться': {'text': 'Записаться', 'callback': 'Записаться'}, 'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Курс 1

Длительность: 10 занятий
Стоимость: 5000 рублей

Описание курса 1''', reply_markup=markup)
#Курс 1_end

#Курс 2
@bot.callback_query_handler(func=lambda call: call.data == 'Курс 2')
def Kurs_callback(call):
    button_dict = {'Записаться': {'text': 'Записаться', 'callback': 'Записаться'}, 'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Курс 2

Длительность: 8 занятий
Стоимость: 4000 рублей

Описание курса 2''', reply_markup=markup)
#Курс 2_end

#Курс 3
@bot.callback_query_handler(func=lambda call: call.data == 'Курс 3')
def Kurs_callback(call):
    button_dict = {'Записаться': {'text': 'Записаться', 'callback': 'Записаться'}, 'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Курс 3

Длительность: 12 занятий
Стоимость: 6000 рублей

Описание курса 3''', reply_markup=markup)
#Курс 3_end

#Курс 4
@bot.callback_query_handler(func=lambda call: call.data == 'Курс 4')
def Kurs_callback(call):
    button_dict = {'Узнать больше': {'text': 'Узнать больше', 'callback': 'Узнать больше'}, 'Записаться': {'text': 'Записаться', 'callback': 'Записаться'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Курс 4

Описание курса 4''', reply_markup=markup)
#Курс 4_end

#Курс 5
@bot.callback_query_handler(func=lambda call: call.data == 'Курс 5')
def Kurs_callback(call):
    button_dict = {'Узнать больше': {'text': 'Узнать больше', 'callback': 'Узнать больше'}, 'Записаться': {'text': 'Записаться', 'callback': 'Записаться'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Курс 5

Описание курса 5''', reply_markup=markup)
#Курс 5_end

#Узнать больше
@bot.callback_query_handler(func=lambda call: call.data == 'Узнать больше')
def Uznatbolshe_callback(call):
    
    bot.send_message(call.message.chat.id, '''Дополнительная информация о выбранном курсе''')
#Узнать больше_end

#Записаться
@bot.callback_query_handler(func=lambda call: call.data == 'Записаться')
def Zapisatsja_callback(call):
    
    bot.send_message(call.message.chat.id, '''Вы успешно записались на выбранный курс!''')
#Записаться_end
bot.polling()