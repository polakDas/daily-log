import peewee
from datetime import datetime

from connection import BaseModel

class Log(BaseModel):
    timestamp = peewee.DateTimeField(default=datetime.now)
    message = peewee.TextField()

class PositiveLog(BaseModel):
    title = peewee.CharField(max_length=100, null=True)
    description = peewee.TextField(null=True)
    timestamp = peewee.DateTimeField(default=datetime.now)


class NegativeLog(BaseModel):
    title = peewee.CharField(max_length=100, null=True)
    description = peewee.TextField(null=True)
    timestamp = peewee.DateTimeField(default=datetime.now)
