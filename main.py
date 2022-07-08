from views import create_log, get_logs


def show_options():
    print('What do you want to do?')
    print('1. Create a log\t\t 2. Show all logs')
    print('3. Exit')
    choice = input('> ')
    main(choice)


def main(choice):
    if choice == '1':
        message = input('Enter a message: ')
        create_log(message)
        print("Log created!\n")
    elif choice == '2':
        for log in get_logs():
            print(f"{log.id:<2} | {log.message:<20} - {log.timestamp.strftime('%d %B, %Y')}")
    elif choice == '3':
        print('Bye!')
        return
    else:
        print('Invalid choice')

    print('*' * 40 + '\n')
    show_options()


if __name__ == '__main__':
    show_options()