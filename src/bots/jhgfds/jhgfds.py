import telebot
from telebot import types

bot_token = "hgfd"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    
    bot.send_message(message.chat.id, '''Приветствую! Добро пожаловать в бот для анализа финансового состояния компаний. Чтобы начать, отправьте мне название компании, по которой хотите получить данные.''')
#start_end

#help
@bot.message_handler(commands=['help'])
def help_message(message):
    
    bot.send_message(message.chat.id, '''Данный бот предназначен для анализа финансового состояния компаний. Он предоставляет информацию о доходах, расходах, прибыли, активах и других показателях компании. Чтобы получить информацию о конкретной компании, отправьте ее название.''')
#help_end

#info
@bot.message_handler(commands=['info'])
def info_message(message):
    
    bot.send_message(message.chat.id, '''Данный бот предназначен для анализа финансового состояния компаний. Он предоставляет информацию о доходах, расходах, прибыли, активах и других показателях компании. Чтобы получить информацию о конкретной компании, отправьте ее название.''')
#info_end

#company
@bot.message_handler(commands=['company'])
def company_message(message):
    
    bot.send_message(message.chat.id, '''Введите название компании, по которой хотите получить информацию.''')
#company_end

#analysis
@bot.message_handler(commands=['analysis'])
def analysis_message(message):
    button_dict = {'Выручка': {'text': 'Выручка', 'callback': 'Выручка'}, 'Чистая прибыль': {'text': 'Чистая прибыль', 'callback': 'Чистая прибыль'}, 'Активы': {'text': 'Активы', 'callback': 'Активы'}, 'Долги': {'text': 'Долги', 'callback': 'Долги'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Выберите показатель, по которому хотите проанализировать финансовое состояние компании''', reply_markup=markup)
#analysis_end

#Выручка
@bot.callback_query_handler(func=lambda call: call.data == 'Выручка')
def Vyruchka_callback(call):
    button_dict = {'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Выручка - это сумма денег, полученных компанией от реализации своих товаров или услуг.''', reply_markup=markup)
#Выручка_end

#Чистая прибыль
@bot.callback_query_handler(func=lambda call: call.data == 'Чистая прибыль')
def Chistajapribyl_callback(call):
    button_dict = {'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Чистая прибыль - это прибыль, полученная компанией после вычета всех расходов и налогов.''', reply_markup=markup)
#Чистая прибыль_end

#Активы
@bot.callback_query_handler(func=lambda call: call.data == 'Активы')
def Aktivy_callback(call):
    button_dict = {'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Активы - это все ресурсы, которыми компания владеет и которые могут принести ей экономическую выгоду.''', reply_markup=markup)
#Активы_end

#Долги
@bot.callback_query_handler(func=lambda call: call.data == 'Долги')
def Dolgi_callback(call):
    button_dict = {'Назад': {'text': 'Назад', 'callback': 'Назад'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Долги - это финансовые обязательства компании перед другими лицами или организациями.''', reply_markup=markup)
#Долги_end

#Назад
@bot.callback_query_handler(func=lambda call: call.data == 'Назад')
def Nazad_callback(call):
    button_dict = {'Выручка': {'text': 'Выручка', 'callback': 'Выручка'}, 'Чистая прибыль': {'text': 'Чистая прибыль', 'callback': 'Чистая прибыль'}, 'Активы': {'text': 'Активы', 'callback': 'Активы'}, 'Долги': {'text': 'Долги', 'callback': 'Долги'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Выберите показатель, по которому хотите проанализировать финансовое состояние компании''', reply_markup=markup)
#Назад_end
bot.polling()