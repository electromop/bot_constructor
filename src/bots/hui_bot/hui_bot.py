import telebot
from telebot import types

bot_token = "6434108320:AAHcb8OpYIPpTKEpCFcpkD0zgl32HmLGMcM"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Подробнее': {'text': 'Подробнее', 'callback': 'Подробнее'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Привет! Я бот для инфобизнеса. Чем могу помочь?''', reply_markup=markup)
#start_end

#Подробнее
@bot.message_handler(commands=['Подробнее'])
def Podrobnee_message(message):
    button_dict = {'Как создать продукт': {'text': 'Как создать продукт', 'callback': 'Как создать продукт'}, 'Как продвигать': {'text': 'Как продвигать', 'callback': 'Как продвигать'}, 'Автоматизация': {'text': 'Автоматизация', 'callback': 'Автоматизация'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Инфобизнес - это бизнес, основанный на продаже информации. Я могу помочь вам с созданием и продвижением своего информационного продукта, а также с автоматизацией процессов в бизнесе.''', reply_markup=markup)
#Подробнее_end

#Контакты
@bot.message_handler(commands=['Контакты'])
def Kontakty_message(message):
    button_dict = {'Телефон': {'text': 'Телефон', 'callback': 'Телефон'}, 'Email': {'text': 'Email', 'callback': 'Email'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Вы можете связаться со мной по следующим контактам:''', reply_markup=markup)
#Контакты_end

#Телефон
@bot.callback_query_handler(func=lambda call: call.data == 'Телефон')
def Telefon_callback(call):
    
    bot.send_message(call.message.chat.id, '''+7 (XXX) XXX-XX-XX''')
#Телефон_end

#Email
@bot.callback_query_handler(func=lambda call: call.data == 'Email')
def Email_callback(call):
    
    bot.send_message(call.message.chat.id, '''info@infobizbot.com''')
#Email_end

#Как создать продукт
@bot.callback_query_handler(func=lambda call: call.data == 'Как создать продукт')
def Kaksozdatprodukt_callback(call):
    button_dict = {'Целевая аудитория': {'text': 'Целевая аудитория', 'callback': 'Целевая аудитория'}, 'Содержание и упаковка': {'text': 'Содержание и упаковка', 'callback': 'Содержание и упаковка'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Для создания информационного продукта вам нужно определить целевую аудиторию, разработать содержание и упаковку продукта, а также провести тестирование и запустить его на рынке.''', reply_markup=markup)
#Как создать продукт_end

#Целевая аудитория
@bot.callback_query_handler(func=lambda call: call.data == 'Целевая аудитория')
def Tselevajaauditorija_callback(call):
    
    bot.send_message(call.message.chat.id, '''Целевая аудитория - это группа людей, которая будет заинтересована и готова платить за вашу информацию. Изучите свою целевую аудиторию, чтобы понять их потребности и предпочтения.''')
#Целевая аудитория_end

#Содержание и упаковка
@bot.callback_query_handler(func=lambda call: call.data == 'Содержание и упаковка')
def Soderzhanieiupakovka_callback(call):
    
    bot.send_message(call.message.chat.id, '''Содержание и упаковка продукта - это то, что вы предлагаете вашей целевой аудитории. Разработайте полезный и уникальный контент, а также привлекательный дизайн и удобную форму предоставления информации.''')
#Содержание и упаковка_end

#Как продвигать
@bot.callback_query_handler(func=lambda call: call.data == 'Как продвигать')
def Kakprodvigat_callback(call):
    
    bot.send_message(call.message.chat.id, '''Для продвижения информационного продукта вы можете использовать различные методы: создание лендинга, использование социальных сетей, контекстная реклама и другие. Определите вашу стратегию продвижения и начните привлекать внимание к вашему продукту.''')
#Как продвигать_end

#Автоматизация
@bot.callback_query_handler(func=lambda call: call.data == 'Автоматизация')
def Avtomatizatsija_callback(call):
    
    bot.send_message(call.message.chat.id, '''Автоматизация процессов в бизнесе поможет вам сэкономить время и ресурсы. Вы можете использовать различные инструменты и программы для автоматизации продаж, маркетинга, управления клиентами и других бизнес-процессов.''')
#Автоматизация_end

#catalog
@bot.message_handler(commands=['catalog'])
def catalog_message(message):
    button_dict = {'Продукт 1': {'text': 'Продукт 1', 'callback': 'Продукт 1'}, 'Продукт 2': {'text': 'Продукт 2', 'callback': 'Продукт 2'}, 'Продукт 3': {'text': 'Продукт 3', 'callback': 'Продукт 3'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, '''Вот каталог наших продуктов:''', reply_markup=markup)
#catalog_end

#question
@bot.message_handler(commands=['question'])
def question_message(message):
    
    bot.send_message(message.chat.id, '''Оставьте свой вопрос и наш менеджер свяжется с вами в ближайшее время.''')
#question_end

#Продукт 1
@bot.callback_query_handler(func=lambda call: call.data == 'Продукт 1')
def Produkt_callback(call):
    button_dict = {'Узнать больше': {'text': 'Узнать больше', 'callback': 'Узнать больше'}, 'Купить': {'text': 'Купить', 'callback': 'Купить'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Продукт 1 - это...''', reply_markup=markup)
#Продукт 1_end

#Продукт 2
@bot.callback_query_handler(func=lambda call: call.data == 'Продукт 2')
def Produkt_callback(call):
    button_dict = {'Узнать больше': {'text': 'Узнать больше', 'callback': 'Узнать больше'}, 'Купить': {'text': 'Купить', 'callback': 'Купить'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Продукт 2 - это...''', reply_markup=markup)
#Продукт 2_end

#Продукт 3
@bot.callback_query_handler(func=lambda call: call.data == 'Продукт 3')
def Produkt_callback(call):
    button_dict = {'Узнать больше': {'text': 'Узнать больше', 'callback': 'Узнать больше'}, 'Купить': {'text': 'Купить', 'callback': 'Купить'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Продукт 3 - это...''', reply_markup=markup)
#Продукт 3_end

#Узнать больше
@bot.callback_query_handler(func=lambda call: call.data == 'Узнать больше')
def Uznatbolshe_callback(call):
    button_dict = {'Оставить заявку': {'text': 'Оставить заявку', 'callback': 'Оставить заявку'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Если вам интересно узнать больше о данном продукте, оставьте заявку и наш менеджер свяжется с вами.''', reply_markup=markup)
#Узнать больше_end

#Купить
@bot.callback_query_handler(func=lambda call: call.data == 'Купить')
def Kupit_callback(call):
    button_dict = {'Оставить заявку': {'text': 'Оставить заявку', 'callback': 'Оставить заявку'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Для покупки продукта оставьте заявку и наш менеджер свяжется с вами.''', reply_markup=markup)
#Купить_end

#Оставить заявку
@bot.callback_query_handler(func=lambda call: call.data == 'Оставить заявку')
def Ostavitzajavku_callback(call):
    
    bot.send_message(call.message.chat.id, '''Оставьте свои контактные данные и наш менеджер свяжется с вами.''')
#Оставить заявку_end

#Описание продукта
@bot.callback_query_handler(func=lambda call: call.data == 'Описание продукта')
def Opisanieprodukta_callback(call):
    button_dict = {'Да': {'text': 'Да', 'callback': 'Да'}, 'Нет, спасибо': {'text': 'Нет, спасибо', 'callback': 'Нет, спасибо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Наш продукт - это инновационное решение, которое поможет вам увеличить продажи и привлечь больше клиентов. Мы предлагаем полный пакет услуг, включающий в себя разработку, маркетинг и поддержку. Хотите узнать больше?''', reply_markup=markup)
#Описание продукта_end

#Да
@bot.callback_query_handler(func=lambda call: call.data == 'Да')
def Da_callback(call):
    button_dict = {'Оставить контакты': {'text': 'Оставить контакты', 'callback': 'Оставить контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Отлично! Мы предлагаем индивидуальный подход к каждому клиенту. Оставьте свои контактные данные и мы свяжемся с вами для дальнейшей консультации.''', reply_markup=markup)
#Да_end

#Нет, спасибо
@bot.callback_query_handler(func=lambda call: call.data == 'Нет, спасибо')
def Netspasibo_callback(call):
    button_dict = {'Описание продукта': {'text': 'Описание продукта', 'callback': 'Описание продукта'}, 'Контакты': {'text': 'Контакты', 'callback': 'Контакты'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Хорошего дня! Если у вас возникнут вопросы, не стесняйтесь обращаться.''', reply_markup=markup)
#Нет, спасибо_end

#Другая информация
@bot.callback_query_handler(func=lambda call: call.data == 'Другая информация')
def Drugajainformatsija_callback(call):
    button_dict = {'FAQ': {'text': 'FAQ', 'callback': 'FAQ'}, 'Условия сотрудничества': {'text': 'Условия сотрудничества', 'callback': 'Условия сотрудничества'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Какую информацию вы хотите получить?''', reply_markup=markup)
#Другая информация_end

#Оставить контакты
@bot.callback_query_handler(func=lambda call: call.data == 'Оставить контакты')
def Ostavitkontakty_callback(call):
    
    bot.send_message(call.message.chat.id, '''Спасибо за вашу заявку! Мы скоро свяжемся с вами для обсуждения деталей. Удачного дня!''')
#Оставить контакты_end

#FAQ
@bot.callback_query_handler(func=lambda call: call.data == 'FAQ')
def FAQ_callback(call):
    button_dict = {'Описание продукта': {'text': 'Описание продукта', 'callback': 'Описание продукта'}, 'Другая информация': {'text': 'Другая информация', 'callback': 'Другая информация'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Вот некоторые часто задаваемые вопросы:
 - Какой срок реализации проекта?
 - Есть ли гарантия на ваш продукт?
 - Какие условия оплаты?
 - Как пользоваться вашим сервисом?''', reply_markup=markup)
#FAQ_end

#Условия сотрудничества
@bot.callback_query_handler(func=lambda call: call.data == 'Условия сотрудничества')
def Uslovijasotrudnichestva_callback(call):
    button_dict = {'Описание продукта': {'text': 'Описание продукта', 'callback': 'Описание продукта'}, 'Другая информация': {'text': 'Другая информация', 'callback': 'Другая информация'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, '''Условия сотрудничества включают следующие пункты:
 - Предоплата 50%
 - Срок выполнения проекта: от 2 недель
 - Гарантия на продукт: 1 год
 - Поддержка клиента 24/7''', reply_markup=markup)
#Условия сотрудничества_end
bot.polling()