def filter_log(lastID, paginatedBy = 5):
    if lastID > paginatedBy:
        firstID = lastID - paginatedBy
    else:
        firstID = 0

    return firstID