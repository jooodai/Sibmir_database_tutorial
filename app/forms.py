from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Логин:', validators=[DataRequired()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    remember_me = BooleanField('Remeber Me')
    submit = SubmitField('Войти')


class UploadForm(FlaskForm):
    upload_file = FileField('Файл')
    submit = SubmitField('Загрузить')

    

