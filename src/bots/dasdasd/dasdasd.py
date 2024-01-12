import telebot
from telebot import types

bot_token = "dasdasda"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Информация о бизнесе': {'text': 'Информация о бизнесе', 'callback': 'Информация о бизнесе'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Приветствуем вас! Выберите одну из доступных команд:''', reply_markup=markup)
#start_end

#info_business
@bot.message_handler(commands=['info_business'])
def infobusiness_message(message):
    button_dict = {'Как начать': {'text': 'Как начать', 'callback': 'Как начать'}, 'Преимущества': {'text': 'Преимущества', 'callback': 'Преимущества'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Информация об инфобизнесе:

Инфобизнес - это бизнес, основанный на знаниях и информации. Он позволяет создавать и продавать информационные продукты, такие как электронные курсы, вебинары, электронные книги и др. Инфобизнес может быть прибыльным и перспективным видом бизнеса, который требует минимальных вложений и позволяет работать из любой точки мира.''', reply_markup=markup)
#info_business_end

#contacts
@bot.message_handler(commands=['contacts'])
def contacts_message(message):
    
    bot.send_message(message.chat.id, '''Контактная информация:

Email: info@business.com
Телефон: +123456789
Адрес: г. Москва, ул. Примерная, д. 1''')
#contacts_end

#Как начать
@bot.callback_query_handler(func=lambda call: call.data == 'Как начать')
def Kaknachat_callback(call):
    
    bot.send_message(call.message.chat.id, '''Для начала инфобизнеса вам потребуется выбрать тему, в которой вы обладаете знаниями и опытом. Затем разработать информационный продукт, который будет интересен вашей целевой аудитории. Не забудьте провести маркетинговые исследования и продвижение вашего продукта для привлечения клиентов.''')
#Как начать_end

#Преимущества
@bot.callback_query_handler(func=lambda call: call.data == 'Преимущества')
def Preimuschestva_callback(call):
    
    bot.send_message(call.message.chat.id, '''Основные преимущества инфобизнеса:
1. Минимальные вложения
2. Возможность работать из любой точки мира
3. Пассивный доход и масштабируемость
4. Большой потенциал роста и развития
5. Возможность делиться своими знаниями и помогать другим''')
#Преимущества_end

#help
@bot.message_handler(commands=['help'])
def help_message(message):
    button_dict = {'/start': {'text': '/start', 'callback': '/start'}, '/offers': {'text': '/offers', 'callback': '/offers'}, '/buy': {'text': '/buy', 'callback': '/buy'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Вот список доступных команд:
 /start - начать работу с ботом
 /offers - посмотреть наши предложения
 /buy - запустить процесс покупки''', reply_markup=markup)
#help_end

#offers
@bot.message_handler(commands=['offers'])
def offers_message(message):
    button_dict = {'1. Булка': {'text': '1. Булка', 'callback': '1. Булка'}, '2. Трюфель': {'text': '2. Трюфель', 'callback': '2. Трюфель'}, '3. Коктейль': {'text': '3. Коктейль', 'callback': '3. Коктейль'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''У нас в продаже есть следующие виды какашек:
 1. Классическая булка
 2. Шоколадный трюфель
 3. Фруктовый коктейль''', reply_markup=markup)
#offers_end

#buy
@bot.message_handler(commands=['buy'])
def buy_message(message):
    button_dict = {'1. Булка': {'text': '1. Булка', 'callback': '1. Булка'}, '2. Трюфель': {'text': '2. Трюфель', 'callback': '2. Трюфель'}, '3. Коктейль': {'text': '3. Коктейль', 'callback': '3. Коктейль'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Выберите вид какашки, который хотите приобрести''', reply_markup=markup)
#buy_end

#1. Булка
@bot.callback_query_handler(func=lambda call: call.data == '1. Булка')
def Bulka_callback(call):
    
    bot.send_message(call.message.chat.id, '''Количество: 1
 Цена: $10.00
 Для оформления заказа, введите свои контактные данные''')
#1. Булка_end

#2. Трюфель
@bot.callback_query_handler(func=lambda call: call.data == '2. Трюфель')
def Trjufel_callback(call):
    
    bot.send_message(call.message.chat.id, '''Количество: 1
 Цена: $15.00
 Для оформления заказа, введите свои контактные данные''')
#2. Трюфель_end

#3. Коктейль
@bot.callback_query_handler(func=lambda call: call.data == '3. Коктейль')
def Koktejl_callback(call):
    
    bot.send_message(call.message.chat.id, '''Количество: 1
 Цена: $20.00
 Для оформления заказа, введите свои контактные данные''')
#3. Коктейль_end
bot.polling()