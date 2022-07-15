import header
from models import Log, PositiveLog, NegativeLog


header.show_title('Daily Log')

def create_log(message):
    Log.create(message=message)


def create_positive_log(title, description):
    PositiveLog.create(title=title, description=description)


def create_negative_log(title, description):
    NegativeLog.create(title=title, description=description)


def get_logs():
    return Log.select().order_by(Log.timestamp.asc())


def get_positive_log(lastID = PositiveLog.select()[-1].id):    # get the last PositiveLog from database
    pLog = PositiveLog.select()

    if lastID > 5:
        firstID = lastID - 5
    else:
        firstID = 0

    if lastID == 0:
        return pLog, lastID
    else:
        return pLog[firstID:lastID], lastID


def get_negative_log():
    return NegativeLog.select().order_by(NegativeLog.timestamp.desc())