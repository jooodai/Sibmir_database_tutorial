# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request
from app import app, images
from app.forms import LoginForm, UploadForm
from app.models import db, FileContents

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Tolya'}
    cars = ['Ford', 'Opel', 'Kia']
    return render_template('index.html', user=user, cars=cars, title='Sibmir')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    form =UploadForm()
    if form.validate_on_submit():
        images.save(form.upload_file.data)
        print(form.upload_file.data)
        # print(images.path(form.upload_file))
    return render_template('upload.html', form=form)


@app.route('/uploadfiles', methods=['POST', 'GET'])
def uploadfiles():
    form = UploadForm()
    if form.validate_on_submit():
        file = request.files['inputfile']
        newFile = FileContents(name=form.upload_file.data, data=form.read())
        db.session.add(newFile)
        db.session.commit()
    return 'Saved!'