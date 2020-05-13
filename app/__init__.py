from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_uploads import configure_uploads, IMAGES, UploadSet, ALL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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

from app import routes, models


