from bot_file import BotFile
from user import User
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask("main", template_folder="templates")

app.secret_key = 'secret_key_for_session'  # Секретный ключ для сессий

# Простая имитация базы данных пользователей
users = {'user1': 'password1', 'user2': 'password2', 'root':'root'}

@app.route('/')
def authorization():
    return render_template('login.html')

# Выход из учетной записи
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('authorization'))

# Роут для обработки логина
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('home'))
    return 'Неправильное имя пользователя или пароль!'

@app.route('/get_user_bots')
def get_users_bots():
    if session.get('logged_in'):
        username = session['username']
        user = User(username)
        bots_list = user.get_bots()
        print(bots_list)
        return bots_list
    else:
        return redirect(url_for('authorization'))

@app.route('/home')
def home():
    if session.get('logged_in'):
        username = session['username']
        return render_template('bot_choose.html', username=username)
    else:
        return redirect(url_for('authorization'))

@app.route('/<bot_token>')
def bot_edit_page(bot_token):
    return render_template('bot_edit.html')

@app.route('/add_new_bot/<bot_token>')
def add_new_bot(bot_token):
    if session.get('logged_in'):
        bot = BotFile(bot_token)
        print(f"Создан бот с токеном: {bot.token}")

        user = User(session["username"])
        user.add_bot(bot_token)
        return bot_token
    else:
        return redirect(url_for('authorization'))

@app.route('/<bot_token>/show_code')
def show_code(bot_token):
    bot = BotFile(bot_token)
    code = bot.get_code()
    return code

@app.route('/<bot_token>/add_handler/<command>7&<text>7&<button_list>7&<colmun_count>')
def add_handler(bot_token, command, text, button_list, colmun_count):
    bot = BotFile(bot_token)
    buttons = True if button_list != "" else False
    print(buttons)
    bot.add_simple_handler(command, text, buttons=buttons, buttons_list=button_list.split(","), ncol=int(colmun_count))
    return bot.get_code()

@app.route('/<bot_token>/delete_handler/<command>')
def delete_handler(bot_token, command):
    bot = BotFile(bot_token)
    bot.delete_simple_handler(command)
    return show_code(bot_token)

@app.route('/<bot_token>/add_callback/<command>7&<text>')
def add_callback(bot_token, command, text):
    bot = BotFile(bot_token)
    bot.add_query_handler(command, text)
    return show_code(bot_token)

if __name__ == "__main__":
    app.run()
