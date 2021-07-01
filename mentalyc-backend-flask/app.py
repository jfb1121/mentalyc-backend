import os

from flask import Flask, jsonify, request
from flask_login import LoginManager
from flask_mongoengine import MongoEngine


# connect(host="mongodb://127.0.0.1:27017/flaskdb")
app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flaskdb',
    'host': 'mongodb',
    'port': 27017
}

for variable, value in os.environ.items():
    app.config[variable] = value

db = MongoEngine()
db.init_app(app)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

from .api.auth_api import auth
app.register_blueprint(auth)