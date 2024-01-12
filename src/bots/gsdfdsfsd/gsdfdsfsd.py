import telebot
from telebot import types

bot_token = "fsdfsdfs"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END

bot.polling()
