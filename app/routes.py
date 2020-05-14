# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request
from app import app, images
from app.forms import LoginForm, UploadForm
from app.models import db, FileContents
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    cars = ['Ford', 'Opel', 'Kia']
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', cars=cars, title='Sibmir', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неверно Имя или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    form =UploadForm()
    if form.validate_on_submit():
        images.save(form.upload_file.data)
        print(form.upload_file.data)
        # print(images.path(form.upload_file))
    return render_template('upload.html', form=form)


@app.route('/uploadfiles', methods=['POST'])
def uploadfiles():
    # form = UploadForm()
    # if form.validate_on_submit():
    file = request.files['inputfile']
        # newFile = FileContents(name=form.upload_file.data, data=form.upload_file.data)
        # db.session.add(newFile)
        # db.session.commit()
        # print(form.upload_file.data)
    newFile = FileContents(name=file.filename, data=file.read())
    db.session.add(newFile)
    db.session.commit()
    return render_template('uploadfiles.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

