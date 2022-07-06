import peewee
from datetime import datetime

db = SqliteDatabase('log.db')

class Log(Model):
    timestamp = DateTimeField(default=datetime.now)
    message = TextField()

    class Meta:
        database = db

Log.create_table()

def create_log(message):
    Log.create(message=message)


def get_logs():
    return Log.select().order_by(Log.timestamp.desc())


if __name__ == '__main__':
    uinput = 's'
    while uinput != 'q':
        uinput = input("Enter message: ")
        create_log(uinput)

    for log in get_logs():
        print(log.timestamp, log.message)

# log1, created = Log.get_or_create(message="Message 1")
# log1.save()

# if created:
#     print(created)
#     print(log1)


# log2, created = Log.get_or_create(message="Message 2")
# log2.save()

# if created:
#     print(created)


# log3, created = Log.get_or_create(message="Message 2         ".strip())
# log3.save()

# if created:
    # print(created)