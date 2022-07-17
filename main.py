import time
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


def show_submenu(lastID, logType):
    '''
    This function will show the sub-menu
    '''
    sub_menu = '0'
    while sub_menu != '2':
        print('*' * 41)

        if lastID > 5:
            print('1. Show more\t\t 2. Main menu')
        else:
            print('1. Show all\t\t 2. Main menu')

        sub_menu = input('> ')
        print('*' * 41)

        if sub_menu == '1':
            if lastID > 5:
                lastID -= 5
            else:
                lastID = 0
            
            if logType == 'positive':
                logs, lastID = get_positive_log(lastID)
            if logType == 'negative':
                logs, lastID = get_negative_log(lastID)

            show_logs(logs)
        elif sub_menu == '2':
            print("Going to main menu...")
            time.sleep(0.5)       # wait 1/2 second
        else:
            print('Invalid option. Please try again.')


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

        show_submenu(lastID, 'positive')
              
    elif choice == '4':     # Show Negative logs
        logs, lastID = get_negative_log()   # return a list and an int

        show_logs(logs)

        show_submenu(lastID, 'negative')

    elif choice == '5':     # Exit
        time.sleep(1)
        print('Bye!\n\n')
        return

    else:                   # If invalid input
        print('Invalid choice')

    print('*' * 41 + '\n')
    show_options()


if __name__ == '__main__':
    show_options()