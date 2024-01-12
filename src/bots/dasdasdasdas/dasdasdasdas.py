import telebot
from telebot import types

bot_token = "dasdadadasdada"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Меню': {'text': 'Меню', 'callback': 'Меню'}, 'Акции': {'text': 'Акции', 'callback': 'Акции'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Привет! Чем я могу помочь тебе в моей кофейне?''', reply_markup=markup)
#start_end

#menu
@bot.message_handler(commands=['menu'])
def menu_message(message):
    button_dict = {'Кофе': {'text': 'Кофе', 'callback': 'Кофе'}, 'Чай': {'text': 'Чай', 'callback': 'Чай'}, 'Соки': {'text': 'Соки', 'callback': 'Соки'}, 'Выпечка': {'text': 'Выпечка', 'callback': 'Выпечка'}, 'Сэндвичи': {'text': 'Сэндвичи', 'callback': 'Сэндвичи'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''У нас в меню есть различные виды кофе, чай, соки, выпечка и сэндвичи. Что желаешь?''', reply_markup=markup)
#menu_end

#actions
@bot.callback_query_handler(func=lambda call: call.data == 'actions')
def actions_callback(call):
    button_dict = {'Скидки': {'text': 'Скидки', 'callback': 'Скидки'}, 'Бонусы': {'text': 'Бонусы', 'callback': 'Бонусы'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас проводятся различные акции, следи за обновлениями! Что тебя интересует?''', reply_markup=markup)
#actions_end

#coffee
@bot.callback_query_handler(func=lambda call: call.data == 'coffee')
def coffee_callback(call):
    button_dict = {'Эспрессо': {'text': 'Эспрессо', 'callback': 'Эспрессо'}, 'Латте': {'text': 'Латте', 'callback': 'Латте'}, 'Капучино': {'text': 'Капучино', 'callback': 'Капучино'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть классический эспрессо, латте, капучино и многое другое. Что выбираешь?''', reply_markup=markup)
#coffee_end

#tea
@bot.callback_query_handler(func=lambda call: call.data == 'tea')
def tea_callback(call):
    button_dict = {'Черный': {'text': 'Черный', 'callback': 'Черный'}, 'Зеленый': {'text': 'Зеленый', 'callback': 'Зеленый'}, 'Фруктовый': {'text': 'Фруктовый', 'callback': 'Фруктовый'}, 'Травяной': {'text': 'Травяной', 'callback': 'Травяной'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть черный, зеленый, фруктовый и травяной чай. Что предпочитаешь?''', reply_markup=markup)
#tea_end

#juices
@bot.callback_query_handler(func=lambda call: call.data == 'juices')
def juices_callback(call):
    button_dict = {'Апельсиновый': {'text': 'Апельсиновый', 'callback': 'Апельсиновый'}, 'Яблочный': {'text': 'Яблочный', 'callback': 'Яблочный'}, 'Грейпфрутовый': {'text': 'Грейпфрутовый', 'callback': 'Грейпфрутовый'}, 'Томатный': {'text': 'Томатный', 'callback': 'Томатный'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть апельсиновый, яблочный, грейпфрутовый и томатный соки. Что ты хочешь попробовать?''', reply_markup=markup)
#juices_end

#pastries
@bot.callback_query_handler(func=lambda call: call.data == 'pastries')
def pastries_callback(call):
    button_dict = {'Пирожные': {'text': 'Пирожные', 'callback': 'Пирожные'}, 'Печенье': {'text': 'Печенье', 'callback': 'Печенье'}, 'Булочки': {'text': 'Булочки', 'callback': 'Булочки'}, 'Пироги': {'text': 'Пироги', 'callback': 'Пироги'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть пирожные, печенье, булочки и пироги. Что выбираешь?''', reply_markup=markup)
#pastries_end

#sandwiches
@bot.callback_query_handler(func=lambda call: call.data == 'sandwiches')
def sandwiches_callback(call):
    button_dict = {'Гамбургеры': {'text': 'Гамбургеры', 'callback': 'Гамбургеры'}, 'Чизбургеры': {'text': 'Чизбургеры', 'callback': 'Чизбургеры'}, 'Куриные сэндвичи': {'text': 'Куриные сэндвичи', 'callback': 'Куриные сэндвичи'}, 'Тунцовые сэндвичи': {'text': 'Тунцовые сэндвичи', 'callback': 'Тунцовые сэндвичи'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть гамбургеры, чизбургеры, сэндвичи с куриной и тунцовой начинкой. Что хочешь попробовать?''', reply_markup=markup)
#sandwiches_end

#Меню
@bot.callback_query_handler(func=lambda call: call.data == 'Меню')
def Menju_callback(call):
    button_dict = {'Эспрессо': {'text': 'Эспрессо', 'callback': 'Эспрессо'}, 'Латте': {'text': 'Латте', 'callback': 'Латте'}, 'Капуччино': {'text': 'Капуччино', 'callback': 'Капуччино'}, 'Американо': {'text': 'Американо', 'callback': 'Американо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть следующие напитки:
- Эспрессо
- Латте
- Капуччино
- Американо
Какой напиток ты хочешь заказать?''', reply_markup=markup)
#Меню_end

#Акции
@bot.callback_query_handler(func=lambda call: call.data == 'Акции')
def Aktsii_callback(call):
    button_dict = {'Заказать': {'text': 'Заказать', 'callback': 'Заказать'}, 'Вернуться в главное меню': {'text': 'Вернуться в главное меню', 'callback': 'Вернуться в главное меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас сейчас действуют следующие акции:
- Скидка 10% на все кофе
- Бесплатный десерт при заказе двух напитков
Не упусти свой шанс!''', reply_markup=markup)
#Акции_end

#Эспрессо
@bot.callback_query_handler(func=lambda call: call.data == 'Эспрессо')
def Espresso_callback(call):
    button_dict = {'1 порция': {'text': '1 порция', 'callback': '1 порция'}, '2 порции': {'text': '2 порции', 'callback': '2 порции'}, '3 порции': {'text': '3 порции', 'callback': '3 порции'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Отличный выбор! Сколько порций эспрессо ты хочешь заказать?''', reply_markup=markup)
#Эспрессо_end

#Латте
@bot.callback_query_handler(func=lambda call: call.data == 'Латте')
def Latte_callback(call):
    button_dict = {'1 порция': {'text': '1 порция', 'callback': '1 порция'}, '2 порции': {'text': '2 порции', 'callback': '2 порции'}, '3 порции': {'text': '3 порции', 'callback': '3 порции'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Прекрасный выбор! Сколько порций латте ты хочешь заказать?''', reply_markup=markup)
#Латте_end

#Капуччино
@bot.callback_query_handler(func=lambda call: call.data == 'Капуччино')
def Kapuchchino_callback(call):
    button_dict = {'1 порция': {'text': '1 порция', 'callback': '1 порция'}, '2 порции': {'text': '2 порции', 'callback': '2 порции'}, '3 порции': {'text': '3 порции', 'callback': '3 порции'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Отличный выбор! Сколько порций капуччино ты хочешь заказать?''', reply_markup=markup)
#Капуччино_end

#Американо
@bot.callback_query_handler(func=lambda call: call.data == 'Американо')
def Amerikano_callback(call):
    button_dict = {'1 порция': {'text': '1 порция', 'callback': '1 порция'}, '2 порции': {'text': '2 порции', 'callback': '2 порции'}, '3 порции': {'text': '3 порции', 'callback': '3 порции'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Отличный выбор! Сколько порций американо ты хочешь заказать?''', reply_markup=markup)
#Американо_end

#Заказ
@bot.callback_query_handler(func=lambda call: call.data == 'Заказ')
def Zakaz_callback(call):
    button_dict = {'Изменить адрес': {'text': 'Изменить адрес', 'callback': 'Изменить адрес'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Спасибо за заказ! Мы приготовим его как можно скорее.
Адрес доставки:''', reply_markup=markup)
#Заказ_end

#Изменить адрес
@bot.callback_query_handler(func=lambda call: call.data == 'Изменить адрес')
def Izmenitadres_callback(call):
    button_dict = {'Подтвердить': {'text': 'Подтвердить', 'callback': 'Подтвердить'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Введите новый адрес доставки:''', reply_markup=markup)
#Изменить адрес_end
bot.polling()