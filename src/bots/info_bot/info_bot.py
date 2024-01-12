import telebot
from telebot import types

bot_token = "6434108320:AAHcb8OpYIPpTKEpCFcpkD0zgl32HmLGMcM"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Женские кроссовки': {'text': 'Женские кроссовки', 'callback': 'Женские кроссовки'}, 'Мужские кроссовки': {'text': 'Мужские кроссовки', 'callback': 'Мужские кроссовки'}, 'Детские кроссовки': {'text': 'Детские кроссовки', 'callback': 'Детские кроссовки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Привет! Я бот-помощник в выборе кроссовок. Что тебя интересует?''', reply_markup=markup)
#start_end

#Женские кроссовки
@bot.callback_query_handler(func=lambda call: call.data == 'Женские кроссовки')
def Zhenskiekrossovki_callback(call):
    button_dict = {'Беговые кроссовки': {'text': 'Беговые кроссовки', 'callback': 'Беговые кроссовки'}, 'Спортивные кроссовки': {'text': 'Спортивные кроссовки', 'callback': 'Спортивные кроссовки'}, 'Повседневные кроссовки': {'text': 'Повседневные кроссовки', 'callback': 'Повседневные кроссовки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть большой выбор женских кроссовок. Что тебе интересно?''', reply_markup=markup)
#Женские кроссовки_end

