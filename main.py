from views import create_log, get_logs


if __name__ == '__main__':
    uinput = 's'
    while uinput != 'q':
        uinput = input("Enter message: ")
        create_log(uinput)

    for log in get_logs():
        print(log.id, log.message)