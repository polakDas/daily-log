import peewee

db = peewee.SqliteDatabase('log.db')

class BaseModel(peewee.Model):
    class Meta:
        database = db