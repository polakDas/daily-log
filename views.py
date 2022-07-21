import header
from models import PositiveLog, NegativeLog
from filter_log import filter_log


header.show_title('Daily Log')


def create_positive_log(title, description):
    PositiveLog.create(title=title, description=description)


def create_negative_log(title, description):
    NegativeLog.create(title=title, description=description)


try:
    last_positive_log = PositiveLog.select()[-1].id
except:
    last_positive_log = 0

def get_positive_log(lastID = last_positive_log):    # default is last PositiveLog from database
    pLog = PositiveLog.select()

    firstID = filter_log(lastID=lastID, paginatedBy=5)

    if lastID == 0:
        return pLog, lastID
    else:
        try:
            return pLog[firstID:lastID], lastID
        except:
            print("There are no positive log yet!!")
            return


try:
    last_negative_log = NegativeLog.select()[-1].id
except:
    last_negative_log = 0

def get_negative_log(lastID = last_negative_log):     # default is last NegativeLog from database
    nLog =  NegativeLog.select()

    firstID = filter_log(lastID=lastID, paginatedBy=5)
    
    if lastID == 0:
        return nLog, lastID
    else:
        try:
            return nLog[firstID:lastID], lastID
        except:
            print("There are no log yet!!")
            return