import telebot
from telebot import types

bot_token = "6434108320:AAHcb8OpYIPpTKEpCFcpkD0zgl32HmLGMcM"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LISTstart,Расписание,Материалы,Контакты,11.05,12.05,13.05,Видеоуроки,Статьи,Телефон,Email,Подробности,Урок 1,Урок 2,Урок 3,Статья 1,Статья 2,Статья 3,Задать вопрос,#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Расписание': {'text': 'Расписание', 'callback': 'Расписание'}, 'Материалы': {'text': 'Материалы', 'callback': 'Материалы'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''/start''', reply_markup=markup)
#start_end

#Расписание
@bot.callback_query_handler(func=lambda call: call.data == 'Расписание')
def Raspisanie_callback(call):
    button_dict = {'11.05': {'text': '11.05', 'callback': '11.05'}, '12.05': {'text': '12.05', 'callback': '12.05'}, '13.05': {'text': '13.05', 'callback': '13.05'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Здесь вы найдете расписание занятий''', reply_markup=markup)
#Расписание_end

#Материалы
@bot.callback_query_handler(func=lambda call: call.data == 'Материалы')
def Materialy_callback(call):
    button_dict = {'Видеоуроки': {'text': 'Видеоуроки', 'callback': 'Видеоуроки'}, 'Статьи': {'text': 'Статьи', 'callback': 'Статьи'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Здесь вы найдете материалы для обучения''', reply_markup=markup)
#Материалы_end

#Контакты
@bot.callback_query_handler(func=lambda call: call.data == 'Контакты')
def Kontakty_callback(call):
    button_dict = {'Телефон': {'text': 'Телефон', 'callback': 'Телефон'}, 'Email': {'text': 'Email', 'callback': 'Email'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Свяжитесь с нами''', reply_markup=markup)
#Контакты_end

#11.05
@bot.callback_query_handler(func=lambda call: call.data == '11.05')
def _callback(call):
    button_dict = {'Подробности': {'text': 'Подробности', 'callback': 'Подробности'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Занятие 11.05: Тема: XXXX''', reply_markup=markup)
#11.05_end

#12.05
@bot.callback_query_handler(func=lambda call: call.data == '12.05')
def _callback(call):
    button_dict = {'Подробности': {'text': 'Подробности', 'callback': 'Подробности'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Занятие 12.05: Тема: XXXX''', reply_markup=markup)
#12.05_end

#13.05
@bot.callback_query_handler(func=lambda call: call.data == '13.05')
def _callback(call):
    button_dict = {'Подробности': {'text': 'Подробности', 'callback': 'Подробности'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Занятие 13.05: Тема: XXXX''', reply_markup=markup)
#13.05_end

#Видеоуроки
@bot.callback_query_handler(func=lambda call: call.data == 'Видеоуроки')
def Videouroki_callback(call):
    button_dict = {'Урок 1': {'text': 'Урок 1', 'callback': 'Урок 1'}, 'Урок 2': {'text': 'Урок 2', 'callback': 'Урок 2'}, 'Урок 3': {'text': 'Урок 3', 'callback': 'Урок 3'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Здесь вы найдете видеоуроки''', reply_markup=markup)
#Видеоуроки_end

#Статьи
@bot.callback_query_handler(func=lambda call: call.data == 'Статьи')
def Stati_callback(call):
    button_dict = {'Статья 1': {'text': 'Статья 1', 'callback': 'Статья 1'}, 'Статья 2': {'text': 'Статья 2', 'callback': 'Статья 2'}, 'Статья 3': {'text': 'Статья 3', 'callback': 'Статья 3'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Здесь вы найдете статьи''', reply_markup=markup)
#Статьи_end

#Телефон
@bot.callback_query_handler(func=lambda call: call.data == 'Телефон')
def Telefon_callback(call):
    button_dict = {'Задать вопрос': {'text': 'Задать вопрос', 'callback': 'Задать вопрос'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Наш телефон: +123456789''', reply_markup=markup)
#Телефон_end

#Email
@bot.callback_query_handler(func=lambda call: call.data == 'Email')
def Email_callback(call):
    button_dict = {'Задать вопрос': {'text': 'Задать вопрос', 'callback': 'Задать вопрос'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Наш Email: example@example.com''', reply_markup=markup)
#Email_end

#Подробности
@bot.callback_query_handler(func=lambda call: call.data == 'Подробности')
def Podrobnosti_callback(call):
    
    bot.send_message(call.message.chat.id, '''Здесь вы найдете подробности занятия''')
#Подробности_end

#Урок 1
@bot.callback_query_handler(func=lambda call: call.data == 'Урок 1')
def Urok_callback(call):
    button_dict = {'Подробности': {'text': 'Подробности', 'callback': 'Подробности'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Урок 1: Тема: XXXX''', reply_markup=markup)
#Урок 1_end

#Урок 2
@bot.callback_query_handler(func=lambda call: call.data == 'Урок 2')
def Urok_callback(call):
    button_dict = {'Подробности': {'text': 'Подробности', 'callback': 'Подробности'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Урок 2: Тема: XXXX''', reply_markup=markup)
#Урок 2_end

#Урок 3
@bot.callback_query_handler(func=lambda call: call.data == 'Урок 3')
def Urok_callback(call):
    button_dict = {'Подробности': {'text': 'Подробности', 'callback': 'Подробности'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Урок 3: Тема: XXXX''', reply_markup=markup)
#Урок 3_end

#Статья 1
@bot.callback_query_handler(func=lambda call: call.data == 'Статья 1')
def Statja_callback(call):
    button_dict = {'Подробности': {'text': 'Подробности', 'callback': 'Подробности'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Статья 1: Тема: XXXX''', reply_markup=markup)
#Статья 1_end

#Статья 2
@bot.callback_query_handler(func=lambda call: call.data == 'Статья 2')
def Statja_callback(call):
    button_dict = {'Подробности': {'text': 'Подробности', 'callback': 'Подробности'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Статья 2: Тема: XXXX''', reply_markup=markup)
#Статья 2_end

#Статья 3
@bot.callback_query_handler(func=lambda call: call.data == 'Статья 3')
def Statja_callback(call):
    button_dict = {'Подробности': {'text': 'Подробности', 'callback': 'Подробности'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Статья 3: Тема: XXXX''', reply_markup=markup)
#Статья 3_end

#Задать вопрос
@bot.callback_query_handler(func=lambda call: call.data == 'Задать вопрос')
def Zadatvopros_callback(call):
    
    bot.send_message(call.message.chat.id, '''Задайте ваш вопрос''')
#Задать вопрос_end
bot.polling()