import telebot
from telebot import types
from bot_file import BotFile
from user import User

bot = telebot.TeleBot("6434108320:AAHcb8OpYIPpTKEpCFcpkD0zgl32HmLGMcM")

class InlineKeyboard:
    def __init__(self, buttons_list, ncol=2):
        self.buttons_list = buttons_list
        self.ncol = ncol
        self.buttons_dict = dict(zip(buttons_list, buttons_list))
    
    def make(self, callback_prefix="", callback_postfix=""):
        button_dict = {}
        for i in self.buttons_list:
            button_dict[i] = {'text':i, 'callback':callback_prefix+i+callback_postfix}
        buttons = [
        types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
        ]
        markup = types.InlineKeyboardMarkup(row_width=self.ncol)
        markup.add(*buttons)
        return markup

@bot.message_handler(commands=["start"])
def start(message):
    kb = InlineKeyboard(["Создать бота", "Мои боты"])
    bot.send_message(message.chat.id, "Привет! Воспользуйся меню ниже.", reply_markup=kb.make())

@bot.callback_query_handler(func=lambda call: call.data == "Создать бота")
def new_bot(callback):
    kb = InlineKeyboard(["Инструкция"])
    bot.send_message(callback.message.chat.id, "Напиши токен бота. \nИнструкцию, где взять токен, можно найти по кнопке ниже.", reply_markup=kb.make())
    bot.register_next_step_handler(callback.message, new_bot_token)

def new_bot_token(message):
    botfile = BotFile(message.text)
    kb = InlineKeyboard(["Мои боты"])
    bot.send_message(message.chat.id, f"Отлично! Добавлен бот с токеном ```{message.text}```", reply_markup=kb.make())
#     bot.register_next_step_handler(message, mb_neuro)

# def mb_neuro(message):


@bot.callback_query_handler(func=lambda call: call.data == "Мои боты")
def my_bots(callback):
    user = User("root")
    bots_list = user.get_bots()
    kb = InlineKeyboard(bots_list)
    bot.send_message(callback.message.chat.id, "Выбери к какому боту перейти:", reply_markup=kb.make(callback_prefix="bot_"))

@bot.callback_query_handler(func=lambda call: call.data[0:4] == "bot_")
def my_bots(callback):
    token = callback.data[4:]
    kb = InlineKeyboard(["Добавить команду", "Добавить действие на кнопку", "Посмотреть список команд"])
    bot.send_message(callback.message.chat.id, "Вы в редакторе бота", reply_markup=kb.make(callback_prefix=f'edit_{token}'))

@bot.callback_query_handler(func=lambda call: call.data[0:4] == "bot_")
def my_bots(callback):
    token = callback.data[4:]
    kb = InlineKeyboard(["Добавить команду", "Добавить действие на кнопку", "Посмотреть список команд"])
    bot.send_message(callback.message.chat.id, "Вы в редакторе бота", reply_markup=kb.make(callback_prefix=f'edit_{token}'))
    
bot.polling()