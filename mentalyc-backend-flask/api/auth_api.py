from flask import Blueprint
from flask.globals import request
from flask.json import jsonify
from flask_login.utils import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.user_model import User

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['POST'])
def login():
    json_data = request.get_json(force=True)
    user = User.objects(email=json_data['email']).first()
    if user is None:
        return jsonify({'success': False, 'err': 'Email not registered'})
    pwhash = user.password 
    
    if check_password_hash(pwhash, json_data["password"]) is True:
        login_user(user)
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False,  'err': 'Invalid password'})


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'success': True}), 200

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        existing_user = User.objects(email=json_data['email']).first()
        if existing_user is None:
            hashpass = generate_password_hash(json_data['password'], method='sha256')
            new_user = User(email=json_data['email'],password=hashpass).save()
            login_user(new_user)
        else:
            return jsonify({'success': False, 'err': 'Email already registered'})
    return jsonify({'success': True}), 200