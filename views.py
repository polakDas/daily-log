from models import Log


def create_log(message):
    Log.create(message=message)


def get_logs():
    return Log.select().order_by(Log.timestamp.asc()).limit(10)