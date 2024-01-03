from keyboard import Keyboard
class Handler:
    def __init__(self, handler_type, key_word, buttons:bool=False, buttons_list=None, ncol=2):
        self.handler = "command" if handler_type == 0 else "callback"
        self.key_word = key_word
        self.buttons = buttons
        self.buttons_list = buttons_list if self.buttons else None
        self.ncol = ncol

    def make(self, message_text):
        keyboard_space, markup = [Keyboard(self.buttons_list, ncol=self.ncol), ", reply_markup=markup"] if self.buttons else ["", ""]
        handler_string = f'''
#{self.key_word}
@bot.message_handler(commands=['{self.key_word}'])
def send_message(message):
    {keyboard_space}
    bot.send_message(message.chat.id, "{message_text}"{markup})
#{self.key_word}_end
'''
        return handler_string

test_handler = Handler(0, "start")
print(test_handler.make("Привет"))
