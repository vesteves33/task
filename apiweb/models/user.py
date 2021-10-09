from datetime import datetime
import mongoengine 


class User(mongoengine.Document):
    name = mongoengine.StringField(min_length=3, max_length=30)
    lastName = mongoengine.StringField(min_length=3, max_length=60)
    cpf = mongoengine.IntField(max_value=11)
    email = mongoengine.EmailField(allow_utf8_user=True)
    username = mongoengine.StringField()
    password = mongoengine.StringField(min_length=6, max_length=16, regex='[A-Za-z0-9"]')
    created_at = mongoengine.DateTimeField(default=datetime.utcnow)
    updated_at = mongoengine.DateTimeField(default=datetime.utcfromtimestamp)


    