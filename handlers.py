class Handler:
    def __init__(self, handler_type, key_word):
        self.handler = "command" if handler_type == 0 else "callback"
        self.key_word = key_word

    def make(self, message_text):
        handler_string = f'''
#{self.key_word}
@bot.message_handler(commands=['{self.key_word}'])
def send_message(message):
    bot.send_message(message.chat.id, "{message_text}")
#{self.key_word}_end
'''
        return handler_string
