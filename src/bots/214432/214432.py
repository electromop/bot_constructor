import telebot
from telebot import types

bot_token = "3432423423"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Каталог курсов': {'text': 'Каталог курсов', 'callback': 'Каталог курсов'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Привет! Я бот по продаже информационных курсов. Чтобы узнать больше о доступных курсах, нажми на кнопку 'Каталог курсов'''', reply_markup=markup)
#start_end

#help
@bot.message_handler(commands=['help'])
def help_message(message):
    button_dict = {'Каталог курсов': {'text': 'Каталог курсов', 'callback': 'Каталог курсов'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Этот бот поможет тебе выбрать подходящий информационный курс. Чтобы узнать больше о доступных курсах, нажми на кнопку 'Каталог курсов'''', reply_markup=markup)
#help_end

#catalog
@bot.message_handler(commands=['catalog'])
def catalog_message(message):
    button_dict = {'Курс 1': {'text': 'Курс 1', 'callback': 'Курс 1'}, 'Курс 2': {'text': 'Курс 2', 'callback': 'Курс 2'}, 'Курс 3': {'text': 'Курс 3', 'callback': 'Курс 3'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Вот список доступных курсов:''', reply_markup=markup)
#catalog_end

#Курс 1
@bot.callback_query_handler(func=lambda call: call.data == 'Курс 1')
def Kurs_callback(call):
    button_dict = {'Купить': {'text': 'Купить', 'callback': 'Купить'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Описание курса 1''', reply_markup=markup)
#Курс 1_end

#Курс 2
@bot.callback_query_handler(func=lambda call: call.data == 'Курс 2')
def Kurs_callback(call):
    button_dict = {'Купить': {'text': 'Купить', 'callback': 'Купить'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Описание курса 2''', reply_markup=markup)
#Курс 2_end

#Курс 3
@bot.callback_query_handler(func=lambda call: call.data == 'Курс 3')
def Kurs_callback(call):
    button_dict = {'Купить': {'text': 'Купить', 'callback': 'Купить'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Описание курса 3''', reply_markup=markup)
#Курс 3_end

#Купить
@bot.callback_query_handler(func=lambda call: call.data == 'Купить')
def Kupit_callback(call):
    
    bot.send_message(call.message.chat.id, '''Спасибо за покупку! Мы отправим информацию о курсе на указанный вами email.''')
#Купить_end
bot.polling()