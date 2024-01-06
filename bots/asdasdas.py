import telebot
from telebot import types

bot_token = "asdasdas"
bot = telebot.Bot(bot_token)
#COMMANDS_LISTstart,help,start,help,das,help,#COMMANDS_LIST_END






#help
@bot.callback_query_handler(func=lambda call: call.data == 'help')
def help_callback(call):
    
    bot.send_message(call.message.chat.id, "dasd")
#help_end