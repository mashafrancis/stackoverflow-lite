from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'francis'}
    questions = [
        {
            'author': {'username': 'Francis'},
            'question': 'What is Python?'
        },
        {
            'author': {'username': 'Masha'},
            'question': 'Do you like coding?'
        }
    ]
    return render_template('index.html', title='Home', user=user, questions=questions)


@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
