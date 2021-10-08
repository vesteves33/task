from mongoengine import *
from mongoengine.base.fields import ObjectIdField
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, ListField, StringField
from datetime import datetime

class Task(Document):
    id = ObjectIdField
    title = StringField(min_length=3, max_length=70, required=True)
    description = StringField(max_length=255)
    priority = ListField(['Very high', 'High', 'Medium', 'Low', 'Very low'])
    status = ListField(['Backlog', 'In progress', 'Completed'])
    created_at = DateTimeField(default=datetime.utcnow) 
    updated_at = DateTimeField(default=datetime.utcfromtimestamp)