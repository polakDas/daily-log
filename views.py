import header
from models import Log, PositiveLog, NegativeLog
from pagination import paginate


header.show_title('Daily Log')

def create_log(message):
    Log.create(message=message)


def create_positive_log(title, description):
    PositiveLog.create(title=title, description=description)


def create_negative_log(title, description):
    NegativeLog.create(title=title, description=description)


def get_logs():
    return Log.select().order_by(Log.timestamp.asc())


def get_positive_log(lastID = PositiveLog.select()[-1].id):    # default is last PositiveLog from database
    pLog = PositiveLog.select()

    firstID = paginate(lastID)

    if lastID == 0:
        return pLog, lastID
    else:
        return pLog[firstID:lastID], lastID


def get_negative_log(lastID = NegativeLog.select()[-1].id):     # default is last NegativeLog from database
    nLog =  NegativeLog.select()

    firstID = paginate(lastID)
    
    if lastID == 0:
        return nLog, lastID
    else:
        return nLog[firstID:lastID], lastID