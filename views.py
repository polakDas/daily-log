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


def get_positive_log(fid = -1, lid = 0):    # get first ID and last ID to show logs
    pLog = PositiveLog.select()

    lastID = PositiveLog.select()[-1].id

    if lastID < 5:
        return pLog
    else:
        firstID = lastID - 5
        context = {
            'last_id': lastID,
            'positive_log': pLog[firstID:lastID]
        }
        return context
    
    # print(dir(PositiveLog.select().order_by()))
    # print(PositiveLog.select().order_by(PositiveLog.id.desc()))
    
    # return pLog[lid:]


def get_negative_log():
    return NegativeLog.select().order_by(NegativeLog.timestamp.desc())