from views import create_log, get_logs, create_positive_log, create_negative_log, get_positive_log, get_negative_log


def show_options():
    '''
    This function will display the options for user
    These options are hardcoded
    '''
    print('What do you want to do?')
    print('1. Create Positive log\t\t 2. Create Negative log')
    print('3. Show Positive logs\t\t 4. Show Negative logs')
    print('5. Exit')
    choice = input('> ')
    main(choice)


def show_logs(logs):
    # this function will show logs one by one from log database
    for log in logs:
        if len(log.title) > 20:
            print(f"{log.id:<2} | {log.title[:18]}.. - {log.timestamp.strftime('%d %B, %Y')}")
        else:
            print(f"{log.id:<2} | {log.title:<20} - {log.timestamp.strftime('%d %B, %Y')}")


def main(choice):
    '''
    This is the main function that runs first and decide what to do
    This function will take a choice from the user and run the appropriate function for user
    '''
    print('\n' + '*' * 41)

    if choice == '1':       # Create Positive log
        title = input('Enter Title: ')
        description = input('Enter description: ')
        create_positive_log(title, description)
        print("Log created! :)\n")

    elif choice == '2':     # Create Negative log
        title = input('Enter title: ')
        description = input('Enter description: ')
        create_negative_log(title, description)
        print("Log created. :(\n")

    elif choice == '3':     # Show positive logs
        logs, lastID = get_positive_log()   # returns two values (list and int)

        show_logs(logs)

        subChoice = '0'
        while subChoice != '2':
            print('*' * 41)

            if lastID > 5:
                print('1. Show more\t\t 2. Main menu')
            else:
                print('1. Show all\t\t 2. Main menu')

            subChoice = input('> ')
            print('*' * 41)

            if subChoice == '1':
                if lastID > 5:
                    lastID -= 5
                else:
                    lastID = 0
                logs, lastID = get_positive_log(lastID)
                show_logs(logs)
            else:
                print('Invalid option. Please try again.')
                
    elif choice == '4':     # Show Negative logs
        for log in get_negative_log():
            print(f"{log.id:<2} | {log.title:<20} - {log.timestamp.strftime('%d %B, %Y')}")

    elif choice == '5':     # Exit
        print('Bye!')
        return

    else:                   # If invalid input
        print('Invalid choice')

    print('*' * 41 + '\n')
    show_options()


if __name__ == '__main__':
    show_options()