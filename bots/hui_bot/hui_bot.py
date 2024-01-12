import telebot
from telebot import types

bot_token = "6434108320:AAHcb8OpYIPpTKEpCFcpkD0zgl32HmLGMcM"
bot = telebot.TeleBot(bot_token)
#COMMANDS_LIST#COMMANDS_LIST_END

bot.polling()
