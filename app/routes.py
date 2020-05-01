# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Tolya'}
    cars = ['Ford', 'Opel', 'Kia']
    return render_template('index.html', user=user, cars=cars)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)



