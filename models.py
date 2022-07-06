import peewee
from datetime import datetime

from connection import BaseModel

class Log(BaseModel):
    timestamp = peewee.DateTimeField(default=datetime.now)
    message = peewee.TextField()