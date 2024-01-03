class Keyboard:
    def __init__(self, buttons_list, ncol=2):
        self.buttons_list = buttons_list
        self.ncol = ncol
        self.buttons_dict = dict(zip(buttons_list, buttons_list))
    
    def __str__(self):
        button_dict = {}
        for i in self.buttons_list:
            button_dict[i] = {'text':i, 'callback':i}
        
        return f'''button_dict = {button_dict}
        buttons = [
        types.InlineKeyboardButton(button_dict[button]['text'], callback_data=button_dict[button]['callback']) for button in button_dict
        ]
        markup = types.InlineKeyboardMarkup(row_width={self.ncol})
        markup.add(*buttons)'''
