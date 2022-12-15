"""
Description of python file
"""

import os


def main_menu():
    os.system('cls')
    print('Welcome to your personal budget app!\n')
    print('Please enter 1, 2 or 3 for the following options:\n')
    print('1. Budget projection')
    print('2. Track your budget')
    print('3. Exit')
    while True:
        try: 
            option = int(input('\nChoose an option:\n'))
            if option == 3:
                print('Exiting the program. Have a nice day!')
                break
            elif option == 1:
                print('1')
            elif option == 2:
                print('2')
            else:
                print('Invalid input... Please enter 1, 2 or 3 for the following options:\n')
                print('1. Budget projection')
                print('2. Track your budget')
                print('3. Exit')
        except ValueError:
            print('Invalid input... Please enter 1, 2 or 3 for the following options:\n')
            print('1. Budget projection')
            print('2. Track your budget')
            print('3. Exit')

main_menu()