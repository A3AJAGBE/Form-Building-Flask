from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
import os
from dotenv import load_dotenv
load_dotenv()


class LoginForm(FlaskForm):
    email = StringField('Name')
    password = StringField('Password')


app = Flask(__name__)

SECRET_KEY = os.environ.get('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
