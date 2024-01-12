import telebot
from telebot import types

bot_token = "6788944411:AAFJDlLmpjvocCtNkgtTqsfSoYjU5UNWDc4"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END

bot.polling()
