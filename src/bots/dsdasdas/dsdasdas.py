import telebot
from telebot import types

bot_token = "dsadasdas"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    
    bot.send_message(message.chat.id, '''Привет! Я бот для погоды. Введите название города, чтобы узнать погоду.''')
#start_end

#help
@bot.message_handler(commands=['help'])
def help_message(message):
    
    bot.send_message(message.chat.id, '''Чтобы узнать погоду, введите название города. Например, Москва или Лондон.''')
#help_end

#settings
@bot.message_handler(commands=['settings'])
def settings_message(message):
    button_dict = {'Изменить город': {'text': 'Изменить город', 'callback': 'Изменить город'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Настройки''', reply_markup=markup)
#settings_end

#change_city
@bot.message_handler(commands=['change_city'])
def changecity_message(message):
    
    bot.send_message(message.chat.id, '''Введите новый город''')
#change_city_end

#Изменить город
@bot.callback_query_handler(func=lambda call: call.data == 'Изменить город')
def Izmenitgorod_callback(call):
    
    bot.send_message(call.message.chat.id, '''Введите новый город''')
#Изменить город_end

#Назад
@bot.callback_query_handler(func=lambda call: call.data == 'Назад')
def Nazad_callback(call):
    
    bot.send_message(call.message.chat.id, '''Вернуться в главное меню''')
#Назад_end

#Подробнее
@bot.callback_query_handler(func=lambda call: call.data == 'Подробнее')
def Podrobnee_callback(call):
    
    bot.send_message(call.message.chat.id, '''Показать подробную информацию о погоде''')
#Подробнее_end

#Прогноз
@bot.callback_query_handler(func=lambda call: call.data == 'Прогноз')
def Prognoz_callback(call):
    
    bot.send_message(call.message.chat.id, '''Показать прогноз на 7 дней''')
#Прогноз_end

#Настройки
@bot.callback_query_handler(func=lambda call: call.data == 'Настройки')
def Nastrojki_callback(call):
    button_dict = {'Изменить город': {'text': 'Изменить город', 'callback': 'Изменить город'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Настройки''', reply_markup=markup)
#Настройки_end
bot.polling()