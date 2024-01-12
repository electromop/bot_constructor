import telebot
from telebot import types

bot_token = "asdasdasd"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Записаться': {'text': 'Записаться', 'callback': 'Записаться'}, 'Прайс лист': {'text': 'Прайс лист', 'callback': 'Прайс лист'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Добро пожаловать в бот для записи на услуги ноготочков! Выберите нужное действие:''', reply_markup=markup)
#start_end

#Записаться
@bot.message_handler(commands=['Записаться'])
def Zapisatsja_message(message):
    button_dict = {'9:00': {'text': '9:00', 'callback': '9:00'}, '10:00': {'text': '10:00', 'callback': '10:00'}, '11:00': {'text': '11:00', 'callback': '11:00'}, '12:00': {'text': '12:00', 'callback': '12:00'}, '13:00': {'text': '13:00', 'callback': '13:00'}, '14:00': {'text': '14:00', 'callback': '14:00'}, '15:00': {'text': '15:00', 'callback': '15:00'}, '16:00': {'text': '16:00', 'callback': '16:00'}, '17:00': {'text': '17:00', 'callback': '17:00'}, '18:00': {'text': '18:00', 'callback': '18:00'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Выберите удобную для вас дату и время:''', reply_markup=markup)
#Записаться_end

#Прайс лист
@bot.message_handler(commands=['Прайс лист'])
def Prajslist_message(message):
    button_dict = {'Записаться': {'text': 'Записаться', 'callback': 'Записаться'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''У нас вы можете заказать следующие услуги:
- Маникюр
- Педикюр
- Наращивание ногтей
- Дизайн ногтей''', reply_markup=markup)
#Прайс лист_end

#9:00
@bot.callback_query_handler(func=lambda call: call.data == '9:00')
def _callback(call):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы записаны на услугу в 9:00. Ожидайте подтверждение!''', reply_markup=markup)
#9:00_end

#10:00
@bot.callback_query_handler(func=lambda call: call.data == '10:00')
def _callback(call):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы записаны на услугу в 10:00. Ожидайте подтверждение!''', reply_markup=markup)
#10:00_end

#11:00
@bot.callback_query_handler(func=lambda call: call.data == '11:00')
def _callback(call):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы записаны на услугу в 11:00. Ожидайте подтверждение!''', reply_markup=markup)
#11:00_end

#12:00
@bot.callback_query_handler(func=lambda call: call.data == '12:00')
def _callback(call):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы записаны на услугу в 12:00. Ожидайте подтверждение!''', reply_markup=markup)
#12:00_end

#13:00
@bot.callback_query_handler(func=lambda call: call.data == '13:00')
def _callback(call):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы записаны на услугу в 13:00. Ожидайте подтверждение!''', reply_markup=markup)
#13:00_end

#14:00
@bot.callback_query_handler(func=lambda call: call.data == '14:00')
def _callback(call):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы записаны на услугу в 14:00. Ожидайте подтверждение!''', reply_markup=markup)
#14:00_end

#15:00
@bot.callback_query_handler(func=lambda call: call.data == '15:00')
def _callback(call):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы записаны на услугу в 15:00. Ожидайте подтверждение!''', reply_markup=markup)
#15:00_end

#16:00
@bot.callback_query_handler(func=lambda call: call.data == '16:00')
def _callback(call):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы записаны на услугу в 16:00. Ожидайте подтверждение!''', reply_markup=markup)
#16:00_end

#17:00
@bot.callback_query_handler(func=lambda call: call.data == '17:00')
def _callback(call):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы записаны на услугу в 17:00. Ожидайте подтверждение!''', reply_markup=markup)
#17:00_end

#18:00
@bot.callback_query_handler(func=lambda call: call.data == '18:00')
def _callback(call):
    button_dict = {'Главное меню': {'text': 'Главное меню', 'callback': 'Главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы записаны на услугу в 18:00. Ожидайте подтверждение!''', reply_markup=markup)
#18:00_end

#Главное меню
@bot.callback_query_handler(func=lambda call: call.data == 'Главное меню')
def Glavnoemenju_callback(call):
    button_dict = {'Записаться': {'text': 'Записаться', 'callback': 'Записаться'}, 'Прайс лист': {'text': 'Прайс лист', 'callback': 'Прайс лист'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Выберите нужное действие:''', reply_markup=markup)
#Главное меню_end
bot.polling()