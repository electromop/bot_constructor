import telebot
from telebot import types

bot_token = "dasdasd"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Каталог товаров': {'text': 'Каталог товаров', 'callback': 'Каталог товаров'}, 'О нас': {'text': 'О нас', 'callback': 'О нас'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Добро пожаловать в магазин вейпов! Чтобы узнать наш ассортимент, нажмите на кнопку 'Каталог товаров'''', reply_markup=markup)
#start_end

#Каталог товаров
@bot.callback_query_handler(func=lambda call: call.data == 'Каталог товаров')
def Katalogtovarov_callback(call):
    button_dict = {'Стартовые наборы': {'text': 'Стартовые наборы', 'callback': 'Стартовые наборы'}, 'Механические моды': {'text': 'Механические моды', 'callback': 'Механические моды'}, 'Боксмоды': {'text': 'Боксмоды', 'callback': 'Боксмоды'}, 'Аккумуляторы': {'text': 'Аккумуляторы', 'callback': 'Аккумуляторы'}, 'Атомайзеры': {'text': 'Атомайзеры', 'callback': 'Атомайзеры'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас вы найдете разнообразные модели вейпов. Выберите интересующую вас категорию:''', reply_markup=markup)
#Каталог товаров_end

#О нас
@bot.callback_query_handler(func=lambda call: call.data == 'О нас')
def Onas_callback(call):
    button_dict = {'Каталог товаров': {'text': 'Каталог товаров', 'callback': 'Каталог товаров'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Мы - магазин вейпов с многолетним опытом. У нас вы найдете только качественные товары от лучших производителей.''', reply_markup=markup)
#О нас_end

#Стартовые наборы
@bot.callback_query_handler(func=lambda call: call.data == 'Стартовые наборы')
def Startovyenabory_callback(call):
    button_dict = {'Набор AIO': {'text': 'Набор AIO', 'callback': 'Набор AIO'}, 'Набор POD': {'text': 'Набор POD', 'callback': 'Набор POD'}, 'Набор Pen': {'text': 'Набор Pen', 'callback': 'Набор Pen'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''В нашем ассортименте есть различные стартовые наборы для новичков. Выберите модель, которая вам нравится:''', reply_markup=markup)
#Стартовые наборы_end

#Механические моды
@bot.callback_query_handler(func=lambda call: call.data == 'Механические моды')
def Mehanicheskiemody_callback(call):
    button_dict = {'Мод AV': {'text': 'Мод AV', 'callback': 'Мод AV'}, 'Мод VG': {'text': 'Мод VG', 'callback': 'Мод VG'}, 'Мод RS': {'text': 'Мод RS', 'callback': 'Мод RS'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Мы предлагаем разнообразные механические моды от известных производителей. Выберите модель, которая вам интересна:''', reply_markup=markup)
#Механические моды_end

#Боксмоды
@bot.callback_query_handler(func=lambda call: call.data == 'Боксмоды')
def Boksmody_callback(call):
    button_dict = {'Мод RX': {'text': 'Мод RX', 'callback': 'Мод RX'}, 'Мод DNA': {'text': 'Мод DNA', 'callback': 'Мод DNA'}, 'Мод SX': {'text': 'Мод SX', 'callback': 'Мод SX'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть большой выбор качественных боксмодов. Выберите модель, которая вам нравится:''', reply_markup=markup)
#Боксмоды_end

#Аккумуляторы
@bot.callback_query_handler(func=lambda call: call.data == 'Аккумуляторы')
def Akkumuljatory_callback(call):
    button_dict = {'Аккумулятор 18650': {'text': 'Аккумулятор 18650', 'callback': 'Аккумулятор 18650'}, 'Аккумулятор 20700': {'text': 'Аккумулятор 20700', 'callback': 'Аккумулятор 20700'}, 'Аккумулятор 21700': {'text': 'Аккумулятор 21700', 'callback': 'Аккумулятор 21700'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''В нашем магазине вы найдете аккумуляторы разных типов и емкостей. Выберите нужный вам вариант:''', reply_markup=markup)
#Аккумуляторы_end

#Атомайзеры
@bot.callback_query_handler(func=lambda call: call.data == 'Атомайзеры')
def Atomajzery_callback(call):
    button_dict = {'Атомайзер RDA': {'text': 'Атомайзер RDA', 'callback': 'Атомайзер RDA'}, 'Атомайзер RTA': {'text': 'Атомайзер RTA', 'callback': 'Атомайзер RTA'}, 'Атомайзер RDTA': {'text': 'Атомайзер RDTA', 'callback': 'Атомайзер RDTA'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть широкий выбор атомайзеров различного типа. Выберите интересующую вас модель:''', reply_markup=markup)
#Атомайзеры_end

#Контакты
@bot.callback_query_handler(func=lambda call: call.data == 'Контакты')
def Kontakty_callback(call):
    button_dict = {'Каталог товаров': {'text': 'Каталог товаров', 'callback': 'Каталог товаров'}, 'О нас': {'text': 'О нас', 'callback': 'О нас'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Если у вас возникли вопросы или вы хотите сделать заказ, свяжитесь с нами по следующим контактам:
Телефон: +123456789
Email: info@vapestore.com''', reply_markup=markup)
#Контакты_end
bot.polling()