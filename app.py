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
        option = int(input('\nChoose an option:\n'))

main_menu()