from flask import Flask, url_for, render_template, flash
from markupsafe import escape

app = Flask(__name__)

app.config['SECRET_KEY'] = 'PIGpig'

@app.route('/', methods = ['GET'])
def index():
    flash('Hello world!')
    return render_template('home.html')