from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
import os
from dotenv import load_dotenv
load_dotenv()


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.Email(message="That's not a valid email address.")])
    password = PasswordField('Password', [validators.Length(min=8, message="Password must be at least 8 characters.")])
    submit = SubmitField('Log in')


app = Flask(__name__)

SECRET_KEY = os.environ.get('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = "admin@email.com"
        password = "12345678"
        if form.email.data == email and form.password.data == password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
