import header
from models import Log


header.show_title('Daily Log')

def create_log(message):
    Log.create(message=message)


def get_logs():
    return Log.select().order_by(Log.timestamp.asc())