import telebot
from telebot import types

bot_token = "6788944411:AAFJDlLmpjvocCtNkgtTqsfSoYjU5UNWDc4"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Да': {'text': 'Да', 'callback': 'Да'}, 'Нет': {'text': 'Нет', 'callback': 'Нет'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Привет! Я бот для продажи какашек. Хочешь купить какашку?''', reply_markup=markup)
#start_end

#Да
@bot.callback_query_handler(func=lambda call: call.data == 'Да')
def Da_callback(call):
    button_dict = {'Обычная': {'text': 'Обычная', 'callback': 'Обычная'}, 'Золотая': {'text': 'Золотая', 'callback': 'Золотая'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Отлично! У нас есть разные варианты какашек. Выбери нужный.''', reply_markup=markup)
#Да_end

#Нет
@bot.callback_query_handler(func=lambda call: call.data == 'Нет')
def Net_callback(call):
    
    bot.send_message(call.message.chat.id, '''Жаль! Если передумаешь, я всегда здесь.''')
#Нет_end

#Обычная
@bot.callback_query_handler(func=lambda call: call.data == 'Обычная')
def Obychnaja_callback(call):
    button_dict = {'Оформить': {'text': 'Оформить', 'callback': 'Оформить'}, 'Отказаться': {'text': 'Отказаться', 'callback': 'Отказаться'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Обычная какашка стоит 5 рублей. Желаешь оформить заказ?''', reply_markup=markup)
#Обычная_end

#Золотая
@bot.callback_query_handler(func=lambda call: call.data == 'Золотая')
def Zolotaja_callback(call):
    button_dict = {'Оформить': {'text': 'Оформить', 'callback': 'Оформить'}, 'Отказаться': {'text': 'Отказаться', 'callback': 'Отказаться'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Золотая какашка стоит 100 рублей. Желаешь оформить заказ?''', reply_markup=markup)
#Золотая_end

#Оформить
@bot.callback_query_handler(func=lambda call: call.data == 'Оформить')
def Oformit_callback(call):
    
    bot.send_message(call.message.chat.id, '''Спасибо за заказ! Ваша какашка будет доставлена в ближайшее время.''')
#Оформить_end

#Отказаться
@bot.callback_query_handler(func=lambda call: call.data == 'Отказаться')
def Otkazatsja_callback(call):
    
    bot.send_message(call.message.chat.id, '''Жаль! Надеемся, что вы вернетесь.''')
#Отказаться_end
bot.polling()