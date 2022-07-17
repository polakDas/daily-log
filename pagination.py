def paginate(lastID, num = 5):
    if lastID > num:
        firstID = lastID - num
    else:
        firstID = 0

    return firstID