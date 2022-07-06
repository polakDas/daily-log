import peewee

from .connection import BaseModel

class Log(BaseModel):
    timestamp = peewee.DateTimeField(default=peewee.datetime.datetime.now)
    message = peewee.TextField()