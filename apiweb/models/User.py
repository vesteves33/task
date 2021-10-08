from mongoengine import *
from mongoengine.base.fields import ObjectIdField
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, EmailField, IntField, StringField
from datetime import datetime


class User(Document):
    id = ObjectIdField
    name = StringField(min_length=3, max_length=30, required=True)
    lastName = StringField(min_length=3, max_length=60, required=True)
    cpf = IntField(max_value=11, required=True)
    email = EmailField(allow_utf8_user=True)
    password = StringField(min_length=6, max_length=16, regex='[A-Za-z0-9"]', )
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcfromtimestamp)