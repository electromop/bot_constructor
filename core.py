from bot_file import BotFile
from flask import Flask, render_template

app = Flask("main", template_folder="templates")

@app.route('/')
def main():
    return render_template('bot_choose.html')

@app.route('/<bot_token>')
def bot_edit_page(bot_token):
    return render_template('bot_edit.html')

@app.route('/add_new_bot/<bot_token>')
def add_new_bot(bot_token):
    bot = BotFile(bot_token)
    print(f"Создан бот с токеном: {bot_token}")
    return BotFile.get_code()

@app.route('/<bot_token>/show_code')
def show_code(bot_token):
    bot = BotFile(bot_token)
    code = bot.get_code()
    return code

@app.route('/<bot_token>/add_handler/<command>7&<text>')
def add_handler(bot_token, command, text):
    bot = BotFile(bot_token)
    bot.add_simple_handler(command, text)
    return show_code(bot_token)

@app.route('/<bot_token>/delete_handler/<command>')
def delete_handler(bot_token, command):
    bot = BotFile(bot_token)
    bot.delete_simple_handler(command)
    return show_code(bot_token)

if __name__ == "__main__":
    app.run()
