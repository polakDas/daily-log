from peewee import *
from datetime import datetime

db = SqliteDatabase('log.db')

class Log(Model):
    timestamp = DateTimeField(default=datetime.now)
    message = TextField()

    class Meta:
        database = db

Log.create_table()

log1 = Log.create(message="Message 1")
log1.save()

log2 = Log.create(message="Message 2")
log2.save()

log3 = Log.create(message="Message 3")
log3.save()