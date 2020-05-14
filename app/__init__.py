from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_uploads import configure_uploads, IMAGES, UploadSet, ALL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)

#  configure Uploads
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'
images = UploadSet('images', ALL)
configure_uploads(app, images)
# ----------------------------------


#  configure DataBase
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# ----------------------------------

# login manager
login = LoginManager(app)
login.login_view = 'login'
login.login_message = "Пожалуйста, войдите, чтобы открыть личную страницу"
# ------------------------------------

from app import routes, models


