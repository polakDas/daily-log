from views import create_log, get_logs, create_positive_log, create_negative_log, get_positive_log, get_negative_log


def show_options():
    print('What do you want to do?')
    print('1. Create Positive log\t\t 2. Create Negative log')
    print('3. Show Positive logs\t\t 4. Show Negative logs')
    print('5. Exit')
    choice = input('> ')
    main(choice)


def main(choice):
    print('\n' + '*' * 41)
    if choice == '1':
        title = input('Enter Title: ')
        description = input('Enter description: ')
        create_positive_log(title, description)
        print("Log created! :)\n")
    elif choice == '2':
        title = input('Enter title: ')
        description = input('Enter description: ')
        create_negative_log(title, description)
        print("Log created. :(\n")
    elif choice == '3':
        for log in get_positive_log().items():
            # if len(log.title) > 20:
            #     print(f"{log.id:<2} | {log.title[:18]}.. - {log.timestamp.strftime('%d %B, %Y')}")
            # else:
            #     print(f"{log.id:<2} | {log.title:<20} - {log.timestamp.strftime('%d %B, %Y')}")
            print(log[1])
    elif choice == '4':
        for log in get_negative_log():
            print(f"{log.id:<2} | {log.title:<20} - {log.timestamp.strftime('%d %B, %Y')}")
    elif choice == '5':
        print('Bye!')
        return
    else:
        print('Invalid choice')

    print('*' * 41 + '\n')
    show_options()


if __name__ == '__main__':
    show_options()