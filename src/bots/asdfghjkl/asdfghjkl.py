import telebot
from telebot import types

bot_token = "asdfghjkl;"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Узнать больше': {'text': 'Узнать больше', 'callback': 'Узнать больше'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Привет! Я бот для инфобизнеса. Чем могу помочь?''', reply_markup=markup)
#start_end

#Узнать больше
@bot.callback_query_handler(func=lambda call: call.data == 'Узнать больше')
def Uznatbolshe_callback(call):
    button_dict = {'Как начать?': {'text': 'Как начать?', 'callback': 'Как начать?'}, 'Как продать?': {'text': 'Как продать?', 'callback': 'Как продать?'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Инфобизнес - это бизнес, основанный на продаже информации. В нем вы можете создать и продавать свои онлайн-курсы, электронные книги, видеоуроки и многое другое. Я могу помочь вам разобраться с основами инфобизнеса и поделиться полезными советами.''', reply_markup=markup)
#Узнать больше_end

#Как начать?
@bot.callback_query_handler(func=lambda call: call.data == 'Как начать?')
def Kaknachat_callback(call):
    button_dict = {'Как продавать?': {'text': 'Как продавать?', 'callback': 'Как продавать?'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Чтобы начать инфобизнес, вам нужно определить свою целевую аудиторию, выбрать тему для своих информационных продуктов и создать качественный контент. Затем вы можете продвигать свои продукты через социальные сети, блоги, партнерские программы и другие каналы. Не забывайте также обратить внимание на правовые и юридические аспекты.''', reply_markup=markup)
#Как начать?_end

#Как продавать?
@bot.callback_query_handler(func=lambda call: call.data == 'Как продавать?')
def Kakprodavat_callback(call):
    button_dict = {'Как начать?': {'text': 'Как начать?', 'callback': 'Как начать?'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Есть несколько способов продавать информационные продукты. Вы можете создать свой собственный сайт или лендинг, где будете предлагать продукты и принимать оплату. Также можно использовать платформы для продажи онлайн-курсов, такие как Udemy или Coursera. Не забывайте также о маркетинговых стратегиях, таких как email-рассылка или рекламные кампании в социальных сетях.''', reply_markup=markup)
#Как продавать?_end

#Контакты
@bot.callback_query_handler(func=lambda call: call.data == 'Контакты')
def Kontakty_callback(call):
    button_dict = {'Узнать больше': {'text': 'Узнать больше', 'callback': 'Узнать больше'}, 'Как начать?': {'text': 'Как начать?', 'callback': 'Как начать?'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Если у вас есть вопросы или вы хотите получить более подробную информацию о инфобизнесе, вы можете связаться со мной по следующим контактам: -email: info@infobusinessbot.com
-телефон: +123456789
-сайт: www.infobusinessbot.com''', reply_markup=markup)
#Контакты_end
bot.polling()