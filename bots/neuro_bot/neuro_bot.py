import telebot
from telebot import types

bot_token = "6434108320:AAHcb8OpYIPpTKEpCFcpkD0zgl32HmLGMcM"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LISTstart,Да, конечно!,Расскажи мне больше!,Покажи примеры систем полива,Что еще интересного?,Нет, спасибо,Какие еще боты есть?,Бот-кулинар,Бот-путешественник,Бот-спортсмен,#COMMANDS_LIST_END



#start
@bot.message_handler(commands=['start'])
def start_message(message):
    button_dict = {'Да, конечно!': {'text': 'Да, конечно!', 'callback': 'Да, конечно!'}, 'Нет, спасибо': {'text': 'Нет, спасибо', 'callback': 'Нет, спасибо'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Я бот-эксперт по системам полива растений. Хочешь узнать все о них?", reply_markup=markup)
#start_end

#Да, конечно!
@bot.callback_query_handler(func=lambda call: call.data == 'Да, конечно!')
def Dakonechno_callback(call):
    button_dict = {'Расскажи мне больше!': {'text': 'Расскажи мне больше!', 'callback': 'Расскажи мне больше!'}, 'Покажи примеры систем полива': {'text': 'Покажи примеры систем полива', 'callback': 'Покажи примеры систем полива'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, "Отлично! Давай начнем! Системы полива растений - это специальные устройства, которые автоматически поддерживают оптимальный уровень влажности для растений. Они оснащены датчиками и насосами, которые контролируют подачу воды. Благодаря таким системам растения получают необходимое количество влаги без участия человека.", reply_markup=markup)
#Да, конечно!_end

#Расскажи мне больше!
@bot.callback_query_handler(func=lambda call: call.data == 'Расскажи мне больше!')
def Rasskazhimnebolshe_callback(call):
    button_dict = {'Покажи примеры систем полива': {'text': 'Покажи примеры систем полива', 'callback': 'Покажи примеры систем полива'}, 'Что еще интересного?': {'text': 'Что еще интересного?', 'callback': 'Что еще интересного?'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, "Конечно! Есть разные типы систем полива растений. Например, капельный полив - это система, при которой вода поступает прямо к корням растений через маленькие капельницы. Это позволяет экономично использовать воду и доставлять ее непосредственно к растению. Еще один популярный тип - это распылительный полив, при котором вода распыляется и покрывает большую площадь. Каждый тип системы полива имеет свои преимущества и подходит для разных условий выращивания растений.", reply_markup=markup)
#Расскажи мне больше!_end

#Покажи примеры систем полива
@bot.callback_query_handler(func=lambda call: call.data == 'Покажи примеры систем полива')
def Pokazhiprimerysistempoliva_callback(call):
    button_dict = {'Расскажи мне больше!': {'text': 'Расскажи мне больше!', 'callback': 'Расскажи мне больше!'}, 'Что еще интересного?': {'text': 'Что еще интересного?', 'callback': 'Что еще интересного?'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, "Хорошо! Вот несколько примеров систем полива: капельная лента, которая распределяет воду по всей длине грядки; спринклеры, которые обеспечивают равномерное покрытие большой площади; автоматические системы полива, которые работают по заданной программе и контролируют влажность почвы. Все эти системы помогают сэкономить время и ресурсы при поливе растений.", reply_markup=markup)
#Покажи примеры систем полива_end

#Что еще интересного?
@bot.callback_query_handler(func=lambda call: call.data == 'Что еще интересного?')
def Chtoescheinteresnogo_callback(call):
    button_dict = {'Расскажи мне больше!': {'text': 'Расскажи мне больше!', 'callback': 'Расскажи мне больше!'}, 'Покажи примеры систем полива': {'text': 'Покажи примеры систем полива', 'callback': 'Покажи примеры систем полива'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, "Кстати, системы полива растений могут быть управляемыми с помощью смартфона или компьютера. Ты можешь настроить необходимые параметры полива и следить за состоянием растений удаленно. Это очень удобно, особенно если ты долго отсутствуешь дома и нужно обеспечить растения постоянным поливом. И помни, правильный полив - залог красивого и здорового роста твоих растений!", reply_markup=markup)
#Что еще интересного?_end

#Нет, спасибо
@bot.callback_query_handler(func=lambda call: call.data == 'Нет, спасибо')
def Netspasibo_callback(call):
    button_dict = {'Какие еще боты есть?': {'text': 'Какие еще боты есть?', 'callback': 'Какие еще боты есть?'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, "Хорошо, если у тебя возникнут вопросы, обращайся! Удачи в уходе за растениями!", reply_markup=markup)
#Нет, спасибо_end

#Какие еще боты есть?
@bot.callback_query_handler(func=lambda call: call.data == 'Какие еще боты есть?')
def Kakieeschebotyest_callback(call):
    button_dict = {'Бот-кулинар': {'text': 'Бот-кулинар', 'callback': 'Бот-кулинар'}, 'Бот-путешественник': {'text': 'Бот-путешественник', 'callback': 'Бот-путешественник'}, 'Бот-спортсмен': {'text': 'Бот-спортсмен', 'callback': 'Бот-спортсмен'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, "У меня есть еще много интересных ботов! Например, бот-кулинар, бот-путешественник и бот-спортсмен. Выбери тот, который тебе интересен, и я расскажу о нем подробнее!", reply_markup=markup)
#Какие еще боты есть?_end

#Бот-кулинар
@bot.callback_query_handler(func=lambda call: call.data == 'Бот-кулинар')
def Botkulinar_callback(call):
    button_dict = {'Какие еще боты есть?': {'text': 'Какие еще боты есть?', 'callback': 'Какие еще боты есть?'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, "Бот-кулинар - это настоящий повар в твоем телефоне! Он поможет тебе найти рецепты на любой вкус и подскажет, как готовить разные блюда. Ты сможешь попробовать себя в роли шеф-повара и удивить своих близких вкусными и оригинальными блюдами!", reply_markup=markup)
#Бот-кулинар_end

#Бот-путешественник
@bot.callback_query_handler(func=lambda call: call.data == 'Бот-путешественник')
def Botputeshestvennik_callback(call):
    button_dict = {'Какие еще боты есть?': {'text': 'Какие еще боты есть?', 'callback': 'Какие еще боты есть?'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, "Бот-путешественник - это твой гид по интересным местам мира! Он расскажет о самых красивых достопримечательностях, покажет фотографии и даст советы, как лучше спланировать свою поездку. Ты узнаешь много нового о разных странах и сможешь выбрать ту, которую хочешь посетить!", reply_markup=markup)
#Бот-путешественник_end

#Бот-спортсмен
@bot.callback_query_handler(func=lambda call: call.data == 'Бот-спортсмен')
def Botsportsmen_callback(call):
    button_dict = {'Какие еще боты есть?': {'text': 'Какие еще боты есть?', 'callback': 'Какие еще боты есть?'}}
    buttons = [
    types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    bot.send_message(call.message.chat.id, "Бот-спортсмен - твой личный тренер по фитнесу! Он поможет подобрать упражнения, составить тренировочный план и даст советы по правильному питанию. Ты сможешь заниматься спортом дома и добиться отличных результатов!", reply_markup=markup)
#Бот-спортсмен_end
bot.polling()