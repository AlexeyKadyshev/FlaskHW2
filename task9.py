# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.
from flask import Flask, render_template, request, redirect, url_for, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('log.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
