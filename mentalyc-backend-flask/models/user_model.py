import datetime
from ..app import login_manager
from flask_login.mixins import UserMixin
from mongoengine import Document
from mongoengine.fields import DateTimeField, EmailField, StringField

@login_manager.user_loader
def load_user(user_email):
    return User.objects.get(email=user_email)


class User(UserMixin, Document):
    meta = {'collection': '<---YOUR_COLLECTION_NAME--->'}
    email = EmailField(required=True)
    password = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    created_date =  DateTimeField(default=datetime.datetime.now)

    def get_id(self):
        return self.email


# class User(UserMixin, document):
#     email = StringField(max_length=200)
#     password = StringField()

    
# @login_manager.user_loader
# def load_user(user_id):
#     return User.objects(pk=user_id).first()