# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Tolya'}
    cars = ['Ford', 'Opel', 'Kia']
    return render_template('index.html', user=user, cars=cars)




