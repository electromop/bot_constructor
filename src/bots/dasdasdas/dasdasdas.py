import telebot
from telebot import types

bot_token = "dasdasdassdasd"
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
    bot.send_message(message.chat.id, '''Добро пожаловать в нашу кофейню! Чем могу помочь?''', reply_markup=markup)
#start_end

#Меню
@bot.callback_query_handler(func=lambda call: call.data == 'Меню')
def Menju_callback(call):
    button_dict = {'Кофе': {'text': 'Кофе', 'callback': 'Кофе'}, 'Чай': {'text': 'Чай', 'callback': 'Чай'}, 'Десерты': {'text': 'Десерты', 'callback': 'Десерты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас в меню есть разные виды кофе и другие напитки. Что вы хотите заказать?''', reply_markup=markup)
#Меню_end

#Акции
@bot.callback_query_handler(func=lambda call: call.data == 'Акции')
def Aktsii_callback(call):
    button_dict = {'Подробнее': {'text': 'Подробнее', 'callback': 'Подробнее'}, 'Заказать': {'text': 'Заказать', 'callback': 'Заказать'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас всегда есть специальные предложения и скидки. Закажите что-нибудь и получите приятный бонус!''', reply_markup=markup)
#Акции_end

#Кофе
@bot.callback_query_handler(func=lambda call: call.data == 'Кофе')
def Kofe_callback(call):
    button_dict = {'Эспрессо': {'text': 'Эспрессо', 'callback': 'Эспрессо'}, 'Капучино': {'text': 'Капучино', 'callback': 'Капучино'}, 'Латте': {'text': 'Латте', 'callback': 'Латте'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть эспрессо, капучино, латте и другие виды кофе. Что вам понравится?''', reply_markup=markup)
#Кофе_end

#Чай
@bot.callback_query_handler(func=lambda call: call.data == 'Чай')
def Chaj_callback(call):
    button_dict = {'Черный чай': {'text': 'Черный чай', 'callback': 'Черный чай'}, 'Зеленый чай': {'text': 'Зеленый чай', 'callback': 'Зеленый чай'}, 'Фруктовый чай': {'text': 'Фруктовый чай', 'callback': 'Фруктовый чай'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть черный чай, зеленый чай, фруктовый чай и другие виды. Что вам понравится?''', reply_markup=markup)
#Чай_end

#Десерты
@bot.callback_query_handler(func=lambda call: call.data == 'Десерты')
def Deserty_callback(call):
    button_dict = {'Торт': {'text': 'Торт', 'callback': 'Торт'}, 'Пирожное': {'text': 'Пирожное', 'callback': 'Пирожное'}, 'Маффин': {'text': 'Маффин', 'callback': 'Маффин'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''У нас есть торты, пирожные, маффины и другие сладости. Что вам понравится?''', reply_markup=markup)
#Десерты_end

#Подробнее
@bot.callback_query_handler(func=lambda call: call.data == 'Подробнее')
def Podrobnee_callback(call):
    button_dict = {'На сайт': {'text': 'На сайт', 'callback': 'На сайт'}, 'В магазин': {'text': 'В магазин', 'callback': 'В магазин'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Подробности акции будут доступны на нашем сайте или в магазине. Приходите и узнайте больше!''', reply_markup=markup)
#Подробнее_end

#Заказать
@bot.callback_query_handler(func=lambda call: call.data == 'Заказать')
def Zakazat_callback(call):
    button_dict = {'Позвонить': {'text': 'Позвонить', 'callback': 'Позвонить'}, 'Адрес': {'text': 'Адрес', 'callback': 'Адрес'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Для заказа свяжитесь с нами по телефону или приходите в магазин. Мы всегда рады вашему визиту!''', reply_markup=markup)
#Заказать_end

#Эспрессо
@bot.callback_query_handler(func=lambda call: call.data == 'Эспрессо')
def Espresso_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Предлагаем вам попробовать наш классический эспрессо. Вы точно не пожалеете!''', reply_markup=markup)
#Эспрессо_end

#Капучино
@bot.callback_query_handler(func=lambda call: call.data == 'Капучино')
def Kapuchino_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Предлагаем вам попробовать наш ароматный капучино. Вы точно не пожалеете!''', reply_markup=markup)
#Капучино_end

#Латте
@bot.callback_query_handler(func=lambda call: call.data == 'Латте')
def Latte_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Предлагаем вам попробовать наше нежное латте. Вы точно не пожалеете!''', reply_markup=markup)
#Латте_end

#Черный чай
@bot.callback_query_handler(func=lambda call: call.data == 'Черный чай')
def Chernyjchaj_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Предлагаем вам попробовать наши классические черный чай. Вы точно не пожалеете!''', reply_markup=markup)
#Черный чай_end

#Зеленый чай
@bot.callback_query_handler(func=lambda call: call.data == 'Зеленый чай')
def Zelenyjchaj_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Предлагаем вам попробовать наш свежий зеленый чай. Вы точно не пожалеете!''', reply_markup=markup)
#Зеленый чай_end

#Фруктовый чай
@bot.callback_query_handler(func=lambda call: call.data == 'Фруктовый чай')
def Fruktovyjchaj_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Предлагаем вам попробовать наш ароматный фруктовый чай. Вы точно не пожалеете!''', reply_markup=markup)
#Фруктовый чай_end

#Торт
@bot.callback_query_handler(func=lambda call: call.data == 'Торт')
def Tort_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Предлагаем вам попробовать наши нежные торты. Вы точно не пожалеете!''', reply_markup=markup)
#Торт_end

#Пирожное
@bot.callback_query_handler(func=lambda call: call.data == 'Пирожное')
def Pirozhnoe_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Предлагаем вам попробовать наши вкусные пирожные. Вы точно не пожалеете!''', reply_markup=markup)
#Пирожное_end

