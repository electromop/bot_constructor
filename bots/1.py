import telebot

bot_token = "1"
bot = telebot.Bot(bot_token)
                        
#start
@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Привет! Чем могу помочь")
#start_end



#help
@bot.message_handler(commands=['help'])
def send_message(message):
    bot.send_message(message.chat.id, "Чем могу помочь")
#help_end

#start
@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "привет")
#start_end