#Мужские кроссовки
@bot.callback_query_handler(func=lambda call: call.data == 'Мужские кроссовки')
def Muzhskiekrossovki_callback(call):
    button_dict = {'Беговые кроссовки': {'text': 'Беговые кроссовки', 'callback': 'Беговые кроссовки'}, 'Спортивные кроссовки': {'text': 'Спортивные кроссовки', 'callback': 'Спортивные кроссовки'}, 'Повседневные кроссовки': {'text': 'Повседневные кроссовки', 'callback': 'Повседневные кроссовки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть большой выбор мужских кроссовок. Что тебе интересно?''', reply_markup=markup)
#Мужские кроссовки_end

#Детские кроссовки
@bot.callback_query_handler(func=lambda call: call.data == 'Детские кроссовки')
def Detskiekrossovki_callback(call):
    button_dict = {'Беговые кроссовки': {'text': 'Беговые кроссовки', 'callback': 'Беговые кроссовки'}, 'Спортивные кроссовки': {'text': 'Спортивные кроссовки', 'callback': 'Спортивные кроссовки'}, 'Повседневные кроссовки': {'text': 'Повседневные кроссовки', 'callback': 'Повседневные кроссовки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть большой выбор детских кроссовок. Что тебе интересно?''', reply_markup=markup)
#Детские кроссовки_end

#Беговые кроссовки
@bot.callback_query_handler(func=lambda call: call.data == 'Беговые кроссовки')
def Begovyekrossovki_callback(call):
    button_dict = {'Маленький': {'text': 'Маленький', 'callback': 'Маленький'}, 'Средний': {'text': 'Средний', 'callback': 'Средний'}, 'Большой': {'text': 'Большой', 'callback': 'Большой'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Мы предлагаем широкий ассортимент беговых кроссовок. Какой размер тебя интересует?''', reply_markup=markup)
#Беговые кроссовки_end

#Спортивные кроссовки
@bot.callback_query_handler(func=lambda call: call.data == 'Спортивные кроссовки')
def Sportivnyekrossovki_callback(call):
    button_dict = {'Маленький': {'text': 'Маленький', 'callback': 'Маленький'}, 'Средний': {'text': 'Средний', 'callback': 'Средний'}, 'Большой': {'text': 'Большой', 'callback': 'Большой'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Мы предлагаем широкий ассортимент спортивных кроссовок. Какой размер тебя интересует?''', reply_markup=markup)
#Спортивные кроссовки_end

#Повседневные кроссовки
@bot.callback_query_handler(func=lambda call: call.data == 'Повседневные кроссовки')
def Povsednevnyekrossovki_callback(call):
    button_dict = {'Маленький': {'text': 'Маленький', 'callback': 'Маленький'}, 'Средний': {'text': 'Средний', 'callback': 'Средний'}, 'Большой': {'text': 'Большой', 'callback': 'Большой'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Мы предлагаем широкий ассортимент повседневных кроссовок. Какой размер тебя интересует?''', reply_markup=markup)
#Повседневные кроссовки_end

#Маленький
@bot.callback_query_handler(func=lambda call: call.data == 'Маленький')
def Malenkij_callback(call):
    button_dict = {'Бренд A': {'text': 'Бренд A', 'callback': 'Бренд A'}, 'Бренд B': {'text': 'Бренд B', 'callback': 'Бренд B'}, 'Бренд C': {'text': 'Бренд C', 'callback': 'Бренд C'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть кроссовки в маленьком размере. Что тебе интересно?''', reply_markup=markup)
#Маленький_end

#Средний
@bot.callback_query_handler(func=lambda call: call.data == 'Средний')
def Srednij_callback(call):
    button_dict = {'Бренд A': {'text': 'Бренд A', 'callback': 'Бренд A'}, 'Бренд B': {'text': 'Бренд B', 'callback': 'Бренд B'}, 'Бренд C': {'text': 'Бренд C', 'callback': 'Бренд C'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть кроссовки в среднем размере. Что тебе интересно?''', reply_markup=markup)
#Средний_end

#Большой
@bot.callback_query_handler(func=lambda call: call.data == 'Большой')
def Bolshoj_callback(call):
    button_dict = {'Бренд A': {'text': 'Бренд A', 'callback': 'Бренд A'}, 'Бренд B': {'text': 'Бренд B', 'callback': 'Бренд B'}, 'Бренд C': {'text': 'Бренд C', 'callback': 'Бренд C'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть кроссовки в большом размере. Что тебе интересно?''', reply_markup=markup)
#Большой_end

#Бренд A
@bot.callback_query_handler(func=lambda call: call.data == 'Бренд A')
def BrendA_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Выбрать другой бренд': {'text': 'Выбрать другой бренд', 'callback': 'Выбрать другой бренд'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Бренд A - это отличный выбор. Эти кроссовки отлично подходят для спорта. Цена: $100.''', reply_markup=markup)
#Бренд A_end

#Бренд B
@bot.callback_query_handler(func=lambda call: call.data == 'Бренд B')
def BrendB_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Выбрать другой бренд': {'text': 'Выбрать другой бренд', 'callback': 'Выбрать другой бренд'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Бренд B - это популярные кроссовки в уличном стиле. Цена: $80.''', reply_markup=markup)
#Бренд B_end

#Бренд C
@bot.callback_query_handler(func=lambda call: call.data == 'Бренд C')
def BrendC_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Выбрать другой бренд': {'text': 'Выбрать другой бренд', 'callback': 'Выбрать другой бренд'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Бренд C - это комфортные повседневные кроссовки. Цена: $90.''', reply_markup=markup)
#Бренд C_end

#Добавить в корзину
@bot.callback_query_handler(func=lambda call: call.data == 'Добавить в корзину')
def Dobavitvkorzinu_callback(call):
    button_dict = {'Оформить заказ': {'text': 'Оформить заказ', 'callback': 'Оформить заказ'}, 'Продолжить покупки': {'text': 'Продолжить покупки', 'callback': 'Продолжить покупки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Товар добавлен в корзину. Что дальше?''', reply_markup=markup)
#Добавить в корзину_end

#Выбрать другой бренд
@bot.callback_query_handler(func=lambda call: call.data == 'Выбрать другой бренд')
def Vybratdrugojbrend_callback(call):
    button_dict = {'Бренд A': {'text': 'Бренд A', 'callback': 'Бренд A'}, 'Бренд B': {'text': 'Бренд B', 'callback': 'Бренд B'}, 'Бренд C': {'text': 'Бренд C', 'callback': 'Бренд C'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Выбери другой бренд кроссовок.''', reply_markup=markup)
#Выбрать другой бренд_end

#Оформить заказ
@bot.callback_query_handler(func=lambda call: call.data == 'Оформить заказ')
def Oformitzakaz_callback(call):
    button_dict = {'Отменить заказ': {'text': 'Отменить заказ', 'callback': 'Отменить заказ'}, 'Помощь': {'text': 'Помощь', 'callback': 'Помощь'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Ок. Ваш заказ принят. Оплатите его по ссылке.''', reply_markup=markup)
#Оформить заказ_end

#Продолжить покупки
@bot.callback_query_handler(func=lambda call: call.data == 'Продолжить покупки')
def Prodolzhitpokupki_callback(call):
    button_dict = {'Женские кроссовки': {'text': 'Женские кроссовки', 'callback': 'Женские кроссовки'}, 'Мужские кроссовки': {'text': 'Мужские кроссовки', 'callback': 'Мужские кроссовки'}, 'Детские кроссовки': {'text': 'Детские кроссовки', 'callback': 'Детские кроссовки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Продолжайте выбирать кроссовки. Что вас интересует?''', reply_markup=markup)
#Продолжить покупки_end

#Отменить заказ
@bot.callback_query_handler(func=lambda call: call.data == 'Отменить заказ')
def Otmenitzakaz_callback(call):
    button_dict = {'Помощь': {'text': 'Помощь', 'callback': 'Помощь'}, 'Продолжить покупки': {'text': 'Продолжить покупки', 'callback': 'Продолжить покупки'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Ваш заказ отменен. Если у вас возникли вопросы, обратитесь к нашей службе поддержки.''', reply_markup=markup)
#Отменить заказ_end

#Помощь
@bot.callback_query_handler(func=lambda call: call.data == 'Помощь')
def Pomosch_callback(call):
    button_dict = {'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}, 'Вопросы и ответы': {'text': 'Вопросы и ответы', 'callback': 'Вопросы и ответы'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Нужна помощь? Обратитесь к нашей службе поддержки.''', reply_markup=markup)
#Помощь_end

#Контакты
@bot.callback_query_handler(func=lambda call: call.data == 'Контакты')
def Kontakty_callback(call):
    button_dict = {'Помощь': {'text': 'Помощь', 'callback': 'Помощь'}, 'Вопросы и ответы': {'text': 'Вопросы и ответы', 'callback': 'Вопросы и ответы'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Свяжитесь с нами по телефону +1234567890 или напишите нам на почту info@example.com.''', reply_markup=markup)
#Контакты_end

#Вопросы и ответы
@bot.callback_query_handler(func=lambda call: call.data == 'Вопросы и ответы')
def Voprosyiotvety_callback(call):
    button_dict = {'Помощь': {'text': 'Помощь', 'callback': 'Помощь'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Если у вас есть вопросы, ознакомьтесь с нашей страницей вопросов и ответов на сайте.''', reply_markup=markup)
#Вопросы и ответы_end
bot.polling()