#Маффин
@bot.callback_query_handler(func=lambda call: call.data == 'Маффин')
def Maffin_callback(call):
    button_dict = {'Добавить в корзину': {'text': 'Добавить в корзину', 'callback': 'Добавить в корзину'}, 'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Предлагаем вам попробовать наши аппетитные маффины. Вы точно не пожалеете!''', reply_markup=markup)
#Маффин_end

#На сайт
@bot.callback_query_handler(func=lambda call: call.data == 'На сайт')
def Nasajt_callback(call):
    button_dict = {'Перейти на сайт': {'text': 'Перейти на сайт', 'callback': 'Перейти на сайт'}, 'Акции': {'text': 'Акции', 'callback': 'Акции'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы можете найти все подробности и условия акции на нашем официальном сайте. Заходите и узнайте больше!''', reply_markup=markup)
#На сайт_end

#В магазин
@bot.callback_query_handler(func=lambda call: call.data == 'В магазин')
def Vmagazin_callback(call):
    button_dict = {'Адрес': {'text': 'Адрес', 'callback': 'Адрес'}, 'Акции': {'text': 'Акции', 'callback': 'Акции'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Загляните к нам в магазин и мы расскажем вам все детали акции. Ждем вас!''', reply_markup=markup)
#В магазин_end

#Позвонить
@bot.callback_query_handler(func=lambda call: call.data == 'Позвонить')
def Pozvonit_callback(call):
    button_dict = {'Меню': {'text': 'Меню', 'callback': 'Меню'}, 'Акции': {'text': 'Акции', 'callback': 'Акции'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Для заказа или получения дополнительной информации звоните по номеру: +123456789''', reply_markup=markup)
#Позвонить_end

#Адрес
@bot.callback_query_handler(func=lambda call: call.data == 'Адрес')
def Adres_callback(call):
    button_dict = {'Меню': {'text': 'Меню', 'callback': 'Меню'}, 'Акции': {'text': 'Акции', 'callback': 'Акции'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Наш адрес: ул. Примерная, 1. Ждем вас приятного вкуса!''', reply_markup=markup)
#Адрес_end

#Добавить в корзину
@bot.callback_query_handler(func=lambda call: call.data == 'Добавить в корзину')
def Dobavitvkorzinu_callback(call):
    button_dict = {'Корзина': {'text': 'Корзина', 'callback': 'Корзина'}, 'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Продукт успешно добавлен в вашу корзину.''', reply_markup=markup)
#Добавить в корзину_end

#Перейти на сайт
@bot.callback_query_handler(func=lambda call: call.data == 'Перейти на сайт')
def Perejtinasajt_callback(call):
    button_dict = {'Акции': {'text': 'Акции', 'callback': 'Акции'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вы будете перенаправлены на наш сайт. Подробности акции доступны там.''', reply_markup=markup)
#Перейти на сайт_end

#Корзина
@bot.callback_query_handler(func=lambda call: call.data == 'Корзина')
def Korzina_callback(call):
    button_dict = {'Оформить заказ': {'text': 'Оформить заказ', 'callback': 'Оформить заказ'}, 'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Ваша корзина пуста. Добавьте продукты и оформите заказ.''', reply_markup=markup)
#Корзина_end

#Оформить заказ
@bot.callback_query_handler(func=lambda call: call.data == 'Оформить заказ')
def Oformitzakaz_callback(call):
    button_dict = {'Меню': {'text': 'Меню', 'callback': 'Меню'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Ваш заказ принят. Ожидайте подтверждения и доставку.''', reply_markup=markup)
#Оформить заказ_end
bot.polling()