from flask import Flask, url_for, render_template, flash, request, redirect
from markupsafe import escape

app = Flask(__name__)

app.config['SECRET_KEY'] = 'PIGpig'

@app.route('/')
@app.route('/index')
def index():
    # flash('Hello world!')
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username not in user or user[username] != password:
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        else:
            return render_template('home.html', username = username)
    return render_template('login.html')

user = {
    'carbide' : '123456'
}